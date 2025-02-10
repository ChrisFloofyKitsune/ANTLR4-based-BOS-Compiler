import os.path
import sys
from io import StringIO
from pathlib import Path

import pcpp
from antlr4 import CommonTokenStream, InputStream

from bos.gen.BosLexer import BosLexer
from bos.gen.BosParser import BosParser

# yoinked from https://github.com/beyond-all-reason/BARScriptCompiler/blob/main/bos2cob_py3.py#L1455
class MyPreprocessor(pcpp.Preprocessor):
    def __init__(self, input_string):
        super().__init__()
        # Use StringIO to simulate file input and output
        self.line_directive = None
        self.input = input_string
        self.output = StringIO()

    def preprocess(self):
        # Parse and preprocess the input

        # defaults = '#define TRUE 1\r\n#define FALSE 0\r\n#define UNKNOWN_UNIT_VALUE \r\n'
        self.define("TRUE 1")
        self.define("FALSE 0")
        self.define("UNKNOWN_UNIT_VALUE")
        self.parse(self.input)
        self.write(self.output)
        # Return the preprocessed output as a string
        return self.output.getvalue()

    def on_error(self, file, line, msg):
        print(f"Preprocessor error in file: {file} at line: {line} Error: {msg}")
        return super().on_error(file, line, msg)()


def main():
    examples_dir = Path('./example_files')
    preprocessed_dir = Path('./preprocessed')
    preprocessed_dir.mkdir(exist_ok=True)

    for root, dirs, files in os.walk(examples_dir):
        root = Path(root)
        bos_files = [f for f in files if f.endswith('.bos')]
        print(
            f"""
______________________________________________
{root}
----------------------------------------------
""",
            flush=True
        )
        for bos_filepath in bos_files:
            try:
                filepath = root.joinpath(bos_filepath)
                with open(filepath, 'r', encoding='utf-8') as bos_file:
                    content = bos_file.read()

                print(f'======== PARSING: {filepath} =============', flush=True)

                preproc = MyPreprocessor(content)
                preproc.add_path(examples_dir)
                preproc.add_path(os.path.dirname(os.path.abspath(filepath)))
                content = preproc.preprocess()

                with open(
                    preprocessed_dir.joinpath(bos_filepath).with_suffix('.pcpp').resolve(),
                    'w',
                    encoding='utf-8'
                ) as pcpp_file:
                    pcpp_file.write(content)

                parse_bos_file(content)
            except BaseException as err:
                print(f'Error parsing {bos_filepath}')
                print(err)
                continue


def parse_bos_file(data: str):

    input_stream = InputStream(data)
    lexer = BosLexer(input_stream)
    # lexer.addErrorListener(DiagnosticErrorListener())
    tokens = CommonTokenStream(lexer)
    parser = BosParser(tokens)
    # parser.addErrorListener(DiagnosticErrorListener())

    sys.stdout.flush()

    return parser.file_()


if __name__ == '__main__':
    main()
