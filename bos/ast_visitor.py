import json
import operator
from types import SimpleNamespace

from antlr4.ParserRuleContext import ParserRuleContext

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

    KEYWORD_MAPPING = {
        BosParser.CALL_SCRIPT: nodes.Keyword.CALL_SCRIPT,
        BosParser.START_SCRIPT: nodes.Keyword.START_SCRIPT,

        BosParser.SIGNAL: nodes.Keyword.SIGNAL,
        BosParser.SET_SIGNAL_MASK: nodes.Keyword.SET_SIGNAL_MASK,

        BosParser.SLEEP: nodes.Keyword.SLEEP,

        BosParser.SET: nodes.Keyword.SET,
        BosParser.GET: nodes.Keyword.GET,

        BosParser.SPIN: nodes.Keyword.SPIN,
        BosParser.STOP_SPIN: nodes.Keyword.STOP_SPIN,

        BosParser.TURN: nodes.Keyword.TURN,
        BosParser.MOVE: nodes.Keyword.MOVE,

        BosParser.WAIT_FOR_TURN: nodes.Keyword.WAIT_FOR_TURN,
        BosParser.WAIT_FOR_MOVE: nodes.Keyword.WAIT_FOR_MOVE,

        BosParser.HIDE: nodes.Keyword.HIDE,
        BosParser.SHOW: nodes.Keyword.SHOW,

        BosParser.EMIT_SFX: nodes.Keyword.EMIT_SFX,
        BosParser.EXPLODE: nodes.Keyword.EXPLODE,

        BosParser.ATTACH_UNIT: nodes.Keyword.ATTACH_UNIT,
        BosParser.DROP_UNIT: nodes.Keyword.DROP_UNIT,

        # effectively removed from the language, these do nothing
        BosParser.CACHE: nodes.Keyword.CACHE,
        BosParser.DONT_CACHE: nodes.Keyword.DONT_CACHE,
        BosParser.DONT_SHADOW: nodes.Keyword.DONT_SHADE,
        BosParser.DONT_SHADE: nodes.Keyword.DONT_SHADE,
    }

    OPERATOR_MAPPING = {
        BosParser.OP_ADD: nodes.ExpressionOp.ADD,
        BosParser.OP_MINUS: nodes.ExpressionOp.MINUS,
        BosParser.OP_MULT: nodes.ExpressionOp.MULT,
        BosParser.OP_DIV: nodes.ExpressionOp.DIV,
        BosParser.OP_MOD: nodes.ExpressionOp.MOD,
        BosParser.LOGICAL_XOR: nodes.ExpressionOp.LOGICAL_XOR,
        BosParser.LOGICAL_OR: nodes.ExpressionOp.LOGICAL_OR,
        BosParser.LOGICAL_AND: nodes.ExpressionOp.LOGICAL_AND,
        BosParser.LOGICAL_NOT: nodes.ExpressionOp.LOGICAL_NOT,
        BosParser.BITWISE_XOR: nodes.ExpressionOp.BITWISE_XOR,
        BosParser.BITWISE_OR: nodes.ExpressionOp.BITWISE_OR,
        BosParser.BITWISE_AND: nodes.ExpressionOp.BITWISE_AND,
        BosParser.COMP_EQUAL: nodes.ExpressionOp.COMP_EQUAL,
        BosParser.COMP_NOT_EQUAL: nodes.ExpressionOp.COMP_NOT_EQUAL,
        BosParser.COMP_GREATER: nodes.ExpressionOp.COMP_GREATER,
        BosParser.COMP_GREATER_EQUAL: nodes.ExpressionOp.COMP_GREATER_EQUAL,
        BosParser.COMP_LESS_EQUAL: nodes.ExpressionOp.COMP_LESS_EQUAL,
        BosParser.COMP_LESS: nodes.ExpressionOp.COMP_LESS,
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

    def visitChildren(self, node: ParserRuleContext):
        result = super().visitChildren(node)
        if isinstance(result, nodes.ASTNode):
            return result
        if result is None:
            return None

        name = node.__class__.__name__.removesuffix('Context')

        return nodes.UndefNode(contents=result, name=name, parser_node=node)

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
        op = self.OPERATOR_MAPPING.get(ctx.op.type, None)
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
        op = self.OPERATOR_MAPPING.get(ctx.op.type, None)
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
            left=operand1,
            op=op,
            right=operand2,
            parser_node=ctx
        )

    def visitExpressionList(self, ctx: BosParser.ExpressionListContext):
        return [
            self.visit(ctx.getChild(0)),
            *self.visitTypedChildren(ctx, BosParser.CommaExpressionContext)
        ]

    def visitStatementBlock(self, ctx: BosParser.StatementBlockContext):
        return nodes.StatementBlock(
            block_level_nodes=[c for c in self.visitTypedChildren(ctx, BosParser.StatementContext) if c],
            parser_node=ctx
        )

    def visitKeywordStatementInner(self, ctx: ParserRuleContext):
        keyword = self.KEYWORD_MAPPING.get(getattr(ctx, 'kw').type, None)
        args = self._extract_args(ctx)

        if (expr_list_ctx := ctx.getChild(0, BosParser.ExpressionListContext)) is not None:
            args.extend(self.visit(expr_list_ctx))

        statement_class = nodes.KeywordStatement
        if keyword == nodes.Keyword.CALL_SCRIPT:
            statement_class = nodes.CallScriptStatement
        elif keyword == nodes.Keyword.START_SCRIPT:
            statement_class = nodes.StartScriptStatement

        # noinspection PyArgumentList
        return statement_class(
            keyword=keyword,
            args=args,
            parser_node=ctx
        )

    def _extract_args(self, ctx):
        args = []
        for attr in dir(ctx):
            if attr.startswith('arg'):
                arg_ctx = getattr(ctx, attr)
                args.append(self.visit(arg_ctx) if arg_ctx is not None else None)
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
                    left=nodes.VarNameTerm(var_name=var_name),
                    op=nodes.ExpressionOp.ADD,
                    right=nodes.Constant(value=1)
                ),
                parser_node=inc_ctx
            )

        dec_ctx: BosParser.DecStatementContext = ctx.decStatement()
        if dec_ctx is not None:
            var_name = self.visit(dec_ctx.varName())
            return nodes.AssignStatement(
                variable=self.visit(var_name),
                expression=nodes.BinaryExpression(
                    left=nodes.VarNameTerm(var_name=var_name),
                    op=nodes.ExpressionOp.MINUS,
                    right=nodes.Constant(value=1)
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
        return None

    def visitFile(self, ctx: BosParser.FileContext):
        return nodes.File(
            top_level_nodes=self.visitTypedChildren(ctx, BosParser.DeclarationContext),
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
        'preprocessed/armcroc.preprocessed.bos',
        enable_constant_folding=False
    )
    print(loader.load_file().model_dump_json(indent=2))

    # loader = BosLoader(
    #     'preprocessed/armaak_clean.preprocessed.bos',
    #     enable_constant_folding=False
    # )
    # print(loader.load_file())


if __name__ == '__main__':
    main()
