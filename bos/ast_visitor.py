import itertools
import json
from collections import defaultdict
from types import SimpleNamespace
from typing import Protocol

from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream
from antlr4.ParserRuleContext import ParserRuleContext

import bos.nodes as nodes
from bos.nodes import PieceDeclaration, StaticVarDeclaration, FuncDeclaration
from bos.gen.BosLexer import BosLexer
from bos.gen.BosParser import BosParser
from bos.gen.BosParserVisitor import BosParserVisitor


class ASTVisitor(BosParserVisitor):

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
        return nodes.UnaryExpression(
            op=nodes.ExpressionOp(ctx.op.type),
            operand=self.visit(ctx.operand),
            parser_node=ctx
        )

    def visitBinaryExpr(self, ctx: BosParser.BinaryExprContext):
        return nodes.BinaryExpression(
            operand1=self.visit(ctx.operand1),
            op=nodes.ExpressionOp(ctx.op.type),
            operand2=self.visit(ctx.operand2),
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
        args = []
        for attr in dir(ctx):
            if attr.startswith('arg') and (arg_ctx := getattr(ctx, attr)) is not None:
                args.append(self.visit(arg_ctx))

        if expr_list_ctx := ctx.getChild(0, BosParser.ExpressionListContext):
            args.extend(self.visit(expr_list_ctx))

        return nodes.KeywordStatement(
            keyword=keyword,
            args=args,
            parser_node=ctx
        )
    
    
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

    def visitForStatement(self, ctx: BosParser.ForStatementContext):
        return nodes.ForStatement(
            initialization=self.visit(ctx.expression(0)),
            condition=self.visit(ctx.expression(1)),
            increment=self.visit(ctx.expression(2)),
            block=self.visit(ctx.statementBlock()),
            parser_node=ctx
        )

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

    def visitFile(self, ctx: BosParser.FileContext):

        child_nodes = itertools.chain(self.visitChildren(child) for child in ctx.children);
        grouped_nodes = defaultdict(list)
        for child in child_nodes:
            grouped_nodes[child.__class__].append(child)

        return nodes.File(
            piece_declarations=grouped_nodes[PieceDeclaration],
            static_var_declarations=grouped_nodes[StaticVarDeclaration],
            function_declarations=grouped_nodes[FuncDeclaration],
            parser_node=ctx
        )

    def visitSpeedOrNow(self, ctx: BosParser.SpeedOrNowContext):
        if expr := ctx.expression():
            return self.visit(expr)
        return None
    
    def visitGetTerm(self, ctx:BosParser.GetTermContext):
        return nodes.GetTerm(
            get_statement=self.visitKeywordStatementInner(ctx.getStatement()),
            parser_node=ctx
        )
    
    def visitRandTerm(self, ctx:BosParser.RandTermContext):
        return nodes.RandTerm(
            min=self.visit(ctx.expression(0)),
            max=self.visit(ctx.expression(1)),
            parser_node=ctx
        )
    
    def visitVarNameTerm(self, ctx:BosParser.VarNameTermContext):
        return nodes.VarNameTerm(
            var_name=self.visit(ctx.varName()),
            parser_node=ctx
        )

def main():
    with open('preprocessed/legcom.pcpp', 'rt', encoding='utf8') as file:
        str_data = file.read()

    input_stream = InputStream(str_data)
    lexer = BosLexer(input_stream)
    tokens = CommonTokenStream(lexer)
    parser = BosParser(tokens)

    token_tree: BosParser.FileContext = parser.file_()
    visitor = ASTVisitor()

    ast: nodes.ASTNode = visitor.visit(token_tree)
    print(
        json.dumps(
            ast.model_dump(),
            indent=2,
            default=lambda x: vars(x) if isinstance(x, SimpleNamespace) else repr(x)
        )
    )


if __name__ == '__main__':
    main()
