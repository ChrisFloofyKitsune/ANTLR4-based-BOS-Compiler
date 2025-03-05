import logging
from pathlib import Path

import bos.ast_nodes as nodes
from bos.bos_loader import BosLoader
from cob.compiler.cob_compiler import CobCompiler


def __main(file_node: nodes.File):
    compiler = CobCompiler(raise_exception_on_unhandled_node=False)
    cob_file = compiler.compile_file_ast(file_node)
    serialized_data = cob_file.to_bytes()
    
    with open('../example_files/Units/legcom.cob', 'rb') as file:
        byte_data = file.read()

    with open('./legcom_recompiled.cob', 'wb') as file:
        file.write(serialized_data)

    if byte_data != serialized_data:
        print("Byte data mismatch found:")
        if len(byte_data) != len(serialized_data):
            print(f"Length mismatch: original {len(byte_data)} != serialized {len(serialized_data)}")
        for i, (original_byte, serialized_byte) in enumerate(zip(byte_data, serialized_data)):
            if original_byte != serialized_byte:
                print(f"Byte {hex(i)}: original {original_byte} ({hex(original_byte)}) != serialized {serialized_byte} ({hex(serialized_byte)})")
    else:
        print("Byte data matches.")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    loader = BosLoader('../../bos/example_files/Units/legcom.bos', enable_constant_folding=True)
    preproc_dir = Path('preprocessed')
    preproc_dir.mkdir(exist_ok=True)
    loader.dump_preprocessed_file(preproc_dir)
    __main(loader.load_file())
