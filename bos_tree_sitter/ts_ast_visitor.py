import operator
from functools import singledispatchmethod, update_wrapper, reduce
from typing import Any, ClassVar

import tree_sitter
import tree_sitter_bos

from bos import ast_nodes


class value_dispatch:
    def __init__(self, func):
        if not callable(func) and not hasattr(func, "__get__"):
            raise TypeError(f"{func!r} is not callable or a descriptor")

        self.dispatch_table = {}
        self.func = func

    def register(self, value):
        def decorator(func):
            if not callable(func) and not hasattr(func, "__get__"):
                raise TypeError(f"{func!r} is not callable or a descriptor")

            self.dispatch_table[value] = func
            return func

        return decorator

    def __get__(self, obj, cls=None):
        def _do_call(call, *args, **kwargs):
            if hasattr(call, '__get__'):
                return call.__get__(obj, cls)(*args, **kwargs)
            return call(*args, **kwargs)

        def _method(value, *args, **kwargs):
            method = self.dispatch_table.get(value, None)
            if method is None:
                return _do_call(self.func, value, *args, **kwargs)
            return _do_call(method, *args, **kwargs)

        _method.register = self.register
        _method.dispatch_table = self.dispatch_table
        update_wrapper(_method, self.func)
        return _method


_bos_lang = tree_sitter.Language(tree_sitter_bos.language())


class TreeSitterBosVisitor:
    super_to_subtype_map: ClassVar[dict[str, tuple[str, ...]]] = {
        _bos_lang.node_kind_for_id(st): tuple(map(_bos_lang.node_kind_for_id, _bos_lang.subtypes(st)))
        for st in _bos_lang.supertypes
    }

    sub_to_supertype_map: ClassVar[dict[str, str]] = {
        subtype: supertype
        for supertype, subtypes in super_to_subtype_map.items()
        for subtype in subtypes
    }

    @singledispatchmethod
    def visit(self, obj: Any) -> ast_nodes.ASTNode | list[ast_nodes.ASTNode]:
        raise NotImplementedError(f'visit not implemented for object {repr(obj)}')

    @visit.register
    def _visit_node(self, node: tree_sitter.Node):
        if (supertype := self.sub_to_supertype_map.get(node.type)) and supertype in self.visit_node_type.dispatch_table:
            return self.visit_node_type(supertype, node)

        return self.visit_node_type(node.type, node)

    @visit.register
    def _visit_list(self, items: list):
        results = (self.visit(item) for item in items if item)
        return [r for r in results if r]

    @visit.register
    def _visit_tree(self, tree: tree_sitter.Tree):
        return self.visit_node_type(tree.root_node.type, tree.root_node)

    @value_dispatch
    def visit_node_type(self, node_type: str, node: tree_sitter.Node):
        if node.is_extra:
            return None

        if not node.is_named:
            return node.text.decode('utf-8').strip()

        if node.child_count == 0:
            return ast_nodes.UndefNode(contents=node.text.decode('utf-8').strip(), name=node_type, parser_node=node)

        result = []
        for index, child in enumerate(node.children):
            if field_name := node.field_name_for_child(index):
                result.append({field_name: self.visit(child)})
            elif child.is_named:
                result.append(self.visit(child))

        result = [r for r in result if r]

        if len(result) == 0:
            return None
        elif len(result) == 1:
            return ast_nodes.UndefNode(contents=result[0], name=node_type, parser_node=node)

        if all(isinstance(r, dict) for r in result):
            result = reduce(operator.__ior__, result, {})
        return ast_nodes.UndefNode(contents=result, name=node_type, parser_node=node)

    @visit_node_type.register('constant')
    def _visit_linear_constant(self, node: tree_sitter.Node):
        return ast_nodes.Constant(node.text.decode('utf-8'), parser_node=node)

    @visit_node_type.register('axis')
    def _visit_axis(self, node: tree_sitter.Node):
        return ast_nodes.Axis(axis=ast_nodes.AxisEnum.from_str(node.text.decode('utf-8')), parser_node=node)

    @visit_node_type.register('parenthesized_expression')
    def _visit_parenthesized_expression(self, node: tree_sitter.Node):
        return self.visit(node.named_child(0))

    @visit_node_type.register('compound_statement')
    def _visit_compound_statement(self, node: tree_sitter.Node):
        return ast_nodes.StatementBlock(statements=self.visit(node.named_children), parser_node=node)

    @visit_node_type.register('func_name')
    def _visit_func_name(self, node: tree_sitter.Node):
        return ast_nodes.FuncName(name=node.text.decode('utf-8'), parser_node=node)

    @visit_node_type.register('function_declaration')
    def _visit_function_declaration(self, node: tree_sitter.Node):
        name_node = node.child_by_field_name('name')
        args_nodes = node.children_by_field_name('arg')

        return ast_nodes.FuncDeclaration(
            name=self.visit(name_node),
            args=[ast_nodes.ArgName(name=arg.text.decode('utf-8'), parser_node=arg) for arg in args_nodes],
            block=self.visit(node.child_by_field_name('body')),
            parser_node=node
        )

    @visit_node_type.register('keyword_statement')
    def _visit_keyword_statement(self, node: tree_sitter.Node):
        result = self.visit_node_type(node.type, node)
        if isinstance(result, ast_nodes.UndefNode):
            result = result.contents

        return ast_nodes.UndefNode(
            contents=result,
            name='keyword__' + node.type, parser_node=node
        )

    @visit_node_type.register('piece_name')
    def _visit_piece_name(self, node: tree_sitter.Node):
        return ast_nodes.PieceName(name=node.text.decode('utf-8'), parser_node=node)

    @visit_node_type.register('piece_declaration')
    def _visit_piece_declaration(self, node: tree_sitter.Node):
        name_nodes = node.children_by_field_name('name')

        return ast_nodes.PieceDeclaration(
            names=[self.visit(name) for name in name_nodes],
            parser_node=node
        )

    @visit_node_type.register('var_name')
    def _visit_var_name(self, node: tree_sitter.Node):
        return ast_nodes.VarName(name=node.text.decode('utf-8'), parser_node=node)

    @visit_node_type.register('static_var_declaration')
    def _visit_static_var_declaration(self, node: tree_sitter.Node):
        name_nodes = node.children_by_field_name('name')

        return ast_nodes.StaticVarDeclaration(
            names=[self.visit(name) for name in name_nodes],
            parser_node=node
        )

