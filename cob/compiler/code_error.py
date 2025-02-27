import sys
from antlr4 import ParserRuleContext
from antlr4.BufferedTokenStream import BufferedTokenStream
from antlr4.Token import CommonToken
from dataclasses import dataclass

from bos.gen.BosLexer import BosLexer
from bos.gen.BosParser import BosParser


class CodeError(Exception):
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
                source_file = '(file being parsed)'
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

        return cls(message, error_loc)

    @classmethod
    def from_token(cls, message: str, token: CommonToken, token_stream: BufferedTokenStream):
        error_loc = None
        try:
            line_offset = 0
            source_file = '(file being parsed)'

            preproc_token_idx = token_stream.previousTokenOnChannel(token.tokenIndex, BosLexer.LINE_MACRO)
            if preproc_token_idx != -1:
                preproc_token: CommonToken = token_stream.tokens[preproc_token_idx]
                if preproc_token.text is not None and preproc_token.text.startswith('#line'):
                    line_str, source_file = preproc_token.text.split()[1:3]
                    line_offset = int(line_str) - preproc_token.line - 1

            error_loc = cls.ErrorLoc(
                token.line + line_offset,
                token.column + 1,
                token.line + line_offset,
                token.column + 1 + len(token.text),
                source_file
            )
        except Exception as err:
            print(f'WARN: another error occurred while trying to calculate error_loc: {str(err)}', file=sys.stderr)

        return cls(message, error_loc)
