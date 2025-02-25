from dataclasses import dataclass

import sys
from antlr4.BufferedTokenStream import BufferedTokenStream
from antlr4.ParserRuleContext import ParserRuleContext
from antlr4.Token import CommonToken
from typing import NamedTuple

import bos.ast_nodes as nodes
from bos import bos_loader
from bos.bos_loader import BosLoader
from bos.gen.BosLexer import BosLexer
from bos.gen.BosParser import BosParser


class BosCompilerError(Exception):
    @dataclass
    class ErrorLoc:
        start_line: int
        start_column: int
        end_line: int
        end_column: int
        source_file: str

    def __init__(self, message: str, error_loc: ErrorLoc | None):
        super().__init__(message, error_loc)
        self.message = message
        self.error_loc = error_loc

    @classmethod
    def from_parser_node(cls, message: str, parser_node: ParserRuleContext | None):
        error_loc = None
        if parser_node is not None:
            try:
                start: CommonToken = parser_node.start
                stop: CommonToken = parser_node.stop
                parser: BosParser = parser_node.parser
                token_stream: BufferedTokenStream = parser.getTokenStream()
                preproc_token_idx = token_stream.previousTokenOnChannel(start.tokenIndex, BosLexer.LINE_MACRO)

                line_offset = 0
                source_file = 'original file'
                if preproc_token_idx != -1:
                    preproc_token: CommonToken = token_stream.tokens[preproc_token_idx]
                    if preproc_token.text is not None and preproc_token.text.startswith('#line'):
                        line_str, source_file = preproc_token.text.split()[1:3]
                        line_offset = int(line_str) - preproc_token.line - 1

                error_loc = cls.ErrorLoc(
                    start.line + line_offset,
                    start.column + 1,
                    stop.line + line_offset,
                    stop.column + 1 + len(stop.text),
                    source_file
                )
            except Exception as err:
                print(f'WARN: another error occurred while trying to calculate error_loc: {str(err)}', file=sys.stderr)

        return BosCompilerError(message, error_loc)


class Compiler:
    ...


def __main(file_node: nodes.File):

    # Keep It Stupid Simple

    pieces: dict[nodes.PieceName, int] = {}
    static_vars: dict[nodes.VarName, int] = {}
    local_vars: dict[nodes.VarName, int] = {}

    def register_static_var(static_var: nodes.VarName):
        if static_var in static_vars:
            msg = f'duplicate declaration of static var "{static_var.name}"'
            raise BosCompilerError.from_parser_node(msg, static_var.parser_node)

        static_vars[static_var] = len(static_vars)

    for sv in file_node.static_var_names:
        register_static_var(sv)
    print(static_vars)


if __name__ == '__main__':
    loader = BosLoader('../bos/example_files/Units/legcom.bos')
    loader.dump_preprocessed_file('./preprocessed')
    __main(loader.load_file())
