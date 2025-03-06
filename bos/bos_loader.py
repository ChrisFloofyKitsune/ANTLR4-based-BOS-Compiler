import logging
import time
from os import PathLike
from pathlib import Path

import antlr4.error.ErrorListener
import pcpp
from antlr4 import Parser
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream
from antlr4.Token import CommonToken
from antlr4.atn.PredictionMode import PredictionMode
from antlr4.error.ErrorStrategy import BailErrorStrategy

from bos import ast_nodes
from bos.ast_visitor import ASTVisitor
from bos.bos_preprocessor import BosPreprocessor
from bos.gen.BosLexer import BosLexer
from bos.gen.BosParser import BosParser
from code_error import CodeError
from code_location import CodeLocation


class BosLoader:

    class ErrorListener(antlr4.error.ErrorListener.ErrorListener):
        def __init__(self, loader: 'BosLoader'):
            self.loader = loader

        def syntaxError(self, recognizer: Parser, offending_symbol: CommonToken, line, column, msg, e):
            token_stream = recognizer.getTokenStream()
            self.loader.parse_errors.append(CodeError(msg, CodeLocation.from_token(offending_symbol, token_stream)))

    def __init__(
        self,
        bos_file_path: str | PathLike[str],
        include_paths: list[str | PathLike[str]] = None,
        /,
        enable_constant_folding=False,
        file_contents: str = None,
    ):

        self.filepath = Path(bos_file_path)
        self.include_paths = [Path(p) for p in include_paths] if include_paths is not None else []
        self.enable_constant_folding = enable_constant_folding

        if file_contents is not None:
            self.file_contents = file_contents

        self.log = logging.getLogger(self.__class__.__name__).getChild(self.filepath.name)

        self.file_contents: str | None = None

        self.preprocessor: pcpp.Preprocessor | None = None
        self.preprocessed_file_contents: str | None = None

        self.bos_lexer: BosLexer | None = None
        self.token_stream: CommonTokenStream | None = None
        self.bos_parser: BosParser | None = None

        self.parse_errors: list[CodeError] = []
        self.parser_node_tree: BosParser.FileContext | None = None
        self.ast_node_tree: ast_nodes.File | None = None

    def _load_file_contents(self, force_reload=False):
        if self.file_contents is not None and not force_reload:
            return

        with open(self.filepath, 'rt', encoding='utf8') as f:
            self.file_contents = f.read()
            self.log.debug('File loaded, %d bytes', len(self.file_contents.encode('utf8')))

    def _run_preprocessor(self, force_reload=False):
        if self.preprocessed_file_contents is not None and not force_reload:
            return

        self.preprocessor = BosPreprocessor()

        (
            self.preprocessed_file_contents,
            self.reconstructed_file_contents,
            self.preproc_chunks
        ) = self.preprocessor.process_file(self.file_contents, self.filepath, self.include_paths)

    def _run_parser(self, force_reload=False):
        if self.parser_node_tree is not None and not force_reload:
            return

        self.bos_lexer = BosLexer(InputStream(self.preprocessed_file_contents))
        self.token_stream = CommonTokenStream(self.bos_lexer)

        # first try with faster, but weaker, parse strategy
        self.bos_parser = BosParser(self.token_stream)
        self.bos_parser._interp.predictionMode = PredictionMode.SLL
        self.bos_parser.removeErrorListeners()
        self.bos_parser._errHandler = BailErrorStrategy()

        start_time = time.perf_counter()

        try:
            self.parser_node_tree = self.bos_parser.file_()
        except BaseException:
            self.log.debug(
                'File could not be handled by faster, but weaker, SLL parser, trying again with default LL parser'
            )
            # reset and try again
            self.bos_lexer = BosLexer(InputStream(self.preprocessed_file_contents))
            self.token_stream = CommonTokenStream(self.bos_lexer)
            self.bos_parser = BosParser(self.token_stream)
            self.bos_parser.addErrorListener(self.ErrorListener(self))

            self.parser_node_tree = self.bos_parser.file_()

        end_time = time.perf_counter()
        self.log.debug('Parsing took %.2f seconds (%.2f mins)', end_time - start_time, (end_time - start_time) / 60)

        if self.bos_parser.getNumberOfSyntaxErrors() > 0:
            raise ValueError('Syntax errors found in preprocessed file')

    def _run_ast_conversion(self, force_reload=False):
        if self.ast_node_tree is not None and not force_reload:
            return

        ast_visitor = ASTVisitor(enable_constant_folding=self.enable_constant_folding)
        self.ast_node_tree = ast_visitor.visitFile(self.parser_node_tree)
        self.log.debug('AST conversion complete')

    def load_file(self, force_reload=False) -> ast_nodes.File:
        self._load_file_contents(force_reload)
        self._run_preprocessor(force_reload)
        self._run_parser(force_reload)
        self._run_ast_conversion(force_reload)

        return self.ast_node_tree

    def dump_preprocessed_file(self, destination: str | PathLike[str] = None):
        if self.preprocessed_file_contents is None:
            self._load_file_contents()
            self._run_preprocessor()

        if destination is None:
            destination = self.filepath.parent
        elif isinstance(destination, str):
            destination = Path(destination)

        if destination.is_dir():
            destination = destination.joinpath(self.filepath.stem + '.preprocessed' + self.filepath.suffix)

        with open(destination, 'wt', encoding='utf8') as f:
            f.write(self.preprocessed_file_contents)
        self.log.info('Preprocessed file dumped to %s', destination)


if __name__ == '__main__':
    def main():
        loader = BosLoader('./example_files/Units/legcom.bos')
        loader.dump_preprocessed_file('./preprocessed_blah.txt')
        # print(loader.load_file().model_dump())


    main()
