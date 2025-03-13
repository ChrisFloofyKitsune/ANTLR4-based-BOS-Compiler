from abc import ABC
from types import SimpleNamespace

from bos.ast_nodes.base_nodes import ValueNode
from bos.ast_nodes.enums import ExpressionOp


class Expression(ValueNode, ABC):
    ...


class UnaryExpression(Expression):
    op: ExpressionOp
    operand: ValueNode

    def get_value(self):
        return SimpleNamespace(op=self.op, operand=self.operand)


class BinaryExpression(Expression):
    operand1: ValueNode
    op: ExpressionOp
    operand2: ValueNode

    def get_value(self):
        return SimpleNamespace(operand1=self.operand1, op=self.op, operand2=self.operand2)


