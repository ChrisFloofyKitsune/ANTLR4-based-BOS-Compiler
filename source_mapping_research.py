import itertools
import logging
import pathlib
import re
from typing import Protocol

import colorama
from antlr4 import InputStream, CommonTokenStream

from bos.ast_visitor import ASTVisitor
from bos.bos_loader import BosLoader
from bos.bos_preprocessor import BosPreprocessor
from bos.gen.BosLexer import BosLexer
from bos.gen.BosParser import BosParser

log = logging.getLogger(__name__)


class PcppToken(Protocol):
    value: str
    type: str
    lexpos: int
    lineno: int
    expanded_from: list[str]
    source: str


def __main():
    source_path = pathlib.PurePosixPath('./bos/example_files/Units/legaap.bos')
    with open(source_path, 'rt', encoding='utf8') as f:
        file_text = f.read()

    preproc = BosPreprocessor()
    preprocessed_text, output_text, chunks = preproc.process_file(file_text, source_path)
    source_ranges = []
    pp_pos, output_pos = 0, 0
    for chunk in chunks:
        source_ranges.append(
            (
                range(pp_pos, pp_pos + len(chunk.text)),
                range(output_pos, output_pos + len(chunk.original_text))
            )
        )
        pp_pos += len(chunk.text)
        output_pos += len(chunk.original_text)

    bos_lexer = BosLexer(InputStream(preprocessed_text))
    token_stream = CommonTokenStream(bos_lexer)
    bos_parser = BosParser(token_stream)
    file_parser_ast = bos_parser.file_()

    ast_visitor = ASTVisitor()
    file_ast = ast_visitor.visitFile(file_parser_ast)

    bos_loader = BosLoader(source_path)
    loader_file_node_tree = bos_loader.load_file()

    assert file_ast == loader_file_node_tree, 'ASTs do not match'
    print('ASTs match')

    preproc_text_to_print = output_text_to_print = ''

    colorama.just_fix_windows_console()

    colors = itertools.cycle(
        [
            colorama.Fore.RED,
            colorama.Fore.GREEN,
            colorama.Fore.YELLOW,
            colorama.Fore.BLUE,
            colorama.Fore.MAGENTA,
            colorama.Fore.CYAN,
        ]
    )

    def count_visible_characters(text):
        """Counts the number of visible characters in a string, 
        ignoring ANSI color codes.
        """
        clean_text = re.sub(r'\x1b\[[0-9;]*m', '', text)
        return len(clean_text)

    for source_range in source_ranges:
        preproc_range, output_range = source_range

        color = next(colors)

        preproc_text_to_print += color + preprocessed_text[preproc_range.start:preproc_range.stop]
        output_text_to_print += color + output_text[output_range.start:output_range.stop]

        # while there are lines to print, keep printing
        while '\n' in preproc_text_to_print or '\n' in output_text_to_print:
            if '\n' not in preproc_text_to_print:
                preproc_line = '>>>>'
            else:
                newline_index = preproc_text_to_print.index('\n')
                preproc_line = preproc_text_to_print[:newline_index + 1].rstrip().replace('\t', '    ')
                preproc_text_to_print = preproc_text_to_print[newline_index + 1:]

            if '\n' not in output_text_to_print:
                output_line = '<<<<'
            else:
                newline_index = output_text_to_print.index('\n')
                output_line = output_text_to_print[:newline_index + 1].rstrip().replace('\t', '    ')
                output_text_to_print = output_text_to_print[newline_index + 1:]

            preproc_line_extra_size = len(preproc_line) - count_visible_characters(preproc_line)

            print(
                '{:{psize}} | {}'.format(
                    preproc_line[:130],
                    output_line[:130],
                    psize=130 + preproc_line_extra_size,
                )
            )


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='[%(levelname)s] (%(name)s:%(lineno)d %(funcName)s) %(message)s')
    __main()
