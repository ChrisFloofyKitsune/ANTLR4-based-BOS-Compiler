import math
import operator
import unittest
from numbers import Number

import antlr4
from antlr4 import ParserRuleContext

from bos.gen.BosLexer import BosLexer
from bos.gen.BosParser import BosParser
from bos.gen.BosParserVisitor import BosParserVisitor


UNARY_OP_FUNC_MAPPING = {
    BosParser.OP_MINUS: operator.neg,
    BosParser.LOGICAL_NOT: operator.not_
}
UNARY_OP_FUNC_MAPPING.setdefault(lambda *args: 0)

BINARY_OP_FUNC_MAPPING = {
    BosParser.OP_MULT: operator.mul,
    BosParser.OP_DIV: operator.truediv,
    BosParser.OP_MOD: operator.mod,
    BosParser.OP_ADD: operator.add,
    BosParser.OP_MINUS: operator.sub,
    BosParser.COMP_LESS: operator.lt,
    BosParser.COMP_LESS_EQUAL: operator.le,
    BosParser.COMP_GREATER: operator.gt,
    BosParser.COMP_GREATER_EQUAL: operator.ge,
    BosParser.COMP_EQUAL: operator.eq,
    BosParser.COMP_NOT_EQUAL: operator.ne,
    BosParser.BITWISE_AND: operator.and_,
    BosParser.BITWISE_OR: operator.or_,
    BosParser.BITWISE_XOR: operator.xor,
    BosParser.LOGICAL_AND: operator.and_,
    BosParser.LOGICAL_OR: operator.or_,
    BosParser.LOGICAL_XOR: operator.xor
}
BINARY_OP_FUNC_MAPPING.setdefault(lambda *args: 0)

COB_LINEAR_SCALE = 65536
COB_ANGULAR_SCALE = COB_LINEAR_SCALE / 2.0 / math.pi

class TestOperatorPrecedence(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_stream: antlr4.InputStream
        self.lexer: BosLexer
        self.token_stream: antlr4.CommonTokenStream
        self.parser: BosParser

    def set_up_parser(self, input_string: str):
        self.input_stream = antlr4.InputStream(input_string)
        self.lexer = BosLexer(self.input_stream)
        self.token_stream = antlr4.CommonTokenStream(self.lexer)
        self.parser = BosParser(self.token_stream)

        return self.parser

    def recursive_print_tree(self, ctx: ParserRuleContext, depth=0):
        padding = ' ' * (depth * 4)
        is_terminal_node = not (hasattr(ctx, 'children') and ctx.children is not None)

        if is_terminal_node:
            print(f'{padding}{ctx.getText()} //{ctx.__class__.__name__}')
            return

        print(f'{padding}( //enter {ctx.__class__.__name__}')
        for child_ctx in ctx.children:
            child_ctx: ParserRuleContext
            self.recursive_print_tree(child_ctx, depth + 1)
        print(f'{padding}) //exit {ctx.__class__.__name__}')

    def test_basic_maths(self):
        TEST_PARAMS: dict[str, tuple[str, Number]] = {
            'Add before Mult': ('1 + 2 * 3', 7),
            'Mult before Add': ('1 * 2 + 3', 5),
            'Parens before Mult': ('(1 + 2) * 3)', 9),
        }

        for test_name, (input_str, expected) in TEST_PARAMS.items():
            with self.subTest(test_name):
                print(test_name)
                expr = self.set_up_parser(input_str).expression()
                visitor = CalculatorVisitor()
                result = visitor.visit(expr)
                self.assertEqual(result, expected)

class CalculatorVisitor(BosParserVisitor):
    def visitParenExpr(self, ctx: BosParser.ParenExprContext):
        return self.visit(ctx.expression())

    def visitUnaryExpr(self, ctx: BosParser.UnaryExprContext):
        return UNARY_OP_FUNC_MAPPING[ctx.op.type](self.visit(ctx.operand))

    def visitBinaryExpr(self, ctx: BosParser.BinaryExprContext):
        return BINARY_OP_FUNC_MAPPING[ctx.op.type](self.visit(ctx.operand1), self.visit(ctx.operand2))

    def visitConstant(self, ctx: BosParser.ConstantContext):
        text: str = ctx.getText()
        return float(text.strip('[]<>'))


if __name__ == '__main__':
    unittest.main()
