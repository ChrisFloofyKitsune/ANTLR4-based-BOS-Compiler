from itertools import chain, repeat
import logging
from array import array
from copy import copy
from functools import singledispatchmethod
from itertools import islice

from bos import ast_nodes as nodes
from bos.ast_nodes import preproc_nodes
from bos.ast_nodes import Keyword
from cob_compiler.cob_file import CobFile
from cob_compiler.name_registry import NameRegistry, NameType
from cob_compiler.opcodes import CobOpCode
from code_error import CodeError
from code_location import CodeLocation

log = logging.getLogger(__name__)


class NodeNameRegistry(NameRegistry[nodes.NameNode]):
    def on_name_missing(self, name):
        raise CodeError(f'name "{str(name)}" has not been defined', CodeLocation.from_node(name.parser_node))

    # def on_name_collision(self, name: nodes.NameNode, name_type: NameType, existing_type: NameType):
    #     if name_type == existing_type and name_type in (NameType.STATIC_VAR, NameType.PIECE):
    #         log.warning(
    #             'Skipping duplicate declaration of global name %s "%s". Location: %s',
    #             name_type.description,
    #             str(name),
    #             CodeLocation.from_node(name.parser_node),
    #         )
    #         return
    #
    #     raise CodeError(
    #         f'invalid declaration of {name_type.description} "{str(name)}", '
    #         f"name is already being used by a {existing_type.description} declaration",
    #         CodeLocation.from_node(name.parser_node),
    #     )


class CobCompiler:
    def __init__(self, /, raise_exception_on_unhandled_node=True):
        self.raise_exception_on_unhandled_node = raise_exception_on_unhandled_node

        self.name_registry: NodeNameRegistry | None = None
        self.function_code_indices: dict[nodes.FuncName, int] | None = None
        self.code: array | None = None

    def compile_file_ast(self, file_node: nodes.File):
        self.handle_node(file_node)

        return CobFile(
            static_var_count=len(self.name_registry.get_name_strings(NameType.STATIC_VAR)),
            code=copy(self.code),
            piece_names=self.name_registry.get_name_strings(NameType.PIECE),
            function_map={func_name.name: idx for func_name, idx in self.function_code_indices.items()},
        )

    def _load_global_names(self, file_node: nodes.File):
        assert self.name_registry is not None, "name_registry has not been initialized!"
        assert len(self.name_registry) == 0, "names have already been loaded!"

        for declaration in file_node.declarations:
            if isinstance(declaration, nodes.PieceDeclaration):
                for piece_name in declaration:
                    self.name_registry.register(piece_name, NameType.PIECE)
            elif isinstance(declaration, nodes.StaticVarDeclaration):
                for var_name in declaration:
                    self.name_registry.register(var_name, NameType.STATIC_VAR)
            elif isinstance(declaration, nodes.FuncDeclaration):
                self.name_registry.register(declaration.name, NameType.FUNCTION)
            else:
                raise ValueError("Unable to register names for object", declaration)

    def handle_node(self, node: nodes.ASTNode):
        try:
            self._handle_node(node)
        except Exception as e:
            note = repr(node)
            if len(note) > 200:
                note = note[:200] + "..."
            e.add_note("Error happened in node: " + note)
            raise

    @singledispatchmethod
    def _handle_node(self, node: nodes.ASTNode):
        if self.raise_exception_on_unhandled_node:
            raise NotImplementedError(
                f"INTERNAL COMPILER ERROR: Node of type {node.node_name} does not have a handler!"
            )
        log.debug(f"TODO: handle %s AST Node", node.node_name)
        self.code.append(CobOpCode.BAD_OP_PLACEHOLDER)

    @_handle_node.register(list)
    def _handle_node__list(self, node_list: list[nodes.ASTNode]):
        for node in node_list:
            self.handle_node(node)

    @_handle_node.register(nodes.PieceDeclaration)
    @_handle_node.register(nodes.StaticVarDeclaration)
    @_handle_node.register(preproc_nodes.PreprocNode)
    def _handle_node__noop(self, *_, **__): ...

    @_handle_node.register
    def _handle_node__file(self, file_node: nodes.File):
        self.name_registry = NodeNameRegistry()
        self.function_code_indices = dict()
        self.code = array("l")

        self._load_global_names(file_node)
        for decl in file_node:
            self.handle_node(decl)

    @_handle_node.register
    def _handle_node__func_declaration(self, func_decl: nodes.FuncDeclaration):
        self.name_registry.clear_local_names()
        self.function_code_indices[func_decl.name] = len(self.code)

        for arg in func_decl.args:
            self.name_registry.register(arg, NameType.ARGUMENT)
            self.code.append(CobOpCode.CREATE_LOCAL_VAR)

        self.handle_node(func_decl.block)

        # add return at end of it's missing
        if not (func_decl.block and isinstance(func_decl.block[-1], nodes.ReturnStatement)):
            self.code.extend([CobOpCode.PUSH_CONSTANT, 0, CobOpCode.RETURN])

    @_handle_node.register
    def _handle_node__statement_block(self, block: nodes.StatementBlock):
        for statement in block:
            self.handle_node(statement)

    # ==== statements ====
    # keywordStatement
    #   callStatement
    #   startStatement
    # varStatement
    # ifStatement
    # whileStatement
    # assignStatement
    # returnStatement

    @_handle_node.register
    def _handle_node__keyword_statement(self, keyword_statement: nodes.KeywordStatement):
        keyword = keyword_statement.keyword
        if keyword == Keyword.PLAY_SOUND:
            raise NotImplementedError("PLAY_SOUND statement is not supported")

        # Get call done purely for side effects, remove the result from the stack
        if keyword == Keyword.GET:
            self.handle_node(keyword_statement.args[0])
            self.code.append(CobOpCode.POP_STACK)
            return

        args = keyword_statement.args
        kw_op_code = CobOpCode.from_keyword(keyword_statement.keyword)
        if keyword in (Keyword.MOVE, Keyword.TURN) and (
            args[-1] is None or len(args) == CobOpCode.MOVE_NOW.num_params
        ):
            match keyword:
                case Keyword.MOVE:
                    kw_op_code = CobOpCode.MOVE_NOW
                case Keyword.TURN:
                    kw_op_code = CobOpCode.TURN_NOW

        # COB, why are you like this?
        # Need to swap the arg order for these keywords because
        # "The COB emulator in Recoil was created via reverse engineering/as a hacky modding tool or something"
        # reasons
        if keyword in (Keyword.SET, Keyword.ATTACH_UNIT):
            # yes, this will get reversed again in a moment
            args = args[::-1]

        immediate_args: list[nodes.NameNode | nodes.Axis | None] = [
            a for a in args if isinstance(a, (nodes.NameNode, nodes.Axis))
        ]

        stack_args = [a for a in args if a not in immediate_args]
        while len(stack_args) < kw_op_code.num_stack_params:
            stack_args.append(None)

        immediate_args = list(islice(chain(immediate_args, repeat(None)), kw_op_code.num_immediate_params))
        stack_args = stack_args[: kw_op_code.num_stack_params]

        immediate_vals = []
        for arg in immediate_args:
            if isinstance(arg, nodes.NameNode):
                immediate_vals.append(self.name_registry.lookup(arg).index)
            elif isinstance(arg, nodes.Axis):
                immediate_vals.append(arg.axis.value)
            else:
                immediate_vals.append(0)

        # Iterate backwards because we're building a Stack (FILO), not a Queue (FIFO)
        for arg in stack_args[::-1]:
            if arg is not None:
                self.handle_node(arg)
            else:
                self.handle_node(nodes.Constant(0))

        self.code.append(kw_op_code)
        self.code.extend(immediate_vals)

    @_handle_node.register
    def _handle_node__var_statement(self, var_statement: nodes.VarStatement):
        for var in var_statement:
            self.name_registry.register(var, NameType.LOCAL_VAR)
            self.code.append(CobOpCode.CREATE_LOCAL_VAR)

    @_handle_node.register(nodes.CallScriptStatement)
    @_handle_node.register(nodes.StartScriptStatement)
    def _handle_node__function_call(self, statement: nodes.CallScriptStatement | nodes.StartScriptStatement):
        for arg in statement.args[1:]:
            self.handle_node(arg)

        self.code.append(CobOpCode.from_keyword(statement.keyword))
        if not isinstance(func_name := statement.args[0], nodes.NameNode):
            raise CodeError(
                f"Expected a function name, got {func_name.node_name}",
                CodeLocation.from_node(statement.parser_node),
            )
        self.code.append(self.name_registry.lookup(func_name).index)
        self.code.append(len(statement.args) - 1)

    @_handle_node.register
    def _handle_node__if_statement(self, if_statement: nodes.IfStatement):
        self.handle_node(if_statement.condition)
        self.code.append(CobOpCode.JUMP_NOT_EQUAL)

        jump_dest_if_false_idx = len(self.code)
        self.code.append(CobOpCode.BAD_OP_PLACEHOLDER)  # placeholder

        self.handle_node(if_statement.then_block)

        jump_dest_skip_else_block_idx = 0
        if if_statement.else_block is not None:
            self.code.append(CobOpCode.JUMP)
            jump_dest_skip_else_block_idx = len(self.code)
            self.code.append(CobOpCode.BAD_OP_PLACEHOLDER)  # placeholder

        self.code[jump_dest_if_false_idx] = len(self.code)

        if if_statement.else_block is not None:
            self.handle_node(if_statement.else_block)
            self.code[jump_dest_skip_else_block_idx] = len(self.code)

    @_handle_node.register
    def _handle_node__while_statement(self, while_statement: nodes.WhileStatement):
        start_jump_pos = len(self.code)
        self.handle_node(while_statement.condition)

        self.code.append(CobOpCode.JUMP_NOT_EQUAL)
        exit_while_jump_idx = len(self.code)
        self.code.append(CobOpCode.BAD_OP_PLACEHOLDER)

        self.handle_node(while_statement.block)
        self.code.append(CobOpCode.JUMP)
        self.code.append(start_jump_pos)

        self.code[exit_while_jump_idx] = len(self.code)

    # For statements are not supported in BOS. :'(
    # @_handle_node.register
    # def _handle_node__for_statement(self, for_statement: nodes.ForStatement):
    #     pass

    @_handle_node.register
    def _handle_node__assign_statement(self, assign_statement: nodes.AssignStatement):
        self.handle_node(assign_statement.expression)
        name_entry = self.name_registry.lookup(assign_statement.variable)

        match name_entry.name_type:
            case NameType.STATIC_VAR:
                self.code.append(CobOpCode.POP_STATIC)
            case NameType.LOCAL_VAR | NameType.ARGUMENT:
                self.code.append(CobOpCode.POP_LOCAL_VAR)
            case _:
                raise CodeError(
                    f'Illegal assignment to {name_entry.name_type.description} "{assign_statement.variable.name}".',
                    CodeLocation.from_node(assign_statement.parser_node),
                )

        self.code.append(name_entry.index)

    @_handle_node.register
    def _handle_node__return_statement(self, return_statement: nodes.ReturnStatement):
        if return_statement.expression is not None:
            self.handle_node(return_statement.expression)
        else:
            self.code.extend([CobOpCode.PUSH_CONSTANT, 0])

        self.code.append(CobOpCode.RETURN)

    # expressions
    @_handle_node.register
    def _handle_node__unary_expression(self, expr: nodes.UnaryExpression):
        maybe_folded_expr = self.constant_folding(expr)
        if maybe_folded_expr is not expr:
            # node changed, reprocess
            log.debug("Unary expression folded to %s", repr(maybe_folded_expr))
            self.handle_node(maybe_folded_expr)
        else:
            self.handle_node(expr.operand)
            self.code.append(CobOpCode.from_expression_op(expr.op))

    @_handle_node.register
    def _handle_node__binary_expression(self, expr: nodes.BinaryExpression):
        maybe_folded_expr = self.constant_folding(expr)
        if maybe_folded_expr is not expr:
            # node changed, reprocess
            log.debug("Binary expression folded to %s", repr(maybe_folded_expr))
            self.handle_node(maybe_folded_expr)
        else:
            self.handle_node(expr.left)
            self.handle_node(expr.right)
            self.code.append(CobOpCode.from_expression_op(expr.op))

    @singledispatchmethod
    def constant_folding(self, node: nodes.ASTNode):
        return node

    @constant_folding.register
    def _constant_folding__unary_expression(self, expr: nodes.UnaryExpression):
        operand = self.constant_folding(expr.operand)
        if isinstance(operand, nodes.Constant):
            log.debug("Folding %s %s", expr.op, repr(operand))
            return nodes.Constant(expr.op.eval(operand.number_value()), parser_node=expr.parser_node)
        return expr

    @constant_folding.register
    def _constant_folding__binary_expression(self, expr: nodes.BinaryExpression):
        left = self.constant_folding(expr.left)
        right = self.constant_folding(expr.right)
        if isinstance(left, nodes.Constant) and isinstance(right, nodes.Constant):
            log.debug("Folding %s %s %s", repr(left), expr.op, repr(right))
            return nodes.Constant(expr.op.eval(left.number_value(), right.number_value()), parser_node=expr.parser_node)
        return expr

    # terms
    @_handle_node.register
    def _handle_node__constant(self, constant: nodes.Constant):
        self.code.extend((CobOpCode.PUSH_CONSTANT, constant.int32_value()))

    @_handle_node.register
    def _handle_node__var_name_term(self, term: nodes.VarNameTerm):
        entry = self.name_registry.lookup(term.var_name)
        match entry.name_type:
            case NameType.STATIC_VAR:
                self.code.append(CobOpCode.PUSH_STATIC)
            case NameType.LOCAL_VAR | NameType.ARGUMENT:
                self.code.append(CobOpCode.PUSH_LOCAL_VAR)
            case NameType.PIECE | NameType.FUNCTION:
                self.code.append(CobOpCode.PUSH_CONSTANT)  # the value to use is literally the index
        self.code.append(entry.index)

    @_handle_node.register
    def _handle_node__rand_term(self, rand: nodes.RandTerm):
        self.handle_node(rand.min)
        self.handle_node(rand.max)
        self.code.append(CobOpCode.RAND)

    @_handle_node.register
    def _handle_node__get_term(self, get_term: nodes.GetTerm):
        self.handle_node(get_term.get_call)

    @_handle_node.register
    def _handle_node__get_call(self, get_call: nodes.GetCall):
        self.handle_node(get_call.value_idx)

        if any(arg is not None for arg in get_call.args):
            for arg in islice(chain(get_call.args, repeat(None)), 4):
                self.handle_node(arg) if arg is not None else nodes.Constant(0)
            self.code.append(CobOpCode.GET)
        else:
            self.code.append(CobOpCode.GET_UNIT_VALUE)
