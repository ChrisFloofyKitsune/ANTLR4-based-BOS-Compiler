import json
import operator
from antlr4.ParserRuleContext import ParserRuleContext
from types import SimpleNamespace

import bos.ast_nodes as nodes
from bos.gen.BosParser import BosParser
from bos.gen.BosParserVisitor import BosParserVisitor


class ASTVisitor(BosParserVisitor):

    UNARY_OP_FUNC_MAPPING = {
        nodes.ExpressionOp.LOGICAL_NOT: lambda a: int(not bool(a))
    }

    BINARY_OP_FUNC_MAPPING = {
        nodes.ExpressionOp.MULT: operator.mul,
        nodes.ExpressionOp.DIV: operator.truediv,
        nodes.ExpressionOp.MOD: operator.mod,
        nodes.ExpressionOp.ADD: operator.add,
        nodes.ExpressionOp.MINUS: operator.sub,

        nodes.ExpressionOp.COMP_LESS: lambda a, b: int(a < b),
        nodes.ExpressionOp.COMP_LESS_EQUAL: lambda a, b: int(a <= b),
        nodes.ExpressionOp.COMP_GREATER: lambda a, b: int(a > b),
        nodes.ExpressionOp.COMP_GREATER_EQUAL: lambda a, b: int(a >= b),
        nodes.ExpressionOp.COMP_EQUAL: lambda a, b: int(a == b),
        nodes.ExpressionOp.COMP_NOT_EQUAL: lambda a, b: int(a != b),

        nodes.ExpressionOp.BITWISE_AND: lambda a, b: int(a) & int(b),
        nodes.ExpressionOp.BITWISE_OR: lambda a, b: int(a) | int(b),
        nodes.ExpressionOp.BITWISE_XOR: lambda a, b: int(a) ^ int(b),

        nodes.ExpressionOp.LOGICAL_AND: lambda a, b: int(bool(a) and bool(b)),
        nodes.ExpressionOp.LOGICAL_OR: lambda a, b: int(bool(a) or bool(b)),
        nodes.ExpressionOp.LOGICAL_XOR: lambda a, b: int(bool(a) ^ bool(b))
    }

    def __init__(self, *args, enable_constant_folding=False, **kwargs):
        self.enable_constant_folding = enable_constant_folding
        super().__init__(*args, **kwargs)

    def aggregateResult(self, aggregate, next_result):
        if next_result is None:
            return aggregate

        if aggregate is None:
            return next_result

        if not isinstance(aggregate, list):
            return [aggregate, next_result]

        return [*aggregate, next_result]

    def visitChildren(self, node):
        result = super().visitChildren(node)
        if isinstance(result, nodes.ASTNode):
            return result
        return nodes.UndefNode(contents=result, parser_node=node)

    def visitTypedChildren(self, node: ParserRuleContext, child_type: type[ParserRuleContext]):
        result = []
        for child in node.getTypedRuleContexts(child_type):
            result.append(self.visit(child))
        return result

    def visitPieceName(self, ctx: BosParser.PieceNameContext):
        return nodes.PieceName(name=ctx.getText(), parser_node=ctx)

    def visitPieceDecl(self, ctx: BosParser.PieceDeclContext):
        return nodes.PieceDeclaration(names=self.visitTypedChildren(ctx, BosParser.PieceNameContext), parser_node=ctx)

    def visitVarName(self, ctx: BosParser.VarNameContext):
        return nodes.VarName(name=ctx.getText(), parser_node=ctx)

    def visitStaticVarDecl(self, ctx: BosParser.StaticVarDeclContext):
        return nodes.StaticVarDeclaration(names=self.visitTypedChildren(ctx, BosParser.VarNameContext), parser_node=ctx)

    def visitFuncName(self, ctx: BosParser.FuncNameContext):
        return nodes.FuncName(name=ctx.getText(), parser_node=ctx)

    def visitFuncDecl(self, ctx: BosParser.FuncDeclContext):
        return nodes.FuncDeclaration(
            name=self.visit(ctx.funcName()),
            args=self.visitTypedChildren(ctx, BosParser.ArgNameContext),
            block=self.visit(ctx.statementBlock()),
            parser_node=ctx
        )

    def visitConstant(self, ctx: BosParser.ConstantContext):
        return nodes.Constant(value=ctx.getText(), parser_node=ctx)

    def visitAxis(self, ctx: BosParser.AxisContext):
        return nodes.Axis(axis=nodes.AxisEnum.from_str(ctx.getText()), parser_node=ctx)

    def visitArgName(self, ctx: BosParser.ArgNameContext):
        return nodes.ArgName(name=ctx.getText(), parser_node=ctx)

    def visitUnaryExpr(self, ctx: BosParser.UnaryExprContext):
        op = nodes.ExpressionOp(ctx.op.type)
        operand = self.visit(ctx.operand)

        if self.enable_constant_folding and isinstance(operand, nodes.Constant):
            return nodes.Constant(
                value=self.UNARY_OP_FUNC_MAPPING[op](operand.number_value()),
                parser_node=ctx
            )

        return nodes.UnaryExpression(
            op=op,
            operand=operand,
            parser_node=ctx
        )

    def visitBinaryExpr(self, ctx: BosParser.BinaryExprContext):
        op = nodes.ExpressionOp(ctx.op.type)
        operand1 = self.visit(ctx.operand1)
        operand2 = self.visit(ctx.operand2)

        if (
            self.enable_constant_folding
            and isinstance(operand1, nodes.Constant)
            and isinstance(operand2, nodes.Constant)
        ):
            return nodes.Constant(
                value=self.BINARY_OP_FUNC_MAPPING[op](
                    operand1.number_value(),
                    operand2.number_value()
                ),
                parser_node=ctx
            )

        return nodes.BinaryExpression(
            operand1=operand1,
            op=op,
            operand2=operand2,
            parser_node=ctx
        )

    def visitExpressionList(self, ctx: BosParser.ExpressionListContext):
        return [
            self.visit(ctx.getChild(0)),
            *self.visitTypedChildren(ctx, BosParser.CommaExpressionContext)
        ]

    def visitStatementBlock(self, ctx: BosParser.StatementBlockContext):
        return nodes.StatementBlock(
            statements=self.visitTypedChildren(ctx, BosParser.StatementContext),
            parser_node=ctx
        )

    def visitKeywordStatementInner(self, ctx: ParserRuleContext):
        keyword = nodes.Keyword(getattr(ctx, 'kw').type)
        args = self._extract_args(ctx)

        if (expr_list_ctx := ctx.getChild(0, BosParser.ExpressionListContext)) is not None:
            args.extend(self.visit(expr_list_ctx))

        statement_class = nodes.KeywordStatement
        if keyword == nodes.Keyword.CALL_SCRIPT:
            statement_class = nodes.CallStatement
        elif keyword == nodes.Keyword.START_SCRIPT:
            statement_class = nodes.StartStatement

        # noinspection PyArgumentList
        return statement_class(
            keyword=keyword,
            args=args,
            parser_node=ctx
        )

    def _extract_args(self, ctx):
        args = []
        for attr in dir(ctx):
            if attr.startswith('arg') and (arg_ctx := getattr(ctx, attr, None)) is not None:
                args.append(self.visit(arg_ctx))
        return args

    def visitKeywordStatement(self, ctx: BosParser.KeywordStatementContext):
        return self.visitKeywordStatementInner(ctx.getChild(0, ParserRuleContext))

    def visitVarStatement(self, ctx: BosParser.VarStatementContext):
        return nodes.VarStatement(
            vars=self.visitTypedChildren(ctx, BosParser.VarNameContext),
            parser_node=ctx
        )

    def visitIfStatement(self, ctx: BosParser.IfStatementContext):
        else_ctx: BosParser.ElseBlockContext = ctx.elseBlock()
        return nodes.IfStatement(
            condition=self.visit(ctx.expression()),
            then_block=self.visit(ctx.statementBlock()),
            else_block=self.visit(else_ctx.statementBlock()) if else_ctx is not None else None,
            parser_node=ctx
        )

    def visitWhileStatement(self, ctx: BosParser.WhileStatementContext):
        return nodes.WhileStatement(
            condition=self.visit(ctx.expression()),
            block=self.visit(ctx.statementBlock()),
            parser_node=ctx
        )

    # def visitForStatement(self, ctx: BosParser.ForStatementContext):
    #     return nodes.ForStatement(
    #         initialization=self.visit(ctx.expression(0)),
    #         condition=self.visit(ctx.expression(1)),
    #         increment=self.visit(ctx.expression(2)),
    #         block=self.visit(ctx.statementBlock()),
    #         parser_node=ctx
    #     )

    def visitAssignStatement(self, ctx: BosParser.AssignStatementContext):
        inc_ctx: BosParser.IncStatementContext = ctx.incStatement()
        if inc_ctx is not None:
            var_name = self.visit(inc_ctx.varName())
            return nodes.AssignStatement(
                variable=var_name,
                expression=nodes.BinaryExpression(
                    operand1=nodes.VarNameTerm(var_name=var_name),
                    op=nodes.ExpressionOp.ADD,
                    operand2=nodes.Constant(value=1)
                ),
                parser_node=inc_ctx
            )

        dec_ctx: BosParser.DecStatementContext = ctx.decStatement()
        if dec_ctx is not None:
            var_name = self.visit(dec_ctx.varName())
            return nodes.AssignStatement(
                variable=self.visit(var_name),
                expression=nodes.BinaryExpression(
                    operand1=var_name,
                    op=nodes.ExpressionOp.SUB,
                    operand2=nodes.Constant(value=1)
                ),
                parser_node=dec_ctx
            )

        return nodes.AssignStatement(
            variable=self.visit(ctx.varName()),
            expression=self.visit(ctx.expression()),
            parser_node=ctx
        )

    def visitReturnStatement(self, ctx: BosParser.ReturnStatementContext):
        return nodes.ReturnStatement(
            expression=self.visit(ctx.expression()) if ctx.expression() is not None else None,
            parser_node=ctx
        )

    def visitEmptyStatement(self, ctx: BosParser.EmptyStatementContext):
        return nodes.EmptyStatement(parser_node=ctx)

    def visitFile(self, ctx: BosParser.FileContext):
        return nodes.File(
            declarations=self.visitTypedChildren(ctx, BosParser.DeclarationContext),
            parser_node=ctx
        )

    def visitSpeedOrNow(self, ctx: BosParser.SpeedOrNowContext):
        if expr := ctx.expression():
            return self.visit(expr)
        return None

    def visitGetTerm(self, ctx: BosParser.GetTermContext):
        return nodes.GetTerm(
            get_call=self.visit(ctx.getCall()),
            parser_node=ctx
        )

    def visitRandTerm(self, ctx: BosParser.RandTermContext):
        return nodes.RandTerm(
            min=self.visit(ctx.expression(0)),
            max=self.visit(ctx.expression(1)),
            parser_node=ctx
        )

    def visitVarNameTerm(self, ctx: BosParser.VarNameTermContext):
        return nodes.VarNameTerm(
            var_name=self.visit(ctx.varName()),
            parser_node=ctx
        )

    def visitGetCall(self, ctx: BosParser.GetCallContext):
        return nodes.GetCall(
            value_idx=self.visit(ctx.value_idx),
            args=self._extract_args(ctx),
            parser_node=ctx
        )


def main():
    from bos_loader import BosLoader
    loader = BosLoader(
        'example_files/Units/armestor_clean.bos',
        enable_constant_folding=True
    )
    loader.load_file()

    ast: nodes.File = loader.ast_node_tree
    print(
        json.dumps(
            ast.function_declarations[-1].block[-2].model_dump(),
            # indent=2,
            default=lambda x: vars(x) if isinstance(x, SimpleNamespace) else repr(x)
        )
    )

    loader = BosLoader(
        'example_files/Units/armestor.bos',
        enable_constant_folding=False
    )
    loader.load_file()

    ast: nodes.File = loader.ast_node_tree
    print(
        json.dumps(
            ast.function_declarations[-1].block[-2].model_dump(),
            # indent=2,
            default=lambda x: vars(x) if isinstance(x, SimpleNamespace) else repr(x)
        )
    )


if __name__ == '__main__':
    main()
