from pathlib import Path

import bos.ast_nodes as nodes
from bos.bos_loader import BosLoader
from cob.opcodes import CobOpCode
from cob.compiler.cob_compiler import CobCompiler


def __main(file_node: nodes.File):
    compiler = CobCompiler(raise_exception_on_unhandled_node=False)
    compiler._handle_node(file_node)
    code = compiler.code
    valid_op_codes = set(CobOpCode)
    print(compiler.function_code_indices)
    print([CobOpCode(val).name if (val in valid_op_codes) else val for val in code])


if __name__ == '__main__':
    loader = BosLoader('../../bos/example_files/Units/legcom.bos')
    preproc_dir = Path('preprocessed')
    preproc_dir.mkdir(exist_ok=True)
    loader.dump_preprocessed_file(preproc_dir)
    __main(loader.load_file())
