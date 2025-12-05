from abc import ABC

from bos.ast_nodes.base_nodes import PreprocNode, ASTNode
from bos.ast_nodes.enums import ExpressionOperator
from bos.ast_nodes.name_nodes import NameNode
from bos.ast_nodes.term_nodes import Constant, StringLiteral


class PreprocValue(PreprocNode, ABC):
    ...


class DefineName(NameNode, PreprocValue):
    ...


class SystemLibString(PreprocNode, StringLiteral):
    def __repr__(self):
        return f'{self.node_name}(<{self.string}>)'


class PreprocArg(PreprocNode, StringLiteral):
    def __repr__(self):
        return f'{self.node_name}({repr(self.string)})'


class PreprocInclude(PreprocNode):
    path: PreprocValue | StringLiteral


class PreprocDefine(PreprocNode):
    name: DefineName
    value: PreprocArg | None

    def __repr__(self):
        return f'{self.node_name}({self.name}, {repr(self.value)})'


class PreprocFunctionDefine(PreprocNode):
    name: DefineName
    parameters: list[NameNode]
    value: PreprocArg | None

    def __repr__(self):
        return f'{self.node_name}({self.name}, {self.parameters}, {repr(self.value)})'


class PreprocUndef(PreprocNode):
    name: DefineName

    def __repr__(self):
        return f'{self.node_name}({self.name})'


class PreprocDirective(PreprocNode):
    directive: NameNode
    argument: PreprocArg | None

    def __repr__(self):
        return f'{self.node_name}({self.directive} {repr(self.argument)})'


class PreprocExpression(PreprocValue, ABC):
    ...


class PreprocCallExpression(PreprocExpression):
    function: DefineName
    arguments: list[PreprocValue | Constant]


class PreprocUnaryExpression(PreprocExpression):
    operator: ExpressionOperator
    operand: PreprocValue | Constant


class PreprocBinaryExpression(PreprocExpression):
    left: PreprocValue | Constant
    operator: ExpressionOperator
    right: PreprocValue | Constant


class PreprocDefinedTerm(PreprocExpression):
    name: DefineName


class PreprocIf(PreprocNode):
    condition: PreprocValue | Constant
    body: list[ASTNode]
    alternative: list[ASTNode] | None


class PreprocLine(PreprocNode):
    lineno: int
    filename: str

    def __repr__(self):
        return f'{self.node_name}({self.lineno} {repr(self.filename)})'
