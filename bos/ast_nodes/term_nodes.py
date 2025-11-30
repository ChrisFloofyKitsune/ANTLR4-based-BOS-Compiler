import contextlib
from abc import ABC
from types import SimpleNamespace
from typing import ClassVar, Literal, Any

from pydantic import model_serializer

from bos.ast_nodes.name_nodes import VarName
from bos.ast_nodes.base_nodes import ValueNode
from bos.ast_nodes.enums import AxisEnum
from code_error import CodeError
from code_location import CodeLocation


class Constant(ValueNode):
    LINEAR_SCALE: ClassVar[int] = 65536
    ANGULAR_SCALE: ClassVar[int] = 182

    base_value: int | float | str
    const_type: Literal['normal', 'angular', 'linear'] = 'normal'

    def __init__(
            self,
            /,
            value: float | int | str,
            *,
            const_type: Literal['normal', 'angular', 'linear'] = None,
            **kwargs
    ):
        if isinstance(value, str):
            if const_type is None:
                if value[0] == '[' and value[-1] == ']':
                    const_type = 'linear'
                elif value[0] == '<' and value[-1] == '>':
                    const_type = 'angular'
                else:
                    const_type = 'normal'

            value = value.strip('()[]<>')
            with contextlib.suppress(ValueError):
                if '.' in value:
                    value = float(value)
                elif value.startswith('0x'):
                    value = int(value, base=16)
                else:
                    value = int(value)

        elif const_type is None:
            const_type = 'normal'
        super().__init__(**kwargs, base_value=value, const_type=const_type)

    def __repr__(self):
        if self.const_type == 'normal':
            return f'Constant({self.base_value})'
        if self.const_type == 'angular':
            return f'Constant(\'<{self.base_value}> degrees\')'
        if self.const_type == 'linear':
            return f'Constant(\'[{self.base_value}] units\')'

    def number_value(self) -> int | float:
        if isinstance(self.base_value, str):
            raise CodeError(
                f'Error compiling constant {self.model_dump()}. '
                f'Likely an un-replaced macro? (value: {self.base_value})',
                CodeLocation.from_node(self.parser_node)
            )

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
                f'Computed value (int_value) cannot fit inside 32 bits',
                CodeLocation.from_node(self.parser_node)
            )

        # In order to preserve the bits of the value, we need to convert
        # what would be unsigned ints into their signed int equivalents
        if int_value > 0x7FFF_FFFF:
            int_value -= 0x1_0000_0000
            if isinstance(self.base_value, float):
                print(
                    f'[WARNING] Converted float from {self.model_dump()} (computed: {number_value}) to very large negative int {int_value}',
                    CodeLocation.from_node(self.parser_node)
                )

        return int_value

    def get_value(self):
        return self.base_value, self.const_type

    @model_serializer()
    def serialize(self) -> str:
        return repr(self)


class VaryingTerm(ValueNode, ABC):
    ...


class GetTerm(VaryingTerm):
    get_call: 'GetCall'

    def get_value(self):
        return self.get_call


class GetCall(ValueNode):
    value_idx: ValueNode
    args: list[ValueNode | None]

    def get_value(self) -> Any:
        args = [a for a in self.args if a]
        if len(args) == 0:
            return SimpleNamespace(value_idx=self.value_idx)

        return SimpleNamespace(value_idx=self.value_idx, args=args)

class VarNameTerm(VaryingTerm):
    var_name: VarName

    def get_value(self):
        return self.var_name

    @model_serializer()
    def serialize(self) -> str:
        return f'{self.node_name}({repr(self.var_name)})'

class RandTerm(VaryingTerm):
    min: ValueNode
    max: ValueNode

    def get_value(self):
        return SimpleNamespace(min=self.min, max=self.max)


class Axis(ValueNode):
    axis: AxisEnum

    def get_value(self):
        return self.axis

    @model_serializer()
    def serialize(self) -> str:
        return f'{self.node_name}({repr(self.axis)})'


class StringLiteral(ValueNode):
    string: str

    def get_value(self):
        return self.string

    @model_serializer()
    def serialize(self) -> str:
        return f'{self.node_name}({repr(self.string)})'
