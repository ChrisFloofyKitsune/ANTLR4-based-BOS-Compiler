from abc import ABC
from types import SimpleNamespace
from typing import Any

from bos.ast_nodes.base_nodes import PreprocNode, ValueNode, ASTNode
from bos.ast_nodes.enums import ExpressionOp
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

    def get_value(self) -> Any:
        return SimpleNamespace(
            filepath=self.path
        )

class PreprocDefine(PreprocNode):
    name: DefineName
    value: PreprocArg | None

    def get_value(self) -> Any:
        return SimpleNamespace(
            name=self.name,
            value=self.value
        )

    def __repr__(self):
        return f'{self.node_name}({self.name}, {repr(self.value)})'

class PreprocFunctionDefine(PreprocNode):
    name: DefineName
    parameters: list[NameNode]
    value: PreprocArg | None

    def get_value(self) -> Any:
        return SimpleNamespace(
            name=self.name,
            parameters=self.parameters,
            value=self.value
        )

    def __repr__(self):
        return f'{self.node_name}({self.name}, {self.parameters}, {repr(self.value)})'

class PreprocUndef(PreprocNode):
    name: DefineName

    def get_value(self) -> Any:
        return SimpleNamespace(
            name=self.name
        )

    def __repr__(self):
        return f'{self.node_name}({self.name})'

class PreprocDirective(PreprocNode):
    directive: NameNode
    argument: PreprocArg | None

    def get_value(self) -> Any:
        return SimpleNamespace(
            directive=self.directive,
            argument=self.argument
        )

    def __repr__(self):
        return f'{self.node_name}({self.directive} {repr(self.argument)})'

class PreprocExpression(PreprocValue, ABC):
    ...

class PreprocCallExpression(PreprocExpression):
    function: DefineName
    arguments: list[PreprocValue | Constant]

    def get_value(self) -> Any:
        return SimpleNamespace(
            function=self.function,
            arguments=self.arguments
        )

class PreprocUnaryExpression(PreprocExpression):
    operator: ExpressionOp
    operand: PreprocValue | Constant

    def get_value(self) -> Any:
        return SimpleNamespace(
            operator=self.operator,
            operand=self.operand
        )

class PreprocBinaryExpression(PreprocExpression):
    left: PreprocValue | Constant
    operator: ExpressionOp
    right: PreprocValue | Constant

    def get_value(self) -> Any:
        return SimpleNamespace(
            left=self.left,
            operator=self.operator,
            right=self.right
        )

class PreprocDefinedTerm(PreprocExpression):
    name: DefineName

    def get_value(self) -> Any:
        return SimpleNamespace(
            name=self.name
        )

class PreprocIf(PreprocNode):
    condition: PreprocValue | Constant
    body: list[ASTNode]
    alternative: list[ASTNode] | None

    def get_value(self) -> Any:
        return SimpleNamespace(
            condition=self.condition,
            body=self.body,
            alternative=self.alternative
        )

class PreprocLine(PreprocNode):
    lineno: int
    filename: str

    def get_value(self) -> Any:
        return SimpleNamespace(
            lineno=self.lineno,
            filename=self.filename
        )

    def __repr__(self):
        return f'{self.node_name}({self.lineno} {repr(self.filename)})'