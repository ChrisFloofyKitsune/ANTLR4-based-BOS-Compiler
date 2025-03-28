import logging
import os
import statistics
import sys
import time
from itertools import pairwise
from pathlib import Path

import tree_sitter
import tree_sitter_bos

from bos.bos_loader import BosLoader
from bos.bos_preprocessor import BosPreprocessor
from bos.ts_ast_visitor import TreeSitterBosVisitor
from cob.compiler.cob_compiler import CobCompiler
from code_error import CodeError


def main():
    bos_language = tree_sitter.Language(tree_sitter_bos.language())
    bos_files_dir = Path('example_files')
    parser = tree_sitter.Parser(bos_language)

    parse_time_stats = []
    for file in walk_files(bos_files_dir, ['.bos', '.h']):
        if process_file(file, parser, parse_time_stats):
            break

    if len(parse_time_stats) == 0:
        raise RuntimeError('No files processed')

    print('Average parse time:', statistics.mean(parse_time_stats))
    print('Total parse time:', sum(parse_time_stats))
    print('Std dev:', statistics.pstdev(parse_time_stats))
    print("Min/Max:", min(parse_time_stats), '/', max(parse_time_stats))


def walk_files(path: str | os.PathLike[str], extensions: list[str]):
    for dirpath, _, filenames in os.walk(path):
        for file in filenames:
            if Path(file).suffix in extensions:
                yield Path(dirpath).joinpath(file)

def process_file(file: Path, parser: tree_sitter.Parser, parse_time_stats: list = None):
    if 'array' in str(file):
        # these things are cursed as fuck
        return False

    # print('Processing', file)
    start_time = time.perf_counter()
    parser.reset()
    with open(file, 'rt', encoding='utf-8') as f:
        file_text = f.read()

    # bos_preprocessor = BosPreprocessor()
    # processed, source, chunks = bos_preprocessor.process_file(file_text, file, ['bos/example_files'])
    #
    # preproc_time = time.perf_counter()
    # print('Preprocessing time:', preproc_time - start_time)

    tree = parser.parse(file_text.encode('utf-8'))
    time_taken = time.perf_counter() - start_time
    # print('Parsing time:', time_taken)
    if parse_time_stats is not None:
        parse_time_stats.append(time_taken)

    if check_errors(tree, file):
        return True

    return False

def check_errors(tree: tree_sitter.Tree, file: Path):
    error_query = tree_sitter.Query(tree.language, "(ERROR) @error")
    error_query_cursor = tree_sitter.QueryCursor(error_query)

    if errors := error_query_cursor.captures(tree.root_node):
        print('\n\nErrors found in', file)
        for error in errors['error']:
            print(error.range)
            display_node(error)
        return False

    missing_query = tree_sitter.Query(tree.language, "(MISSING) @missing")
    missing_query_cursor = tree_sitter.QueryCursor(missing_query)

    # if missing := missing_query_cursor.captures(tree.root_node):
    #     print('\n\nMissing found in', file)
    #     for miss in missing['missing']:
    #         print(miss.range)
    #         display_node(miss.parent)
    #     return True

    return False

NODES_TO_EXPAND = ['function_declaration', 'compound_statement', 'while_statement', 'ERROR', 'MISSING']
def display_node(node: tree_sitter.Node, depth=0):
    print('->' * (depth+1), node.grammar_name, '<-' * (depth+1))
    for idx, child in enumerate(node.children):
        if (field_name := node.field_name_for_child(idx)) is not None:
            print('  ' * depth, '---', field_name, '---')

        if child.grammar_name in NODES_TO_EXPAND:
            display_node(child, depth+1)
        else:
            if child.is_named:
                print('  ' * depth, str(child))
                print('  ' * depth, child.text.decode('utf-8'))
            else:
                print('  ' * depth, '"', child.text.decode('utf-8'), '"')
    # print(error.parent.text.decode('utf-8'))


    # parent = error.parent
    #
    # parent_text = parent.text.decode('utf-8')
    # start_line = parent.start_point.row
    # end_line = parent.end_point.row
    #
    # error_lines = error.text.decode('utf-8').splitlines()
    # for line, line_no in zip(parent_text.splitlines(), range(start_line, end_line + 1)):
    #     print(f'#{line_no:04d}: {line}')
    #     if error.start_point.row >= line_no <= error.end_point.row:
    #         print(error_lines)

def main2():
    bos_lang = tree_sitter.Language(tree_sitter_bos.language())
    parser = tree_sitter.Parser(bos_lang)
    # tree = parser.parse(b'//')
    # node = tree.root_node.children[0]
    #
    # print(str(node), str(node.children))

    print('Node kinds:', bos_lang.node_kind_count)
    print('State count:', bos_lang.parse_state_count)

    dead_ends = set()
    state_transition_names = {}

    for node_id in range(bos_lang.node_kind_count):
        for state_id in range(bos_lang.parse_state_count):
            next_state = bos_lang.next_state(state_id, node_id)
            if next_state == 0:
                continue
            for next_node_id, next_node_name in bos_lang.lookahead_iterator(next_state):
                if bos_lang.next_state(next_state, next_node_id) == 0:
                    dead_ends.add((next_state, next_node_id))

    for node_id in range(bos_lang.node_kind_count):
        if not bos_lang.node_kind_is_named(node_id):
            continue
        completions_ingress_map = {}
        for state_id in range(bos_lang.parse_state_count):
            next_state = bos_lang.next_state(state_id, node_id)
            if next_state == 0:
                continue
            completion = tuple(n_name for n_id, n_name in bos_lang.lookahead_iterator(next_state) if not (next_state, n_id) in dead_ends)
            completions_ingress_map[completion] = completions_ingress_map.get(completion, list()) + [state_id]
        for completion, state_ids in completions_ingress_map.items():
            run_start = state_ids[0]
            ids_string = f'{state_ids[0]}'
            for prev, next_ in pairwise(state_ids):
                if prev + 1 == next_:
                    continue

                if prev == run_start:
                    ids_string += f', '
                else:
                    ids_string += f'-{prev}, '
                run_start = next_
                ids_string += f'{next_}'

            print(bos_lang.node_kind_for_id(node_id), ids_string)
            print(completion)

def main3():
    # with open('../bos/example_files/debug.h', 'rb') as f:
    #     data = f.read()

    bos_lang = tree_sitter.Language(tree_sitter_bos.language())
    parser = tree_sitter.Parser(bos_lang)
    top_path = Path('example_files/Units')

    outer_start_time = time.perf_counter()

    for file in walk_files(top_path, ['.bos']):
        if 'array' in str(file):
            continue

        if 'leg' not in str(file):
            continue

        print('Processing', file)
        data = open(file, 'rt').read()

        start_time = time.perf_counter()

        bos_preprocessor = BosPreprocessor()
        bos_preprocessor.add_path(top_path)
        preproc_text, _, _ = bos_preprocessor.process_file(data, file, [top_path])

        preproc_time = time.perf_counter()

        tree = parser.parse(preproc_text.encode('utf-8'))

        parse_time = time.perf_counter()

        visitor = TreeSitterBosVisitor()
        ast_node_tree = visitor.visit(tree)

        ast_time = time.perf_counter()

        new_bytes = None
        try:
            compiler = CobCompiler()
            new_bytes = compiler.compile_file_ast(ast_node_tree).to_bytes()
            Path('../bos_tree_sitter/compiled').mkdir(exist_ok=True)
            with open(Path('../bos_tree_sitter/compiled').joinpath(file.name).with_suffix('.cob'), 'wb') as f:
                f.write(new_bytes)
        except CodeError:
            print('file failed to compile :(')
        compile_time = time.perf_counter()
        print(
            f'Preproc time: {preproc_time - start_time:.4f}',
            f'Parse time:   {parse_time - preproc_time:.4f}',
            f'AST time:     {ast_time - parse_time:.4f}',
            f'Compile time: {compile_time - ast_time:.4f}',
            f'Total time:   {compile_time - start_time:.4f}'
        )

        if new_bytes is None:
            continue

        cob_path = Path(str(file).replace('\\bos\\', '\\cob\\').replace('.bos', '.cob'))
        if not cob_path.exists():
            print('original compiled file does not exist')
            continue

        with open(cob_path, 'rb') as f:
            old_bytes = f.read()

        if new_bytes == old_bytes:
            print("Compiled byte data matches!?!?")
        else:
            print("Byte data mismatch found between compiled files:")
            if len(old_bytes) != len(new_bytes):
                print(f"Length mismatch: old {len(old_bytes)} != new {len(new_bytes)}")
                if len(old_bytes) < len(new_bytes):
                    print(f'File size increased for {file.name}, this should not happen', file=sys.stderr)

    print('Total time:', time.perf_counter() - outer_start_time)

def main3_old__compare_new_and_old_ast(new_ast_dict, file, ast_node_tree):
        # # remove any fancy new PreprocNode stuff
        cleaned_ast = purge_preproc_nodes(new_ast_dict)

        bos_loader = BosLoader(file)
        prev_version_ast = bos_loader.load_file()
        prev_version_dict = prev_version_ast.model_dump()

        if cleaned_ast == prev_version_dict:
            print('ASTs "match"')

            try:
                compiler = CobCompiler()
                cob_file_new = compiler.compile_file_ast(ast_node_tree)
                cob_file_old = compiler.compile_file_ast(prev_version_ast)
            except CodeError:
                print('file failed to compile :(')
                return

            new_bytes = cob_file_new.to_bytes()
            old_bytes = cob_file_old.to_bytes()

            Path('../bos_tree_sitter/compiled').mkdir(exist_ok=True)
            cob_file_new.save_to_file(Path(
                '../bos_tree_sitter/compiled').joinpath(Path(file.name).with_suffix(".new_parser.cob")))
            cob_file_old.save_to_file(Path(
                '../bos_tree_sitter/compiled').joinpath(Path(file.name).with_suffix(".old_parser.cob")))

            if new_bytes != old_bytes:
                print("Byte data mismatch found between compiled files:")
                if len(old_bytes) != len(new_bytes):
                    print(f"Length mismatch: old {len(old_bytes)} != new {len(new_bytes)}")
                for i, (original_byte, serialized_byte) in enumerate(zip(old_bytes, new_bytes)):
                    if original_byte != serialized_byte:
                        print(
                            f"Byte {hex(i):>6}: old {original_byte} ({hex(original_byte)}) != new {serialized_byte} ({hex(serialized_byte)})")
                return
            else:
                print("Compiled byte data matches.")
        else:
            print('ASTs do not match')

def purge_preproc_nodes(ast_dict):
    new_values = {}
    for key, value in ast_dict.items():
        if 'Preproc' in key:
            continue

        if isinstance(value, dict):
            value = purge_preproc_nodes(value)
            if value is not None and len(value) > 0:
                new_values[key] = purge_preproc_nodes(value)
        elif isinstance(value, list):
            list_values = []
            for item in value:
                if isinstance(item, dict):
                    list_values.append(purge_preproc_nodes(item))
                else:
                    list_values.append(item)
            new_values[key] = [v for v in list_values if v]
        else:
            new_values[key] = value
    return new_values

if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s %(filename)s %(funcName)s %(lineno)s: %(message)s', level=logging.INFO)
    # main()
    # main2()
    main3()
