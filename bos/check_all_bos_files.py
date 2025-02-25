import os.path

import sys
from pathlib import Path

from bos.bos_loader import BosLoader


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
            if 'preprocessed' in bos_filepath:
                continue

            try:
                filepath = root.joinpath(bos_filepath)
                print(f'======== PARSING: {filepath} =============', flush=True)

                loader = BosLoader(filepath, [examples_dir])
                loader.dump_preprocessed_file(preprocessed_dir)
                file_ast = loader.load_file()
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
