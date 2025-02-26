import json

import enum
import sys
from antlr4.BufferedTokenStream import BufferedTokenStream
from antlr4.ParserRuleContext import ParserRuleContext
from antlr4.Token import CommonToken
from dataclasses import dataclass
from enum import IntEnum

import bos.ast_nodes as nodes
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


class NameRegistry:

    class NameType(IntEnum):
        STATIC = 0, 'Static variable'
        LOCAL = 1, 'Local variable'
        PIECE = 2, 'Piece name'
        FUNCTION = 3, 'Function name'
        ARG = 4, 'Function argument'

        @enum.property
        def description(self) -> str:
            return self._description

        def __new__(cls, value, description):
            obj = int.__new__(cls, value)
            obj._value_ = value
            obj._description = description
            return obj

    def __init__(self):
        self.__backing_dict: dict[NameRegistry.NameType, dict[nodes.NameNode, int]] = {
            t: dict() for t in NameRegistry.NameType
        }

        self.__lookup_dict: dict[nodes.NameNode, tuple[int, NameRegistry.NameType]] = dict()

    def register(self, name: nodes.NameNode, name_type: NameType):
        lookup_result = self.__lookup_dict.get(name, None)

        if lookup_result is not None:
            raise BosCompilerError.from_parser_node(
                f'invalid declaration of {name_type.description} "{name.name}, '
                f'name has been declared as a {lookup_result[1].description}"',
                name.parser_node
            )

        new_idx = len(self.__backing_dict[name_type])
        self.__backing_dict[name_type][name] = new_idx
        self.__lookup_dict[name] = (new_idx, name_type)

    def get_idx(self, name: nodes.NameNode) -> tuple[int, NameType]:
        result = self.__lookup_dict.get(name, None)

        if result is None:
            raise BosCompilerError.from_parser_node(
                f'name "{name.name}" has not been defined',
                name.parser_node
            )

        return result

    def clear_local_names(self):
        self.__backing_dict[NameRegistry.NameType.LOCAL].clear()
        self.__backing_dict[NameRegistry.NameType.ARG].clear()

        self.__lookup_dict = {
            name: (idx, type_) for name, (idx, type_) in self.__lookup_dict.items()
            if type_ not in (NameRegistry.NameType.LOCAL, NameRegistry.NameType.ARG)
        }

    def get_names(self):
        return self.__lookup_dict.copy()
    
    def get_names_by_type(self, name_type: NameType):
        return self.__backing_dict[name_type].copy()


def __main(file_node: nodes.File):

    # Keep It Stupid Simple
    
    name_registry = NameRegistry()
    
    for declaration in file_node.declarations:
        if isinstance(declaration, nodes.PieceDeclaration):
            for piece_name in declaration.names:
                name_registry.register(piece_name, NameRegistry.NameType.PIECE)
        elif isinstance(declaration, nodes.StaticVarDeclaration):
            for var_name in declaration.names:
                name_registry.register(var_name, NameRegistry.NameType.STATIC)
        elif isinstance(declaration, nodes.FuncDeclaration):
            name_registry.register(declaration.name, NameRegistry.NameType.FUNCTION)
        else:
            raise ValueError('Unable to register names for object', declaration)
    
    for item in name_registry.get_names().items():
        print(item)

if __name__ == '__main__':
    loader = BosLoader('../bos/example_files/Units/legcom.bos')
    loader.dump_preprocessed_file('./preprocessed')
    __main(loader.load_file())
