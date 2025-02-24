import os.path

import sys
from pathlib import Path

from bos import bos_loader


# from bos.ast.ast_visitor import ASTVisitor


def main():
    examples_dir = Path('./example_files')
    preprocessed_dir = Path('./preprocessed')
    preprocessed_dir.mkdir(exist_ok=True)

    for root, _dirs, files in os.walk(examples_dir):
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

                preprocced = bos_loader.preprocess_bos_file(content, include_paths=[examples_dir], source_path=filepath)

                with open(
                    preprocessed_dir.joinpath(bos_filepath).with_suffix('.pcpp').resolve(),
                    'w',
                    encoding='utf-8'
                ) as pcpp_file:
                    pcpp_file.write(preprocced)

                file_ast = bos_loader.parse_preprocessed_bos_file(preprocced)
                format_str = 'PARSED: {} | Referenced Pieces: {} | Static Vars: {} | Functions: {}'
                print(
                    format_str.format(
                        bos_filepath,
                        sum(len(pd.names) for pd in file_ast.piece_declarations),
                        sum(len(sd.names) for sd in file_ast.static_var_declarations),
                        len(file_ast.function_declarations)
                    ), flush=True
                )
                sys.stderr.flush()
            except BaseException as err:
                print(f'Error parsing {bos_filepath}')
                print(err)
                continue


if __name__ == '__main__':
    main()
