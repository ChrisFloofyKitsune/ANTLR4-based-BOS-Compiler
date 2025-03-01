import logging
import operator
from functools import reduce

import lsprotocol.types as lsp_types
from pygls.server import LanguageServer
from pygls.workspace import TextDocument

from bos.bos_loader import BosLoader
from language_server_protocol.lsp_visitor import LspVisitor
from language_server_protocol.models import TokenType, TokenModifier, LspToken

log = logging.getLogger(__name__)


class BosLanguageServer(LanguageServer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tokens: dict[str, list[LspToken]] = dict()

    def parse(self, doc: TextDocument):
        loader = BosLoader(doc.path)
        loader._load_file_contents()
        loader._setup_preprocessor()
        loader._run_preprocessor()
        loader._run_parser()

        file_tree = loader.parser_node_tree

        lsp_visitor = LspVisitor(doc.path, loader.token_stream)
        lsp_visitor.visitFile(file_tree)

        self.tokens[doc.uri] = sorted(lsp_visitor.lsp_tokens)


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

    prev_loc = (0, 0)
    for token in tokens:
        log.debug("emitting token: %s", token)
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
                reduce(operator.or_, [tm.int_value for tm in token.token_modifiers], 0)
            ]
        )

        prev_loc = (line, column)

    return lsp_types.SemanticTokens(data=data)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(name)s : %(message)s")
    logging.getLogger('pygls.protocol.json_rpc').setLevel(logging.ERROR)
    server.start_io()

    # doc = TextDocument(uri='file:///E:/bar_dev/antlr4_based_bos_tools/bos/example_files/Units/legmed.bos')
    # server.parse(doc)
    # print(semantic_tokens_full(server, lsp_types.SemanticTokensParams(
    #     text_document=TextDocumentIdentifier(uri=doc.uri)
    # )))
