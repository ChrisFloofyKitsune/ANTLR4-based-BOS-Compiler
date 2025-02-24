from os import PathLike

import os
import pcpp
from antlr4.CommonTokenStream import CommonTokenStream
from antlr4.InputStream import InputStream
from io import StringIO

from bos import ast_nodes
from bos.ast_visitor import ASTVisitor
from bos.gen.BosLexer import BosLexer
from bos.gen.BosParser import BosParser
from unit_value_nums import UnitValue


class BosPreprocessorWrapper:
    pcpp_preprocessor: pcpp.Preprocessor

    def __init__(self, include_paths: list[str] = None):
        self.pcpp_preprocessor = pcpp.Preprocessor()

        for def_str in [
            "TRUE 1",
            "true 1",
            "FALSE 0",
            "false 0",
            "UNKNOWN_UNIT_VALUE(val) val",
            *[f'{val.name.upper()} {val.value}' for val in UnitValue]
        ]:
            self.pcpp_preprocessor.define(def_str)

        if include_paths is not None:
            for include_path in include_paths:
                self.pcpp_preprocessor.add_path(include_path)

    def process_text(self, text: str) -> str:
        self.pcpp_preprocessor.parse(text)
        output = StringIO()
        self.pcpp_preprocessor.write(output)
        return output.getvalue()


def load_bos_file(bos_file_path: str | PathLike[str], include_paths: str | PathLike[str] = None) -> ast_nodes.File:

    with open(bos_file_path, 'rt', encoding='utf8') as f:
        processed = preprocess_bos_file(
            f.read(),
            include_paths,
            bos_file_path
        )

        return parse_preprocessed_bos_file(processed)


def preprocess_bos_file(
    bos_file_text: str,
    include_paths: list[str | PathLike[str]] = None,
    source_path: str | PathLike[str] = None,
) -> str:
    preproc = pcpp.Preprocessor()
    for def_str in [
        "TRUE 1",
        "true 1",
        "FALSE 0",
        "false 0",
        "UNKNOWN_UNIT_VALUE(val) val",
        *[f'{val.name.upper()} {val.value}' for val in UnitValue]
    ]:
        preproc.define(def_str)

    if include_paths is not None:
        for include_path in include_paths:
            preproc.add_path(os.fspath(include_path))

    preproc.parse(bos_file_text, source_path)
    output = StringIO()
    preproc.write(output)

    return output.getvalue()


def parse_preprocessed_bos_file(bos_file_text: str):
    lexer = BosLexer(InputStream(bos_file_text))
    token_stream = CommonTokenStream(lexer)
    parser = BosParser(token_stream)
    token_tree = parser.file_()

    ast_visitor = ASTVisitor()
    return ast_visitor.visitFile(token_tree)


if __name__ == '__main__':
    print(load_bos_file('./example_files/Units/legcom.bos').model_dump())
