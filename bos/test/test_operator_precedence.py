import unittest
from numbers import Number

import antlr4
from antlr4 import ParserRuleContext

from bos.gen.BosLexer import BosLexer
from bos.gen.BosParser import BosParser
from bos.gen.BosParserVisitor import BosParserVisitor


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
            'Mult before Add': ('1 * 2 + 3', 6),
            'Parens before Mult': ('(1 + 2) * 3)', 9),
        }

        for test_name, (input_str, expected) in TEST_PARAMS.items():
            with self.subTest(test_name):
                print(test_name)
                expr = self.set_up_parser(input_str).expression()
                visitor = CalculatorVisitor()
                result = visitor.visitExpression(expr)
                print('=', result)

                text_repr: str = expr.toStringTree(recog=self.parser)

                print(text_repr)


class CalculatorVisitor(BosParserVisitor):
    def visitExpression(self, ctx: BosParser.ExpressionContext):
        if ctx.op is None:
            inner_expr = ctx.expression(0)
            if inner_expr is not None:
                return self.visit(inner_expr)
            return self.visitChildren(ctx)

        if ctx.operand1 is None:
            match ctx.op.type:
                case BosParser.OP_MINUS:
                    return -self.visit(ctx.operand0)
                case BosParser.LOGICAL_NOT:
                    return not self.visit(ctx.operand0)
                case _:
                    return 0

        match ctx.op.type:
            case BosParser.OP_MULT:
                return self.visit(ctx.operand0) * self.visit(ctx.operand1)
            case BosParser.OP_DIV:
                return self.visit(ctx.operand0) / self.visit(ctx.operand1)
            case BosParser.OP_MOD:
                return self.visit(ctx.operand0) % self.visit(ctx.operand1)
            case BosParser.OP_ADD:
                return self.visit(ctx.operand0) + self.visit(ctx.operand1)
            case BosParser.OP_MINUS:
                return self.visit(ctx.operand0) - self.visit(ctx.operand1)

            case BosParser.COMP_LESS:
                return self.visit(ctx.operand0) < self.visit(ctx.operand1)
            case BosParser.COMP_LESS_EQUAL:
                return self.visit(ctx.operand0) <= self.visit(ctx.operand1)
            case BosParser.COMP_GREATER:
                return self.visit(ctx.operand0) > self.visit(ctx.operand1)
            case BosParser.COMP_GREATER_EQUAL:
                return self.visit(ctx.operand0) >= self.visit(ctx.operand1)
            case BosParser.COMP_EQUAL:
                return self.visit(ctx.operand0) == self.visit(ctx.operand1)
            case BosParser.COMP_NOT_EQUAL:
                return self.visit(ctx.operand0) != self.visit(ctx.operand1)

            case BosParser.BITWISE_AND:
                return int(self.visit(ctx.operand0)) & int(self.visit(ctx.operand1))
            case BosParser.BITWISE_OR:
                return int(self.visit(ctx.operand0)) | int(self.visit(ctx.operand1))
            case BosParser.BITWISE_XOR:
                return int(self.visit(ctx.operand0)) ^ int(self.visit(ctx.operand1))

            case BosParser.LOGICAL_AND:
                return bool(self.visit(ctx.operand0)) and bool(self.visit(ctx.operand1))
            case BosParser.LOGICAL_OR:
                return bool(self.visit(ctx.operand0)) or bool(self.visit(ctx.operand1))
            case BosParser.LOGICAL_XOR:
                return bool(self.visit(ctx.operand0)) ^ bool(self.visit(ctx.operand1))
            case _:
                return 0

    def visitConstant(self, ctx: BosParser.ConstantContext):
        print(ctx.getText())
        return int(ctx.getText())


if __name__ == '__main__':
    unittest.main()
