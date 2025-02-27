from array import array
from functools import singledispatchmethod
from typing import cast, ClassVar

from bos import ast_nodes as nodes
from bos2cob_py3 import LINEAR_SCALE, ANGULAR_SCALE
from cob.compiler.name_registry import NameRegistry
from cob.opcodes import CobOpCode


class CobCompiler:
    LINEAR_SCALE: ClassVar[int] = 65536
    ANGULAR_SCALE: ClassVar[int] = 182

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
    # forStatement
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
            match type(arg):
                case nodes.PieceName | nodes.FuncName:
                    post_opcode_vals.append(self.name_registry.get_idx(cast(nodes.NameNode, arg))[0])
                case nodes.Axis:
                    post_opcode_vals.append(cast(nodes.Axis, arg).axis.value)
                case _:
                    self._handle_node(arg)

    @_handle_node.register
    def _handle_node__call_statement(self, call_statement: nodes.CallStatement):
        print("TODO: handle call statement")

    @_handle_node.register
    def _handle_node__start_statement(self, start_statement: nodes.StartStatement):
        print("TODO: handle start statement")

    @_handle_node.register
    def _handle_node__var_statement(self, var_statement: nodes.VarStatement):
        print("TODO: handle var statement")

    @_handle_node.register
    def _handle_node__if_statement(self, if_statement: nodes.IfStatement):
        print("TODO: handle if statement")

    @_handle_node.register
    def _handle_node__while_statement(self, while_statement: nodes.WhileStatement):
        print("TODO: handle while statement")

    @_handle_node.register
    def _handle_node__for_statement(self, for_statement: nodes.ForStatement):
        print("TODO: handle for statement")

    @_handle_node.register
    def _handle_node__assign_statement(self, assign_statement: nodes.AssignStatement):
        print("TODO: handle assign statement")

    @_handle_node.register
    def _handle_node__return_statement(self, return_statement: nodes.ReturnStatement):
        if return_statement.expression is not None:
            self._handle_node(return_statement.expression)
        else:
            self.code.extend([CobOpCode.PUSH_CONSTANT, 0])

        self.code.append(CobOpCode.RETURN)

    # expressions

    # constants
    @_handle_node.register
    def _handle_node__constant(self, constant: nodes.Constant):
        match constant.const_type:
            case 'linear':
                value = LINEAR_SCALE * constant.number_value
            case 'angular':
                value = ANGULAR_SCALE * constant.number_value
            case _:
                value = constant.number_value
        # print(constant.model_dump(), value)
        self.code.extend((CobOpCode.PUSH_CONSTANT, int(value)))
