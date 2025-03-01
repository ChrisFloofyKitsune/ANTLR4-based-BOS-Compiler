import logging
from typing import cast

from antlr4 import CommonTokenStream
from antlr4.ParserRuleContext import ParserRuleContext
from antlr4.Token import CommonToken
from antlr4.tree.Tree import TerminalNodeImpl

from bos.gen.BosLexer import BosLexer
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

        log.info('%s tokens', len(token_stream.tokens))
        for token in token_stream.tokens:
            match token.channel:
                case BosLexer.COMMENTS:
                    self._add_token(token, token_type=TokenType.Comment)
                case BosLexer.PREPROCESSOR:
                    self._add_token(token, token_type=TokenType.Macro)

    def _add_token(
        self, source_obj: ParserRuleContext | TerminalNodeImpl | CommonToken, token_type: TokenType,
        *token_mods: TokenModifier
    ):
        token_mods = list(token_mods)
        if isinstance(source_obj, ParserRuleContext):
            self.lsp_tokens.append(
                LspToken(
                    code_location=CodeLocation.from_parser_node(source_obj, self.filepath),
                    token_type=token_type,
                    token_modifiers=token_mods
                )
            )

        if isinstance(source_obj, TerminalNodeImpl):
            source_obj = source_obj.symbol

        if isinstance(source_obj, CommonToken):
            self.lsp_tokens.append(
                LspToken(
                    code_location=CodeLocation.from_token(source_obj, self.token_stream, self.filepath),
                    token_type=token_type,
                    token_modifiers=token_mods
                )
            )

    def visitPieceDecl(self, ctx: BosParser.PieceDeclContext):
        self._add_token(ctx.PIECE(), TokenType.Enum)
        for piece_name_ctx in ctx.pieceName():
            self._add_token(piece_name_ctx, TokenType.EnumMember, TokenModifier.Declaration, TokenModifier.ReadOnly)
            self.name_registry.register(cast(BosParser.PieceNameContext, piece_name_ctx).getText(), NameType.PIECE)

    def visitStaticVarDecl(self, ctx: BosParser.StaticVarDeclContext):
        self._add_token(ctx.STATIC_VAR(), TokenType.Enum)
        for var_name_ctx in ctx.varName():
            self._add_token(var_name_ctx, TokenType.Variable, TokenModifier.Static, TokenModifier.Declaration)
            self.name_registry.register(cast(BosParser.VarNameContext, var_name_ctx).getText(), NameType.STATIC)

    def visitConstant(self, ctx: BosParser.ConstantContext):
        self._add_token(ctx, TokenType.Number)

    def visitBinaryExpr(self, ctx: BosParser.BinaryExprContext):
        self.visit(ctx.operand1)
        self._add_token(ctx.op, TokenType.Operator)
        self.visit(ctx.operand2)

    def visitUnaryExpr(self, ctx: BosParser.UnaryExprContext):
        self._add_token(ctx.op, TokenType.Operator)
        self.visit(ctx.operand)

    def visitKeywordStatement(self, ctx: BosParser.KeywordStatementContext):
        ctx: ParserRuleContext = ctx.getChild(0, ParserRuleContext)
        for text_node in (c for c in ctx.children if isinstance(c, TerminalNodeImpl)):
            if text_node.getText() in ('(', ')', '()'):
                continue
            self._add_token(text_node, token_type=TokenType.Keyword)
        for rule_node in (c for c in ctx.children if isinstance(c, ParserRuleContext)):
            self.visit(rule_node)

    def visitSpeedOrNow(self, ctx: BosParser.SpeedOrNowContext):
        if speed := ctx.SPEED():
            self._add_token(speed, TokenType.Keyword)
            self.visit(ctx.expression())
        elif now := ctx.NOW():
            self._add_token(now, TokenType.Keyword)

    def visitAxis(self, ctx: BosParser.AxisContext):
        self._add_token(ctx, TokenType.EnumMember, TokenModifier.DefaultLibrary)

    def visitFuncDecl(self, ctx: BosParser.FuncDeclContext):
        self.name_registry.clear_local_names()

        self._add_token(ctx.funcName(), TokenType.Function, TokenModifier.Declaration)
        self.name_registry.register(ctx.funcName().getText(), NameType.FUNCTION)
        for arg_name_ctx in ctx.argName():
            self._add_token(arg_name_ctx, TokenType.Parameter)
            self.name_registry.register(arg_name_ctx.getText(), NameType.ARG)
        self.visit(ctx.statementBlock())

    def visitVarNameTerm(self, ctx: BosParser.VarNameTermContext):
        var_name_ctx: BosParser.VarNameContext = ctx.varName()
        _, name_type = self.name_registry.lookup(var_name_ctx.getText())
        match name_type:
            case NameType.STATIC:
                self._add_token(var_name_ctx, TokenType.Variable, TokenModifier.Static)
            case NameType.PIECE:
                self._add_token(var_name_ctx, TokenType.EnumMember, TokenModifier.Static, TokenModifier.ReadOnly)
            case NameType.ARG | NameType.LOCAL:
                self._add_token(var_name_ctx, TokenType.Variable)
            case NameType.FUNCTION:
                self._add_token(var_name_ctx, TokenType.Function)
