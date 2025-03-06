import logging
import operator
from functools import reduce
from typing import cast

from antlr4 import CommonTokenStream
from antlr4.ParserRuleContext import ParserRuleContext
from antlr4.Token import CommonToken
from antlr4.tree.Tree import TerminalNodeImpl

from bos.gen.BosParser import BosParser
from bos.gen.BosParserVisitor import BosParserVisitor
from cob.compiler.name_registry import NameRegistry, NameType
from code_location import CodeLocation
from language_server_protocol.models import LspToken, TokenType, TokenModifier

log = logging.getLogger(__name__)


class LspVisitor(BosParserVisitor):
    def __init__(self, filepath: str, token_stream: CommonTokenStream):
        super().__init__()

        self.lsp_tokens: list[LspToken] = []
        self.name_registry = NameRegistry[str]()

        self.filepath = filepath
        self.token_stream = token_stream

    def _add_token(
        self, source_obj: ParserRuleContext | TerminalNodeImpl | CommonToken, token_type: TokenType,
        *token_mods: TokenModifier
    ):
        token_mod = reduce(operator.or_, token_mods, TokenModifier(0))
        if isinstance(source_obj, ParserRuleContext):
            self.lsp_tokens.append(
                LspToken(
                    code_location=CodeLocation.from_parser_node(source_obj, self.filepath),
                    token_type=token_type,
                    token_modifier=token_mod
                )
            )

        if isinstance(source_obj, TerminalNodeImpl):
            source_obj = source_obj.symbol

        if isinstance(source_obj, CommonToken):
            self.lsp_tokens.append(
                LspToken(
                    code_location=CodeLocation.from_token(source_obj, self.token_stream, self.filepath),
                    token_type=token_type,
                    token_modifier=token_mod
                )
            )
    
    def visitFile(self, ctx:BosParser.FileContext):
        func_declarations = []
        for decl in ctx.declaration():
            decl: BosParser.DeclarationContext
            if piece_decl := decl.pieceDecl():
                self.visit(piece_decl)
            if static_var_decl := decl.staticVarDecl():
                self.visit(static_var_decl)
            if func_decl := decl.funcDecl():
                func_declarations.append(func_decl)
                self._add_token(func_decl.funcName(), TokenType.Function, TokenModifier.Declaration | TokenModifier.Static)
                self.name_registry.register(func_decl.funcName().getText(), NameType.FUNCTION)
        for func_decl in func_declarations:
            self.visit(func_decl)
    
    def visitPieceDecl(self, ctx: BosParser.PieceDeclContext):
        for piece_name_ctx in ctx.pieceName():
            self._add_token(
                piece_name_ctx, TokenType.EnumMember, TokenModifier.Static, TokenModifier.Declaration,
                TokenModifier.ReadOnly
            )
            self.name_registry.register(cast(BosParser.PieceNameContext, piece_name_ctx).getText(), NameType.PIECE)

    def visitStaticVarDecl(self, ctx: BosParser.StaticVarDeclContext):
        for var_name_ctx in ctx.varName():
            self._add_token(var_name_ctx, TokenType.Variable, TokenModifier.Static, TokenModifier.Declaration)
            self.name_registry.register(cast(BosParser.VarNameContext, var_name_ctx).getText(), NameType.STATIC)

    def visitKeywordStatement(self, ctx: BosParser.KeywordStatementContext):
        ctx: ParserRuleContext = ctx.getChild(0, ParserRuleContext)
        for rule_node in (c for c in ctx.children if isinstance(c, ParserRuleContext)):
            self.visit(rule_node)

    def visitFuncDecl(self, ctx: BosParser.FuncDeclContext):
        self.name_registry.clear_local_names()

        for arg_name_ctx in ctx.argName():
            self._add_token(arg_name_ctx, TokenType.Parameter, TokenModifier.Declaration)
            self.name_registry.register(arg_name_ctx.getText(), NameType.ARG)
        self.visit(ctx.statementBlock())

    def visitPieceName(self, ctx: BosParser.PieceNameContext):
        self.visit_var_name_node(ctx)

    def visitFuncName(self, ctx: BosParser.FuncNameContext):
        self.visit_var_name_node(ctx)

    def visitVarNameTerm(self, ctx: BosParser.VarNameTermContext):
        var_name_ctx: BosParser.VarNameContext = ctx.varName()
        self.visit_var_name_node(var_name_ctx)

    def visit_var_name_node(self, name_node: ParserRuleContext, /, extra_token_mod: TokenModifier = 0):
        _, name_type = self.name_registry.lookup(name_node.getText())
        match name_type:
            case NameType.STATIC:
                self._add_token(name_node, TokenType.Variable, TokenModifier.Static | extra_token_mod)
            case NameType.PIECE:
                self._add_token(name_node, TokenType.EnumMember, TokenModifier.Static, TokenModifier.ReadOnly | extra_token_mod)
            case NameType.ARG:
                self._add_token(name_node, TokenType.Parameter, extra_token_mod)
            case NameType.LOCAL:
                self._add_token(name_node, TokenType.Variable, extra_token_mod)
            case NameType.FUNCTION:
                self._add_token(name_node, TokenType.Function, TokenModifier.Static | extra_token_mod)

    def visitAssignStatement(self, ctx: BosParser.AssignStatementContext):
        if (var_name := ctx.varName()) and (expr := ctx.expression()):
            self.visit_var_name_node(var_name, extra_token_mod=TokenModifier.Modification)
            self.visit(expr)
        elif inc := ctx.incStatement():
            self.visit_var_name_node(inc.varName())
        elif dec := ctx.decStatement():
            self.visit_var_name_node(dec.varName())
