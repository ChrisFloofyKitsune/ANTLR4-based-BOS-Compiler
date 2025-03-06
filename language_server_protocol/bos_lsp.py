import logging

import lsprotocol.types as lsp_types
from antlr4 import CommonTokenStream, InputStream
from antlr4.Token import CommonToken
from pygls.server import LanguageServer
from pygls.workspace import TextDocument

from bos.bos_loader import BosLoader
from bos.gen.BosLexer import BosLexer
from code_location import CodeLocation
from language_server_protocol.lsp_visitor import LspVisitor
from language_server_protocol.models import TokenType, TokenModifier, LspToken

log = logging.getLogger(__name__)

lexer_token_symbolic_type_defs: dict[tuple[int, ...], tuple[TokenType, TokenModifier]] = {
    (BosLexer.LINE_COMMENT, BosLexer.BLOCK_COMMENT): (TokenType.Comment, 0),
    (BosLexer.INCLUDE_DIRECTIVE,): (TokenType.Namespace, 0),
    (BosLexer.LINE_DIRECTIVE, BosLexer.MULTI_LINE_MACRO, BosLexer.SINGLE_LINE_MACRO): (TokenType.Macro, 0),
    (BosLexer.STRING,): (TokenType.String, 0),
    (BosLexer.LINEAR_CONSTANT,): (TokenType.Number, TokenModifier.Linear),
    (BosLexer.DEGREES_CONSTANT,): (TokenType.Number, TokenModifier.Angular),
    (BosLexer.INT, BosLexer.FLOAT): (TokenType.Number, 0),
    (
        BosLexer.EQUAL_ASSIGN,
        BosLexer.OP_ADD, BosLexer.OP_MINUS, BosLexer.OP_MULT, BosLexer.OP_DIV, BosLexer.OP_MOD,
        BosLexer.OP_INCREMENT, BosLexer.OP_DECREMENT,
        BosLexer.BITWISE_AND, BosLexer.BITWISE_OR, BosLexer.BITWISE_XOR,
        BosLexer.COMP_EQUAL, BosLexer.COMP_NOT_EQUAL, BosLexer.COMP_LESS, BosLexer.COMP_LESS_EQUAL,
        BosLexer.COMP_GREATER, BosLexer.COMP_GREATER_EQUAL,
        BosLexer.LOGICAL_AND, BosLexer.LOGICAL_OR, BosLexer.LOGICAL_NOT, BosLexer.LOGICAL_XOR,
    ): (TokenType.Operator, 0),
    (BosLexer.STATIC_VAR, BosLexer.PIECE,): (TokenType.Enum, 0),
    (
        BosLexer.VAR,
        BosLexer.TURN, BosLexer.MOVE,
        BosLexer.SPIN, BosLexer.STOP_SPIN,
        BosLexer.WAIT_FOR_TURN, BosLexer.WAIT_FOR_MOVE,
        BosLexer.SET, BosLexer.GET,
        BosLexer.CALL_SCRIPT, BosLexer.START_SCRIPT, BosLexer.RETURN,
        BosLexer.EMIT_SFX,
        BosLexer.SLEEP,
        BosLexer.HIDE, BosLexer.SHOW,
        BosLexer.EXPLODE,
        BosLexer.SIGNAL, BosLexer.SET_SIGNAL_MASK,
        BosLexer.ATTACH_UNIT, BosLexer.DROP_UNIT,
        BosLexer.PLAY_SOUND,
        BosLexer.RAND,
    ): (TokenType.Keyword, 0),
    (
        BosLexer.AROUND, BosLexer.ALONG,
        BosLexer.X_AXIS, BosLexer.Y_AXIS, BosLexer.Z_AXIS,
        BosLexer.TO, BosLexer.FROM, BosLexer.NOW, BosLexer.SPEED,
        BosLexer.ACCELERATE, BosLexer.DECELERATE,
        BosLexer.TYPE,
    ): (TokenType.Modifier, 0),
    (
        BosLexer.CACHE, BosLexer.DONT_CACHE, BosLexer.DONT_SHADOW, BosLexer.DONT_SHADE,
    ): (TokenType.Keyword, TokenModifier.Deprecated),
}

lexer_token_symbolic_type_lookup: dict[int, tuple[TokenType, TokenModifier]] = {
    token_idx: symbol_def
    for token_keys, symbol_def in lexer_token_symbolic_type_defs.items()
    for token_idx in token_keys
}


class BosLanguageServer(LanguageServer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tokens: dict[str, list[LspToken]] = dict()

    def parse(self, doc: TextDocument):
        # quickly rip through the tokens in the file and store them
        box_lexer = BosLexer(InputStream(doc.source))
        token_stream = CommonTokenStream(box_lexer)
        token_stream.fill()

        token_list: list[LspToken] = list()
        for token in token_stream.tokens:
            token: CommonToken
            if token.type in lexer_token_symbolic_type_lookup:
                token_type, token_mod = lexer_token_symbolic_type_lookup[token.type]
                token_list.append(
                    LspToken(
                        code_location=CodeLocation.from_token(token, token_stream, doc.path),
                        token_type=token_type,
                        token_modifier=token_mod
                    )
                )

        self.tokens[doc.uri] = token_list

        try:
            bos_loader = BosLoader(doc.path, file_contents=doc.source)
            bos_loader.load_file()
            
            lsp_visitor = LspVisitor(doc.path, bos_loader.token_stream)
            lsp_visitor.visit(bos_loader.parser_node_tree)
            
            self.tokens[doc.uri].extend(lsp_visitor.lsp_tokens)
        except Exception as err:
            log.exception(err)


server = BosLanguageServer('bos-language-server', 'alpha')


@server.feature(lsp_types.TEXT_DOCUMENT_DID_OPEN)
def did_open(ls: BosLanguageServer, params: lsp_types.DidOpenTextDocumentParams):
    doc = ls.workspace.get_text_document(params.text_document.uri)
    ls.parse(doc)


@server.feature(lsp_types.TEXT_DOCUMENT_DID_CHANGE)
def did_change(ls: BosLanguageServer, params: lsp_types.DidChangeTextDocumentParams):
    doc = ls.workspace.get_text_document(params.text_document.uri)
    ls.parse(doc)


@server.feature(lsp_types.TEXT_DOCUMENT_DID_SAVE)
def did_save(ls: BosLanguageServer, params: lsp_types.DidSaveTextDocumentParams):
    doc = ls.workspace.get_text_document(params.text_document.uri)
    ls.parse(doc)


@server.feature(
    lsp_types.TEXT_DOCUMENT_SEMANTIC_TOKENS_FULL,
    lsp_types.SemanticTokensLegend(
        token_types=[tt.str_value for tt in TokenType],
        token_modifiers=[tm.str_value for tm in TokenModifier]
    )
)
def semantic_tokens_full(ls: BosLanguageServer, params: lsp_types.SemanticTokensParams):
    data = []
    tokens: list[LspToken] = ls.tokens.get(params.text_document.uri, [])
    tokens.sort()

    prev_loc = (0, 0)
    for token in tokens:
        line = token.code_location.start_line - 1
        column = token.code_location.start_column - 1
        length = token.code_location.end_column - token.code_location.start_column

        rel_line = line - prev_loc[0]
        rel_column = column - prev_loc[1] if rel_line == 0 else column
        data.extend(
            [
                rel_line,
                rel_column,
                length,
                token.token_type.int_value,
                token.token_modifier.value
            ]
        )

        prev_loc = (line, column)

    return lsp_types.SemanticTokens(data=data)


if __name__ == '__main__':
    def main():
        logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s : %(message)s")
        logging.getLogger('pygls.protocol.json_rpc').setLevel(logging.ERROR)
        server.start_io()


    def test_main():
        doc = TextDocument(uri='file:///E:/bar_dev/antlr4_based_bos_tools/bos/example_files/Units/legmed.bos')
        server.parse(doc)
        print(
            semantic_tokens_full(
                server, lsp_types.SemanticTokensParams(
                    text_document=lsp_types.TextDocumentIdentifier(uri=doc.uri)
                )
            )
        )


    main()
