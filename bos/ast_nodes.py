import sys
from abc import ABC, abstractmethod
from collections.abc import Generator
from enum import Enum
from math import floor
from types import SimpleNamespace
from typing import Literal, Any, Union, ClassVar

from antlr4 import ParserRuleContext
from pydantic import BaseModel, computed_field, model_serializer

from bos.gen.BosParser import BosParser
from code_error import CodeError
from code_location import CodeLocation


class ASTNode(BaseModel, ABC):

    @computed_field
    @property
    def node_name(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def value(self) -> Any:
        pass

    @model_serializer()
    def serialize(self) -> dict[str, Any]:
        if isinstance(self, UndefNode):
            sys.stderr.write(
                f'!! Parser Node was not converted to an AST Node: {self._parser_node.__class__.__name__} !!\n'
            )

        value = self.value()
        if isinstance(value, SimpleNamespace):
            value = dict(vars(value))

        if isinstance(value, dict):
            value = {
                k: (v.model_dump()) if isinstance(v, BaseModel) else v
                for k, v in value.items()
            }

            value = {
                k: [item.model_dump() if isinstance(item, BaseModel) else item for item in v]
                if isinstance(v, list) else v
                for k, v in value.items()
            }

        return {self.node_name: value}

    _parser_node: Union[ParserRuleContext, None]

    def __init__(self, parser_node: ParserRuleContext = None, **kwargs):
        super().__init__(**kwargs)
        self._parser_node = parser_node

    @property
    def parser_node(self) -> Union[ParserRuleContext, None]:
        return self._parser_node


class UndefNode(ASTNode):
    contents: Any

    @computed_field
    @property
    def node_name(self) -> str:
        return "Undef__" + self._parser_node.__class__.__name__.removesuffix('Context')

    def value(self):
        return self.contents


class ValueNode(ASTNode, ABC):
    ...


class NameNode(ASTNode):
    name: str

    def value(self):
        return self.name

    @model_serializer()
    def serialize(self) -> str:
        return f'{self.node_name}(\'{self.name}\')'

    def __eq__(self, other):
        return isinstance(other, NameNode) and self.name.lower() == other.name.lower()

    def __hash__(self):
        return hash(self.name.lower())

    def __repr__(self):
        return f'{self.node_name}(\'{self.name}\')'


class PieceName(NameNode, ValueNode):
    ...


class Declaration(ASTNode, ABC):
    ...


class PieceDeclaration(Declaration):
    names: list[PieceName]

    def value(self):
        return self.names

    def __iter__(self) -> Generator[PieceName]:
        yield from self.names


class VarName(NameNode):
    ...


class StaticVarDeclaration(Declaration):
    names: list[VarName]

    def value(self):
        return self.names

    def __iter__(self) -> Generator[VarName]:
        yield from self.names


class FuncName(NameNode):
    ...


class Expression(ASTNode, ABC):
    ...


class ExpressionOp(Enum):
    MULT = BosParser.OP_MULT
    DIV = BosParser.OP_DIV
    MOD = BosParser.OP_MOD
    ADD = BosParser.OP_ADD
    MINUS = BosParser.OP_MINUS

    COMP_LESS = BosParser.COMP_LESS
    COMP_LESS_EQUAL = BosParser.COMP_LESS_EQUAL
    COMP_GREATER = BosParser.COMP_GREATER
    COMP_GREATER_EQUAL = BosParser.COMP_GREATER_EQUAL
    COMP_EQUAL = BosParser.COMP_EQUAL
    COMP_NOT_EQUAL = BosParser.COMP_NOT_EQUAL

    BITWISE_AND = BosParser.BITWISE_AND
    BITWISE_OR = BosParser.BITWISE_OR
    BITWISE_XOR = BosParser.BITWISE_XOR

    LOGICAL_AND = BosParser.LOGICAL_AND
    LOGICAL_OR = BosParser.LOGICAL_OR
    LOGICAL_XOR = BosParser.LOGICAL_XOR
    LOGICAL_NOT = BosParser.LOGICAL_NOT

    def __repr__(self):
        return f'ExpressionOp.{self.name}'


class UnaryExpression(Expression):
    op: ExpressionOp
    operand: Expression | ValueNode

    def value(self):
        return SimpleNamespace(op=self.op, operand=self.operand)


class BinaryExpression(Expression):
    operand1: Expression | ValueNode
    op: ExpressionOp
    operand2: Expression | ValueNode

    def value(self):
        return SimpleNamespace(operand1=self.operand1, op=self.op, operand2=self.operand2)


class Constant(ValueNode):
    LINEAR_SCALE: ClassVar[int] = 65536
    ANGULAR_SCALE: ClassVar[int] = 182

    base_value: int | float
    const_type: Literal['normal', 'angular', 'linear'] = 'normal'

    def __init__(self, /, value: float | int | str, **kwargs):
        const_type: Literal['normal', 'angular', 'linear'] = 'normal'
        if isinstance(value, str):
            if value[0] == '[' and value[-1] == ']':
                const_type = 'linear'
            elif value[0] == '<' and value[-1] == '>':
                const_type = 'angular'
            value = value.strip('()[]<>')
            if '.' in value:
                value = float(value)
            elif value.startswith('0x'):
                value = int(value, base=16)
            else:
                value = int(value)
        super().__init__(**kwargs, base_value=value, const_type=const_type)

    def __repr__(self):
        if self.const_type == 'normal':
            return f'Constant({self.base_value})'
        if self.const_type == 'angular':
            return f'Constant(\'<{self.base_value}> degrees\')'
        if self.const_type == 'linear':
            return f'Constant(\'[{self.base_value}] units\')'

    def number_value(self) -> int | float:
        match self.const_type:
            case 'linear':
                return self.LINEAR_SCALE * self.base_value
            case 'angular':
                return self.ANGULAR_SCALE * self.base_value
            case _:
                return self.base_value

    def int32_value(self) -> int:
        number_value = self.number_value()
        int_value = int(round(number_value))
        if int_value > 0xFFFF_FFFF or int_value < -0x8000_0000:
            raise CodeError(
                f'{"Overflow" if int_value > 0 else "Underflow"} error compiling constant {self.model_dump()}. '
                f'Computed value (int_value) cannot fit inside a 32bit int',
                CodeLocation.from_parser_node(self.parser_node)
            )

        # force large unsigned ints to fit
        if int_value > 0x7FFF_FFFF:
            int_value -= 0x1_0000_0000
            if isinstance(self.base_value, float):
                print(
                    f'[WARNING] Converted float from {self.model_dump()} (computed: {number_value}) to very large negative int {int_value}',
                    CodeLocation.from_parser_node(self.parser_node)
                )

        return int_value

    def value(self):
        return self.base_value, self.const_type

    @model_serializer()
    def serialize(self) -> str:
        return repr(self)


class AxisEnum(Enum):
    X = 0
    Y = 1
    Z = 2

    @staticmethod
    def from_str(string: str):
        match string[0].lower():
            case 'x':
                return AxisEnum.X
            case 'y':
                return AxisEnum.Y
            case 'z':
                return AxisEnum.Z

        return None

    def __repr__(self):
        return f'AxisEnum.{self.name}'


class Axis(ASTNode):
    axis: AxisEnum

    def value(self):
        return self.axis

    @model_serializer()
    def serialize(self) -> str:
        return f'{self.node_name}({repr(self.axis)})'


class ArgName(NameNode):
    ...


class Keyword(Enum):
    TURN = BosParser.TURN
    AROUND = BosParser.AROUND
    MOVE = BosParser.MOVE
    ALONG = BosParser.ALONG
    TO = BosParser.TO
    FROM = BosParser.FROM
    NOW = BosParser.NOW
    SPEED = BosParser.SPEED
    SPIN = BosParser.SPIN
    ACCELERATE = BosParser.ACCELERATE
    STOP_SPIN = BosParser.STOP_SPIN
    DECELERATE = BosParser.DECELERATE
    WAIT_FOR_TURN = BosParser.WAIT_FOR_TURN
    WAIT_FOR_MOVE = BosParser.WAIT_FOR_MOVE
    SET = BosParser.SET
    GET = BosParser.GET
    CALL_SCRIPT = BosParser.CALL_SCRIPT
    START_SCRIPT = BosParser.START_SCRIPT
    EMIT_SFX = BosParser.EMIT_SFX
    SLEEP = BosParser.SLEEP
    HIDE = BosParser.HIDE
    SHOW = BosParser.SHOW
    EXPLODE = BosParser.EXPLODE
    TYPE = BosParser.TYPE
    SIGNAL = BosParser.SIGNAL
    SET_SIGNAL_MASK = BosParser.SET_SIGNAL_MASK
    ATTACH_UNIT = BosParser.ATTACH_UNIT
    DROP_UNIT = BosParser.DROP_UNIT
    RETURN = BosParser.RETURN
    CACHE = BosParser.CACHE
    DONT_CACHE = BosParser.DONT_CACHE
    DONT_SHADOW = BosParser.DONT_SHADOW
    DONT_SHADE = BosParser.DONT_SHADE
    PLAY_SOUND = BosParser.PLAY_SOUND

    def __repr__(self):
        return f'Keyword.{self.name}'


class Statement(ASTNode, ABC):
    ...


class StatementBlock(ASTNode):
    statements: list[Statement | UndefNode]

    def value(self):
        return self.statements

    def __iter__(self) -> Generator[Statement]:
        yield from (s for s in self.statements if isinstance(s, Statement))

    def __len__(self):
        return len(self.statements)

    def __getitem__(self, key):
        return self.statements[key]


class KeywordStatement(Statement):
    keyword: Keyword
    args: list[ASTNode | None]

    def value(self):
        return SimpleNamespace(keyword=self.keyword, args=self.args)


class CallStatement(KeywordStatement):
    ...


class StartStatement(KeywordStatement):
    ...


class VarStatement(Statement):
    vars: list[VarName]

    def value(self):
        return self.vars

    def __iter__(self) -> Generator[VarName]:
        yield from self.vars


class IfStatement(Statement):
    condition: Expression | ValueNode
    then_block: StatementBlock
    else_block: StatementBlock | None

    def value(self):
        return SimpleNamespace(condition=self.condition, then_block=self.then_block, else_block=self.else_block)


class WhileStatement(Statement):
    condition: Expression | ValueNode
    block: StatementBlock

    def value(self):
        return SimpleNamespace(condition=self.condition, block=self.block)


# class ForStatement(Statement):
#     initialization: Expression
#     condition: Expression
#     increment: Expression
#     block: StatementBlock
#
#     def value(self):
#         return SimpleNamespace(
#             initialization=self.initialization,
#             condition=self.condition,
#             increment=self.increment,
#             block=self.block
#         )


class AssignStatement(Statement):
    variable: VarName
    expression: Expression | ValueNode

    def value(self):
        return SimpleNamespace(variable=self.variable, expression=self.expression)


class ReturnStatement(Statement):
    expression: Expression | ValueNode | None

    def value(self):
        return SimpleNamespace(expression=self.expression)


class EmptyStatement(Statement):
    def value(self):
        return None


class FuncDeclaration(Declaration):
    name: FuncName
    args: list[ArgName]
    block: StatementBlock

    def value(self):
        return SimpleNamespace(name=self.name, args=self.args, block=self.block)


class File(ASTNode):
    declarations: list[Declaration]

    @property
    def piece_declarations(self):
        return [d for d in self.declarations if isinstance(d, PieceDeclaration)]

    @property
    def static_var_declarations(self):
        return [d for d in self.declarations if isinstance(d, StaticVarDeclaration)]

    @property
    def function_declarations(self):
        return [d for d in self.declarations if isinstance(d, FuncDeclaration)]

    def value(self):
        return SimpleNamespace(
            declarations=self.declarations
        )

    def __iter__(self) -> Generator[Declaration]:
        yield from self.declarations


class VaryingTerm(ValueNode, ABC):
    ...


class GetCall(ASTNode):
    value_idx: Expression | ValueNode
    args: list[Expression | ValueNode | None]

    def value(self) -> Any:
        if len(self.args) == 0:
            return SimpleNamespace(value_idx=self.value_idx)

        return SimpleNamespace(value_idx=self.value_idx, args=self.args)


class GetTerm(VaryingTerm):
    get_call: GetCall

    def value(self):
        return self.get_call


class RandTerm(VaryingTerm):
    min: Expression | ValueNode
    max: Expression | ValueNode

    def value(self):
        return SimpleNamespace(min=self.min, max=self.max)


class VarNameTerm(VaryingTerm):
    var_name: VarName

    def value(self):
        return self.var_name
