import os
import statistics
import time
from itertools import pairwise
from pathlib import Path

import tree_sitter
import tree_sitter_bos

from bos.bos_preprocessor import BosPreprocessor
from bos_tree_sitter.ts_ast_visitor import TreeSitterBosVisitor


def main():
    bos_language = tree_sitter.Language(tree_sitter_bos.language())
    bos_files_dir = Path('../bos/example_files')
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


def walk_files(path: Path, extensions: list[str]):
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
    with open('../bos/example_files/Units/legcom.bos', 'rb') as f:
        data = f.read()

    bos_lang = tree_sitter.Language(tree_sitter_bos.language())
    parser = tree_sitter.Parser(bos_lang)
    tree = parser.parse(data)

    visitor = TreeSitterBosVisitor()
    print(visitor.visit(tree).model_dump_json(indent=2))

if __name__ == "__main__":
    # main()
    # main2()
    main3()
