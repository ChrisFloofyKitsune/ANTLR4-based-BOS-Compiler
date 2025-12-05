import pathlib
import sys
from typing import Self, NamedTuple

from tree_sitter import Node as TSNode

from bos.ast_nodes import ASTNode
from util.ts_util import nearest_previous


class CodeLocation(NamedTuple):
    source_file: str
    start_line: int
    start_column: int
    end_line: int
    end_column: int

    @classmethod
    def from_node(cls, node: ASTNode | TSNode | None, source_file: str = None) -> Self | None:
        if isinstance(node, ASTNode):
            node = node.parser_node

        if not isinstance(node, TSNode):
            return None

        start_line, start_column = node.start_point
        end_line, end_column = node.end_point

        line_offset = 0

        if preproc_line_node := nearest_previous(node, "preproc_line"):
            lineno = int(preproc_line_node.child_by_field_name('lineno').text.decode('utf-8'))
            line_offset = lineno - preproc_line_node.start_point[0] - 1
            if filename_node := preproc_line_node.child_by_field_name('filename'):
                source_file = filename_node.named_child(0).text.decode('utf-8')

        return cls(source_file, start_line + line_offset, start_column, end_line + line_offset, end_column)

    def __str__(self) -> str:


        return f'File "{str(pathlib.Path(self.source_file).absolute())}" line {self.start_line}'

    def __repr__(self) -> str:
        return (
            f"CodeLocation(source_file={self.source_file!r}, start_line={self.start_line}, "
            f"start_column={self.start_column}, end_line={self.end_line}, end_column={self.end_column})"
        )

if __name__ == "__main__":
    def main():
        from tree_sitter_bos import language
        from tree_sitter import Language, Parser, Query, QueryCursor
        from bos.ast_nodes import Constant
        bos_lang = Language(language())
        parser = Parser(bos_lang)

        test_data = \
            b"""
            funcName(a, b, c, d) {
                a = 10;
                #line 1 "source_file.bos"
                b = 20;
                #line 10 "other_file.h"
                c = 30;
                #line 20 "source_file.bos"
                d = 10;
                d = 20;
                d = 30;
                if (a == 10) {
                    #line 30 "other_file.h"
                    b = 20;               // 30
                    if (TRUE) {           // 31
                        if (TRUE) {       // 32
                            a = 1;        // 33
                            b = 2;        // 34
                            c = 3;        // 35
                        }
                    }
                }
            }
            """
        tree = parser.parse(test_data)
        query = Query(bos_lang, "(assign_statement) @target")
        q_cursor = QueryCursor(query)
        for _, thing in q_cursor.matches(tree.root_node):
            node = thing['target'][0]
            loc = CodeLocation.from_node(node, "blah.bos")
            loc2 = CodeLocation.from_node(Constant(0, parser_node=node), "blah.bos")
            print(loc)
            assert loc == loc2


    main()
