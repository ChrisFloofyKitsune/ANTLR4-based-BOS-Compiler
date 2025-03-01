import functools
import sys
from functools import total_ordering

from antlr4.BufferedTokenStream import BufferedTokenStream
from antlr4.Token import CommonToken
from typing import Self

from antlr4 import ParserRuleContext
from dataclasses import dataclass

from bos.gen.BosLexer import BosLexer
from bos.gen.BosParser import BosParser


@total_ordering
@dataclass()
class CodeLocation:
    start_line: int
    start_column: int
    end_line: int
    end_column: int
    source_file: str

    @classmethod
    def from_parser_node(cls, parser_node: ParserRuleContext | None, starting_file: str = None) -> Self | None:
        if parser_node is None:
            return None

        start: CommonToken = parser_node.start
        stop: CommonToken = parser_node.stop
        parser: BosParser = parser_node.parser
        token_stream: BufferedTokenStream = parser.getTokenStream()

        loc = cls.from_token(start, token_stream, starting_file)

        if loc is None:
            return None

        loc.end_line = stop.line + (loc.start_line - start.line)
        loc.end_column = stop.column + 1 + len(stop.text)
        return loc

    @classmethod
    def from_token(cls, token: CommonToken, token_stream: BufferedTokenStream, starting_file: str = None) -> Self | None:
        try:
            line_offset = 0
            source_file = starting_file if starting_file is not None else 'source file unspecified'

            preproc_token_idx = token_stream.previousTokenOnChannel(token.tokenIndex, BosLexer.LINE_MACRO)
            if preproc_token_idx != -1:
                preproc_token: CommonToken = token_stream.tokens[preproc_token_idx]
                if preproc_token.text is not None:
                    line_str, source_file = preproc_token.text.split()[1:3]
                    line_offset = int(line_str) - preproc_token.line - 1

            return cls(
                token.line + line_offset,
                token.column + 1,
                token.line + line_offset,
                token.column + 1 + len(token.text),
                source_file
            )
        except Exception as err:
            print(f'WARN: another error occurred while trying to calculate error_loc: {str(err)}', file=sys.stderr)
            return None
    
    def _comp_tuple(self) -> tuple[str, int, int, int, int]:
        return self.source_file, self.start_line, self.start_column, self.end_line, self.end_column
    
    def __repr__(self):
        return f'CodeLocation({self.source_file}, {self.start_line}, {self.start_column}, {self.end_line}, {self.end_column})'
    
    def __eq__(self, other):
        if not isinstance(other, CodeLocation):
            return NotImplemented
        return self._comp_tuple() == other._comp_tuple()
    
    def __lt__(self, other):
        if not isinstance(other, CodeLocation):
            return NotImplemented
        return self._comp_tuple() < other._comp_tuple()