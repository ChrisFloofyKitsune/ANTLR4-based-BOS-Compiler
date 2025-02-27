from os import PathLike

import antlr4.error.ErrorListener
import os
import pcpp
from antlr4 import Parser
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream
from antlr4.Token import CommonToken
from io import StringIO
from pathlib import Path

from bos import ast_nodes
from bos.ast_visitor import ASTVisitor
from bos.gen.BosLexer import BosLexer
from bos.gen.BosParser import BosParser
from cob.compiler.code_error import CodeError
from unit_value_nums import UnitValue


class BosLoader:
    class ErrorListener(antlr4.error.ErrorListener.ErrorListener):
        def syntaxError(self, recognizer: Parser, offendingSymbol: CommonToken, line, column, msg, e):
            token_stream = recognizer.getTokenStream()
            raise CodeError.from_token(msg, offendingSymbol, token_stream)

    def __init__(
        self,
        bos_file_path: str | PathLike[str],
        include_paths: list[str | PathLike[str]] = None,
    ):
        self.filepath = Path(bos_file_path)
        self.include_paths = [Path(p) for p in include_paths] if include_paths is not None else []

        self.file_contents: str | None = None

        self.preprocessor: pcpp.Preprocessor | None = None
        self.preprocessed_file_contents: str | None = None

        self.bos_parser: BosParser | None = None
        self.token_stream: CommonTokenStream | None = None
        self.bos_lexer: BosLexer | None = None

        self.parser_node_tree: BosParser.FileContext | None = None
        self.ast_node_tree: ast_nodes.File | None = None

    def _setup_preprocessor(self, force_reload=False):
        if self.preprocessor is not None and not force_reload:
            return

        self.preprocessor = pcpp.Preprocessor()
        for def_str in [
            "TRUE 1",
            "true 1",
            "FALSE 0",
            "false 0",
            "UNKNOWN_UNIT_VALUE(val) val",
            *[f'{val.name.upper()} {val.value}' for val in UnitValue]
        ]:
            self.preprocessor.define(def_str)

        for include_path in self.include_paths:
            self.preprocessor.add_path(os.fspath(include_path))

    def _load_file_contents(self, force_reload=False):
        if self.file_contents is not None and not force_reload:
            return

        with open(self.filepath, 'rt', encoding='utf8') as f:
            self.file_contents = f.read()

    def _run_preprocessor(self, force_reload=False):
        if self.preprocessed_file_contents is not None and not force_reload:
            return

        self.preprocessor.parse(self.file_contents, self.filepath)
        output = StringIO()
        self.preprocessor.write(output)
        self.preprocessed_file_contents = output.getvalue()

    def _run_parser(self, force_reload=False):
        if self.parser_node_tree is not None and not force_reload:
            return

        self.bos_lexer = BosLexer(InputStream(self.preprocessed_file_contents))
        self.token_stream = CommonTokenStream(self.bos_lexer)
        self.bos_parser = BosParser(self.token_stream)

        self.bos_parser.addErrorListener(self.ErrorListener())

        self.parser_node_tree = self.bos_parser.file_()
        if self.bos_parser.getNumberOfSyntaxErrors() > 0:
            raise ValueError('Syntax errors found in preprocessed file')

    def _run_ast_conversion(self, force_reload=False):
        if self.ast_node_tree is not None and not force_reload:
            return

        ast_visitor = ASTVisitor()
        self.ast_node_tree = ast_visitor.visitFile(self.parser_node_tree)

    def load_file(self, force_reload=False) -> ast_nodes.File:
        self._load_file_contents(force_reload)
        self._setup_preprocessor(force_reload)
        self._run_preprocessor(force_reload)
        self._run_parser(force_reload)
        self._run_ast_conversion(force_reload)

        return self.ast_node_tree

    def dump_preprocessed_file(self, destination: str | PathLike[str] = None):
        if self.preprocessed_file_contents is None:
            self._load_file_contents()
            self._setup_preprocessor()
            self._run_preprocessor()

        if destination is None:
            destination = self.filepath.parent
        elif isinstance(destination, str):
            destination = Path(destination)

        if destination.is_dir():
            destination = destination.joinpath(self.filepath.stem + '.preprocessed' + self.filepath.suffix)

        with open(destination, 'wt', encoding='utf8') as f:
            f.write(self.preprocessed_file_contents)


if __name__ == '__main__':
    loader = BosLoader('./example_files/Units/legcom.bos')
    print(loader.load_file().model_dump())
