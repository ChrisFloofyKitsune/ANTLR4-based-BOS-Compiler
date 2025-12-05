from abc import ABC
from typing import Generator

from bos.ast_nodes.base_nodes import BlockLevelNode, ValueNode
from bos.ast_nodes.enums import Keyword
from bos.ast_nodes.expression_nodes import Expression, MacroCallExpression
from bos.ast_nodes.name_nodes import VarName, NameNode
from bos.ast_nodes.preproc_nodes import DefineName


class Statement(BlockLevelNode, ABC):
    ...


class StatementBlock(Statement):
    block_level_nodes: list[BlockLevelNode]

    def get_value(self):
        return self.block_level_nodes

    def __iter__(self) -> Generator[Statement, None, None]:
        yield from (s for s in self.block_level_nodes if isinstance(s, Statement))

    def __len__(self):
        return len(self.block_level_nodes)

    def __getitem__(self, key):
        return self.block_level_nodes[key]


class KeywordStatement(Statement):
    keyword: Keyword
    args: list[ValueNode | NameNode | None]


class CallScriptStatement(KeywordStatement):
    ...


class StartScriptStatement(KeywordStatement):
    ...


class VarStatement(Statement):
    vars: list[VarName]

    def get_value(self):
        return self.vars

    def __iter__(self) -> Generator[VarName, None, None]:
        yield from self.vars


class IfStatement(Statement):
    condition: Expression | ValueNode
    then_block: Statement
    else_block: Statement | None


class WhileStatement(Statement):
    condition: Expression | ValueNode
    block: Statement


class AssignStatement(Statement):
    variable: VarName
    expression: Expression | ValueNode


class ReturnStatement(Statement):
    expression: Expression | ValueNode | None


class MacroCallStatement(Statement):
    macro_call: MacroCallExpression


class MacroNameStatement(Statement):
    macro_name: DefineName
