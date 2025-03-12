import operator
import warnings
from functools import singledispatchmethod, reduce
from typing import Any, ClassVar

import tree_sitter
import tree_sitter_bos

from bos import ast_nodes
from value_dispatch import ValueDispatch

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

    keyword_map = {
        'call-script': ast_nodes.Keyword.CALL_SCRIPT,
        'start-script': ast_nodes.Keyword.START_SCRIPT,

        'signal': ast_nodes.Keyword.SIGNAL,
        'set-signal-mask': ast_nodes.Keyword.SET_SIGNAL_MASK,

        'sleep': ast_nodes.Keyword.SLEEP,

        'set': ast_nodes.Keyword.SET,
        'get': ast_nodes.Keyword.GET,

        'spin': ast_nodes.Keyword.SPIN,
        'stop-spin': ast_nodes.Keyword.STOP_SPIN,

        'turn': ast_nodes.Keyword.TURN,
        'move': ast_nodes.Keyword.MOVE,

        'wait-for-turn': ast_nodes.Keyword.WAIT_FOR_TURN,
        'wait-for-move': ast_nodes.Keyword.WAIT_FOR_MOVE,

        'hide': ast_nodes.Keyword.HIDE,
        'show': ast_nodes.Keyword.SHOW,

        'emit-sfx': ast_nodes.Keyword.EMIT_SFX,
        'explode': ast_nodes.Keyword.EXPLODE,

        'attach-unit': ast_nodes.Keyword.ATTACH_UNIT,
        'drop-unit': ast_nodes.Keyword.DROP_UNIT,

        # effectively removed from the language, these do nothing
        # 'cache': ast_nodes.Keyword.CACHE,
        # 'dont-cache': ast_nodes.Keyword.DONT_CACHE,
        # 'dont-shadow': ast_nodes.Keyword.DONT_SHADE,
        # 'dont-shade': ast_nodes.Keyword.DONT_SHADE,
    }

    operator_map = {
        '+': ast_nodes.ExpressionOp.ADD,
        '-': ast_nodes.ExpressionOp.MINUS,
        '*': ast_nodes.ExpressionOp.MULT,
        '/': ast_nodes.ExpressionOp.DIV,
        '%': ast_nodes.ExpressionOp.MOD,
        '^^': ast_nodes.ExpressionOp.LOGICAL_XOR,
        '||': ast_nodes.ExpressionOp.LOGICAL_OR,
        '&&': ast_nodes.ExpressionOp.LOGICAL_AND,
        '!': ast_nodes.ExpressionOp.LOGICAL_NOT,
        '^': ast_nodes.ExpressionOp.BITWISE_XOR,
        '|': ast_nodes.ExpressionOp.BITWISE_OR,
        '&': ast_nodes.ExpressionOp.BITWISE_AND,
        '==': ast_nodes.ExpressionOp.COMP_EQUAL,
        '!=': ast_nodes.ExpressionOp.COMP_NOT_EQUAL,
        '>': ast_nodes.ExpressionOp.COMP_GREATER,
        '>=': ast_nodes.ExpressionOp.COMP_GREATER_EQUAL,
        '<=': ast_nodes.ExpressionOp.COMP_LESS_EQUAL,
        '<': ast_nodes.ExpressionOp.COMP_LESS,
    }

    @singledispatchmethod
    def visit(self, obj: Any) -> ast_nodes.ASTNode | list[ast_nodes.ASTNode]:
        raise NotImplementedError(f'visit not implemented for object {repr(obj)}')

    @visit.register
    def _visit_node(self, node: tree_sitter.Node):
        target_type = node.type
        while (
                target_type not in self.visit_node_type.dispatch_table
                and target_type in self.sub_to_supertype_map
                and self.sub_to_supertype_map[target_type] in self.visit_node_type.dispatch_table
        ):
            target_type = self.sub_to_supertype_map[target_type]

        return self.visit_node_type(target_type, node)

    @visit.register
    def _visit_list(self, items: list):
        results = (self.visit(item) for item in items if item)
        return [r for r in results if r]

    @visit.register
    def _visit_tree(self, tree: tree_sitter.Tree):
        return self.visit_node_type(tree.root_node.type, tree.root_node)

    @ValueDispatch
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

    @visit_node_type.register('call_script_statement')
    def _visit_call_script_statement(self, node: tree_sitter.Node):
        func_name = self.visit(node.child_by_field_name('function'))
        args = self.visit(node.child_by_field_name('arguments').named_children)

        return ast_nodes.CallStatement(
            keyword=ast_nodes.Keyword.CALL_SCRIPT,
            args=[func_name] + args,
            parser_node=node
        )

    @visit_node_type.register('start_script_statement')
    def _visit_start_script_statement(self, node: tree_sitter.Node):
        func_name = self.visit(node.child_by_field_name('function'))
        args = self.visit(node.child_by_field_name('arguments').named_children)

        return ast_nodes.StartStatement(
            keyword=ast_nodes.Keyword.START_SCRIPT,
            args=[func_name] + args,
            parser_node=node
        )

    @visit_node_type.register('keyword_statement')
    def _visit_keyword_statement(self, node: tree_sitter.Node):
        keyword = node.child_by_field_name('keyword').text.decode('utf-8')
        if keyword not in self.keyword_map:
            return None

        args = self.visit(node.named_children)

        return ast_nodes.KeywordStatement(
            keyword=self.keyword_map[keyword],
            args=args,
            parser_node=node,
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

    @visit_node_type.register('unary_expression')
    def _visit_unary_expression(self, node: tree_sitter.Node):
        operand = self.visit(node.child_by_field_name('argument'))
        op = self.operator_map[node.child_by_field_name('operator').type]

        return ast_nodes.UnaryExpression(operand=operand, op=op, parser_node=node)

    @visit_node_type.register('binary_expression')
    def _visit_binary_expression(self, node: tree_sitter.Node):
        left = self.visit(node.child_by_field_name('left'))
        right = self.visit(node.child_by_field_name('right'))
        op = self.operator_map.get(node.child_by_field_name('operator').type, None)
        if op is None:
            op_text = node.child_by_field_name('operator').type
            warnings.warn(f'Could not find operator for binary expression {op_text}', UserWarning)
            return None

        return ast_nodes.BinaryExpression(operand1=left, operand2=right, op=op, parser_node=node)

    @visit_node_type.register('var_name_term')
    def _visit_var_name_term(self, node: tree_sitter.Node):
        return ast_nodes.VarNameTerm(var_name=self._visit_var_name(node), parser_node=node)

    @visit_node_type.register('source_file')
    def _visit_source_file(self, node: tree_sitter.Node):
        declarations = self.visit(node.named_children)
        declarations = [d for d in declarations if not isinstance(d, ast_nodes.UndefNode)]
        return ast_nodes.File(declarations=declarations, parser_node=node)

    @visit_node_type.register('if_statement')
    def _visit_if_statement(self, node: tree_sitter.Node):
        condition = self.visit(node.child_by_field_name('condition'))
        then_block = self.visit(node.child_by_field_name('then'))
        if else_node := node.child_by_field_name('else'):
            else_block = self.visit(else_node)
        else:
            else_block = None

        return ast_nodes.IfStatement(
            condition=condition,
            then_block=then_block,
            else_block=else_block,
            parser_node=node
        )

    @visit_node_type.register('while_statement')
    def _visit_while_statement(self, node: tree_sitter.Node):
        condition = self.visit(node.child_by_field_name('condition'))
        block = self.visit(node.child_by_field_name('body'))

        return ast_nodes.WhileStatement(
            condition=condition,
            block=block,
            parser_node=node
        )

    @visit_node_type.register('get_term')
    def _visit_get_term(self, node: tree_sitter.Node):
        return ast_nodes.GetTerm(get_call=self.visit(node.named_child(0)), parser_node=node)

    @visit_node_type.register('get_call')
    def _visit_get_call(self, node: tree_sitter.Node):
        value_index = self.visit(node.child_by_field_name('value_index'))
        args = self.visit(node.children_by_field_name('arg'))

        return ast_nodes.GetCall(
            value_idx=value_index,
            args=args,
            parser_node=node
        )

    @visit_node_type.register('rand_call')
    def _visit_rand_call(self, node: tree_sitter.Node):
        return ast_nodes.RandTerm(
            min=self.visit(node.child_by_field_name('lower_bound')),
            max=self.visit(node.child_by_field_name('upper_bound')),
        )

    @visit_node_type.register('assign_statement')
    def _visit_assign_statement(self, node: tree_sitter.Node):
        var_name_node = node.child_by_field_name('name')
        if not var_name_node:
            return self.visit(node.named_child(0))

        var_name = self.visit(var_name_node)
        value = self.visit(node.child_by_field_name('value'))

        return ast_nodes.AssignStatement(
            variable=var_name,
            expression=value,
            parser_node=node
        )

    @visit_node_type.register('increment_statement')
    def _visit_increment_statement(self, node: tree_sitter.Node):
        var_name = self.visit(node.child_by_field_name('name'))

        return ast_nodes.AssignStatement(
            variable=var_name,
            expression=ast_nodes.BinaryExpression(
                operand1=ast_nodes.VarNameTerm(var_name=var_name),
                op=ast_nodes.ExpressionOp.ADD,
                operand2=ast_nodes.Constant(1)
            ),
            parser_node=node
        )

    @visit_node_type.register('decrement_statement')
    def _visit_decrement_statement(self, node: tree_sitter.Node):
        var_name = self.visit(node.child_by_field_name('name'))

        return ast_nodes.AssignStatement(
            variable=var_name,
            expression=ast_nodes.BinaryExpression(
                operand1=ast_nodes.VarNameTerm(var_name=var_name),
                op=ast_nodes.ExpressionOp.MINUS,
                operand2=ast_nodes.Constant(1)
            ),
            parser_node=node
        )

    @visit_node_type.register('var_statement')
    def _visit_var_statement(self, node: tree_sitter.Node):
        return ast_nodes.VarStatement(
            vars=self.visit(node.named_children),
            parser_node=node
        )

    @visit_node_type.register('return_statement')
    def _visit_return_statement(self, node: tree_sitter.Node):
        if node.named_child(0) is None:
            return ast_nodes.ReturnStatement(expression=None, parser_node=node)

        return ast_nodes.ReturnStatement(
            expression=self.visit(node.named_child(0)),
            parser_node=node
        )