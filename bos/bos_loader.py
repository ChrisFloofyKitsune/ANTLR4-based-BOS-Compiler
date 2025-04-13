import logging
import time
from os import PathLike
from pathlib import Path

import pcpp
import tree_sitter
import tree_sitter_bos

from bos import ast_nodes
from bos.ast_visitor import TreeSitterBosVisitor
from bos.bos_preprocessor import BosPreprocessor
from code_error import CodeError
from code_location import CodeLocation


class BosLoader:
    def __init__(
        self,
        bos_file_path: str | PathLike[str],
        include_paths: list[str | PathLike[str]] = None,
        /,
        enable_constant_folding=False,
        file_contents: str = None,
    ):
        self.filepath = Path(bos_file_path)
        self.log = logging.getLogger(self.__class__.__name__).getChild(self.filepath.name)
        self.include_paths = [Path(p) for p in include_paths] if include_paths is not None else []
        self.enable_constant_folding = enable_constant_folding

        self.file_contents: str | None = None

        if file_contents is not None:
            self.file_contents = file_contents

        self.preprocessor: pcpp.Preprocessor | None = None
        self.preprocessed_file_contents: str | None = None

        self.parser: tree_sitter.Parser

        self.parse_errors: list[CodeError] = []
        self.parser_tree: tree_sitter.Tree | None = None
        self.ast_node_tree: ast_nodes.File | None = None

    def _load_file_contents(self, force_reload=False):
        if self.file_contents is not None and not force_reload:
            return

        with open(self.filepath, 'rt') as f:
            self.file_contents = f.read()
            self.log.debug('File %s loaded, %d bytes', self.filepath, self.filepath.lstat().st_size)

    def _run_preprocessor(self, force_reload=False):
        if self.preprocessed_file_contents is not None and not force_reload:
            return

        self.preprocessor = BosPreprocessor()

        (
            self.preprocessed_file_contents,
            self.reconstructed_file_contents,
            self.preproc_chunks
        ) = self.preprocessor.process_file(self.file_contents, self.filepath, self.include_paths)

    @staticmethod
    def check_errors(tree: tree_sitter.Tree, file: Path):
        error_query = tree_sitter.Query(tree.language, "(ERROR) @error")
        error_query_cursor = tree_sitter.QueryCursor(error_query)

        if errors := error_query_cursor.captures(tree.root_node):
            return errors['error']

        missing_query = tree_sitter.Query(tree.language, "(MISSING) @missing")
        missing_query_cursor = tree_sitter.QueryCursor(missing_query)

        if missing := missing_query_cursor.captures(tree.root_node):
            return missing['missing']

        return None

    NODES_TO_EXPAND = ['function_declaration', 'compound_statement', 'while_statement', 'ERROR', 'MISSING']

    @staticmethod
    def display_node(node: tree_sitter.Node, depth=0):
        print('->' * (depth + 1), node.grammar_name, '<-' * (depth + 1))
        for idx, child in enumerate(node.children):
            if (field_name := node.field_name_for_child(idx)) is not None:
                print('  ' * depth, '---', field_name, '---')

            if child.grammar_name in BosLoader.NODES_TO_EXPAND:
                BosLoader.display_node(child, depth + 1)
            else:
                if child.is_named:
                    print('  ' * depth, str(child))
                    print('  ' * depth, child.text)
                else:
                    print('  ' * depth, '"', child.text, '"')

    def _run_parser(self, force_reload=False):
        if self.parser_tree is not None and not force_reload:
            return

        start_time = time.perf_counter()

        bos_language = tree_sitter.Language(tree_sitter_bos.language())
        self.parser: tree_sitter.Parser = tree_sitter.Parser(bos_language)

        self.parser_tree = self.parser.parse(self.preprocessed_file_contents.encode('utf-8'))

        end_time = time.perf_counter()
        self.log.debug('Parsing took %.2f seconds (%.2f mins)', end_time - start_time, (end_time - start_time) / 60)

        if errors := BosLoader.check_errors(self.parser_tree, self.filepath):
            for error in errors:
                BosLoader.display_node(error)
            raise ValueError('Syntax errors found in preprocessed file', errors)

    def _run_ast_conversion(self, force_reload=False):
        if self.ast_node_tree is not None and not force_reload:
            return

        ast_visitor = TreeSitterBosVisitor()
        self.ast_node_tree = ast_visitor.visit(self.parser_tree)
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
        loader = BosLoader('./example_files/Raptors/e_raptorq.bos')
        # loader.dump_preprocessed_file('./preprocessed_blah.txt')
        print(loader.load_file().model_dump_json(indent=2))


    main()
