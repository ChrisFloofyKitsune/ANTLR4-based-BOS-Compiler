from array import array
from functools import singledispatchmethod
from typing import cast, Final

from bos import ast_nodes as nodes
from code_error import CodeError
from cob.compiler.name_registry import NameRegistry
from cob.opcodes import CobOpCode
from code_location import CodeLocation

LINEAR_SCALE: Final[int] = 65536
ANGULAR_SCALE: Final[int] = 182


class CobCompiler:
    def __init__(self, /, raise_exception_on_unhandled_node=True):
        self.raise_exception_on_unhandled_node = raise_exception_on_unhandled_node

        self.name_registry: NameRegistry | None = None
        self.function_code_indices: dict[nodes.FuncName, int] | None = None
        self.code: array | None = None

    def _load_global_names(self, file_node: nodes.File):
        assert self.name_registry is not None, 'name_registry has not been initialized!'
        assert len(self.name_registry) == 0, 'names have already been loaded!'

        for declaration in file_node:
            if isinstance(declaration, nodes.PieceDeclaration):
                for piece_name in declaration:
                    self.name_registry.register(piece_name, NameRegistry.NameType.PIECE)
            elif isinstance(declaration, nodes.StaticVarDeclaration):
                for var_name in declaration:
                    self.name_registry.register(var_name, NameRegistry.NameType.STATIC)
            elif isinstance(declaration, nodes.FuncDeclaration):
                self.name_registry.register(declaration.name, NameRegistry.NameType.FUNCTION)
            else:
                raise ValueError('Unable to register names for object', declaration)

    @singledispatchmethod
    def _handle_node(self, node: nodes.ASTNode):
        if self.raise_exception_on_unhandled_node:
            raise NotImplementedError(
                f'INTERNAL COMPILER ERROR: Node of type {node.node_name} does not have a handler!'
            )
        print(f'TODO: handle {node.node_name} AST Node')
        self.code.append(CobOpCode.BAD_OP_PLACEHOLDER)

    @_handle_node.register(list)
    def _handle_node__list(self, node_list: list[nodes.ASTNode]):
        for node in node_list:
            self._handle_node(node)

    @_handle_node.register(nodes.PieceDeclaration)
    @_handle_node.register(nodes.StaticVarDeclaration)
    @_handle_node.register(nodes.EmptyStatement)
    def _handle_node__noop(self, *_, **__):
        ...

    @_handle_node.register
    def _handle_node__file(self, file_node: nodes.File):
        self.name_registry = NameRegistry()
        self.function_code_indices = dict()
        self.code = array('l')

        self._load_global_names(file_node)
        for decl in file_node:
            self._handle_node(decl)

    @_handle_node.register
    def _handle_node__func_declaration(self, func_decl: nodes.FuncDeclaration):
        self.name_registry.clear_local_names()
        self.function_code_indices[func_decl.name] = len(self.code)

        for arg in func_decl.args:
            self.name_registry.register(arg, NameRegistry.NameType.ARG)
            self.code.append(CobOpCode.CREATE_LOCAL_VAR)

        self._handle_node(func_decl.block)

        # add return at end of it's missing
        if len(func_decl.block) == 0 or not isinstance(func_decl.block[-1], nodes.ReturnStatement):
            self.code.extend([CobOpCode.PUSH_CONSTANT, 0, CobOpCode.RETURN])

    @_handle_node.register
    def _handle_node__statement_block(self, block: nodes.StatementBlock):
        for statement in block:
            self._handle_node(statement)

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
        if keyword == nodes.Keyword.PLAY_SOUND:
            raise NotImplementedError("PLAY_SOUND statement is not supported")

        # Get call done purely for side effects, remove the result from the stack
        if keyword == nodes.Keyword.GET:
            self._handle_node(keyword_statement.args[0])
            self.code.append(CobOpCode.POP_STACK)
            return

        args = keyword_statement.args
        kw_op_code = CobOpCode.from_keyword(keyword_statement.keyword)
        if keyword in (nodes.Keyword.MOVE, nodes.Keyword.TURN) and args[-1] is None:
            match keyword:
                case nodes.Keyword.MOVE:
                    kw_op_code = CobOpCode.MOVE_NOW
                case nodes.Keyword.TURN:
                    kw_op_code = CobOpCode.TURN_NOW
            args = args[:-1]

        # print(keyword_statement.keyword, kw_op_code.name)
        post_opcode_vals = []
        for arg in args:
            match arg:
                case _ if isinstance(arg, nodes.NameNode):
                    post_opcode_vals.append(self.name_registry.get_idx(cast(nodes.NameNode, arg))[0])
                case _ if isinstance(arg, nodes.Axis):
                    post_opcode_vals.append(cast(nodes.Axis, arg).axis.value)
                case _:
                    self._handle_node(arg)

        # legacy/dummy arg :(
        if keyword == nodes.Keyword.ATTACH_UNIT:
            self.code.extend([CobOpCode.PUSH_CONSTANT, 0])

        self.code.append(kw_op_code)
        self.code.extend(post_opcode_vals)

    @_handle_node.register
    def _handle_node__var_statement(self, var_statement: nodes.VarStatement):
        for var in var_statement:
            self.name_registry.register(var, NameRegistry.NameType.LOCAL)
            self.code.append(CobOpCode.CREATE_LOCAL_VAR)

    @_handle_node.register(nodes.CallStatement)
    @_handle_node.register(nodes.StartStatement)
    def _handle_node__function_call(self, statement: nodes.CallStatement | nodes.StartStatement):
        for arg in statement.args[1:]:
            self._handle_node(arg)

        self.code.append(CobOpCode.from_keyword(statement.keyword))
        self.code.append(self.name_registry.get_idx(statement.args[0])[1])
        self.code.append(len(statement.args) - 1)

    @_handle_node.register
    def _handle_node__if_statement(self, if_statement: nodes.IfStatement):
        self._handle_node(if_statement.condition)
        self.code.append(CobOpCode.JUMP_NOT_EQUAL)

        jump_dest_if_false_idx = len(self.code)
        self.code.append(CobOpCode.BAD_OP_PLACEHOLDER)  # placeholder

        self._handle_node(if_statement.then_block)

        jump_dest_skip_else_block_idx = 0
        if if_statement.else_block is not None:
            self.code.append(CobOpCode.JUMP)
            jump_dest_skip_else_block_idx = len(self.code)
            self.code.append(CobOpCode.BAD_OP_PLACEHOLDER)  # placeholder

        self.code[jump_dest_if_false_idx] = len(self.code)

        if if_statement.else_block is not None:
            self._handle_node(if_statement.else_block)
            self.code[jump_dest_skip_else_block_idx] = len(self.code)

    @_handle_node.register
    def _handle_node__while_statement(self, while_statement: nodes.WhileStatement):
        start_jump_pos = len(self.code)
        self._handle_node(while_statement.condition)

        self.code.append(CobOpCode.JUMP_NOT_EQUAL)
        exit_while_jump_idx = len(self.code)
        self.code.append(CobOpCode.BAD_OP_PLACEHOLDER)

        self._handle_node(while_statement.block)
        self.code.append(CobOpCode.JUMP)
        self.code.append(start_jump_pos)

        self.code[exit_while_jump_idx] = len(self.code)

    # For statements are not supported in BOS. :'(
    # @_handle_node.register
    # def _handle_node__for_statement(self, for_statement: nodes.ForStatement):
    #     print("TODO: handle for statement")

    @_handle_node.register
    def _handle_node__assign_statement(self, assign_statement: nodes.AssignStatement):
        self._handle_node(assign_statement.expression)
        idx, name_type = self.name_registry.get_idx(assign_statement.variable)

        match name_type:
            case NameRegistry.NameType.STATIC:
                self.code.append(CobOpCode.POP_STATIC)
            case NameRegistry.NameType.LOCAL | NameRegistry.NameType.ARG:
                self.code.append(CobOpCode.POP_LOCAL_VAR)
            case _:
                raise CodeError(
                    f'Illegal assignment to {name_type.description} "{assign_statement.variable.name}".',
                    CodeLocation.from_parser_node(assign_statement.parser_node)
                )

        self.code.append(idx)

    @_handle_node.register
    def _handle_node__return_statement(self, return_statement: nodes.ReturnStatement):
        if return_statement.expression is not None:
            self._handle_node(return_statement.expression)
        else:
            self.code.extend([CobOpCode.PUSH_CONSTANT, 0])

        self.code.append(CobOpCode.RETURN)

    # expressions
    @_handle_node.register
    def _handle_node__unary_expression(self, expr: nodes.UnaryExpression):
        self._handle_node(expr.operand)
        self.code.append(CobOpCode.from_unary_expression_op(expr.op))

    @_handle_node.register
    def _handle_node__binary_expression(self, expr: nodes.BinaryExpression):
        self._handle_node(expr.operand1)
        self._handle_node(expr.operand2)
        self.code.append(CobOpCode.from_binary_expression_op(expr.op))

    # terms
    @_handle_node.register
    def _handle_node__constant(self, constant: nodes.Constant):
        match constant.const_type:
            case 'linear':
                float_value = LINEAR_SCALE * constant.number_value
            case 'angular':
                float_value = ANGULAR_SCALE * constant.number_value
            case _:
                float_value = constant.number_value

        int_value = int(float_value)
        if int_value > 0xFFFF_FFFF or int_value < -0x8000_0000:
            raise CodeError(
                f'{"Overflow" if int_value > 0 else "Underflow"} error compiling constant {constant.model_dump()}. '
                f'Computed value (int_value) cannot fit inside a 32bit int',
                CodeLocation.from_parser_node(constant.parser_node)
            )

        # force large unsigned ints to fit
        if int_value > 0x7FFF_FFFF:
            int_value -= 0x1_0000_0000
            if isinstance(constant.number_value, float):
                print(
                    f'[WARNING] Converted float from {constant.model_dump()} (computed: {float_value}) to very large negative int {int_value}',
                    CodeLocation.from_parser_node(constant.parser_node)
                )

        self.code.extend((CobOpCode.PUSH_CONSTANT, int_value))

    @_handle_node.register
    def _handle_node__var_name_term(self, term: nodes.VarNameTerm):
        idx, var_type = self.name_registry.get_idx(term.var_name)
        self.code.append(idx)
        match var_type:
            case NameRegistry.NameType.STATIC:
                self.code.append(CobOpCode.PUSH_STATIC)
            case NameRegistry.NameType.LOCAL | NameRegistry.NameType.ARG:
                self.code.append(CobOpCode.PUSH_LOCAL_VAR)
            case NameRegistry.NameType.PIECE | NameRegistry.NameType.FUNCTION:
                self.code.append(CobOpCode.PUSH_CONSTANT)  # the value to use is literally the index

    @_handle_node.register
    def _handle_node__rand_term(self, rand: nodes.RandTerm):
        self._handle_node(rand.min)
        self._handle_node(rand.max)
        self.code.append(CobOpCode.RAND)

    @_handle_node.register
    def _handle_node__get_term(self, get_term: nodes.GetTerm):
        self._handle_node(get_term.get_call)

    @_handle_node.register
    def _handle_node__get_call(self, get_call: nodes.GetCall):
        self._handle_node(get_call.value_idx)

        if len(get_call.args) > 0:
            for idx in range(4):
                arg = get_call.args[idx] if idx < len(get_call.args) else nodes.Constant(0)
                self._handle_node(arg)
            self.code.append(CobOpCode.GET)
        else:
            self.code.append(CobOpCode.GET_UNIT_VALUE)
