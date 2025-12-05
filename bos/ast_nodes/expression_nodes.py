from abc import ABC
from types import SimpleNamespace

from bos.ast_nodes.base_nodes import ValueNode
from bos.ast_nodes.enums import ExpressionOperator
from bos.ast_nodes.preproc_nodes import PreprocCallExpression


class Expression(ValueNode, ABC):
    ...


class UnaryExpression(Expression):
    op: ExpressionOperator
    operand: ValueNode


class BinaryExpression(Expression):
    left: ValueNode
    op: ExpressionOperator
    right: ValueNode

class MacroCallExpression(PreprocCallExpression, Expression):
    ...
