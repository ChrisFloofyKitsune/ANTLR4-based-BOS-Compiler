from abc import ABC
from types import SimpleNamespace
from typing import Generator, Any

from bos.ast_nodes.enums import Keyword
from bos.ast_nodes.expression_nodes import Expression, MacroCallExpression
from bos.ast_nodes.base_nodes import BlockLevelNode, ValueNode
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

    def get_value(self):
        return SimpleNamespace(
            keyword=self.keyword,
            args=[a for a in self.args if a]
        )


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

    def get_value(self):
        return SimpleNamespace(condition=self.condition, then_block=self.then_block, else_block=self.else_block)


class WhileStatement(Statement):
    condition: Expression | ValueNode
    block: Statement

    def get_value(self):
        return SimpleNamespace(condition=self.condition, block=self.block)


class AssignStatement(Statement):
    variable: VarName
    expression: Expression | ValueNode

    def get_value(self):
        return SimpleNamespace(variable=self.variable, expression=self.expression)


class ReturnStatement(Statement):
    expression: Expression | ValueNode | None

    def get_value(self):
        return SimpleNamespace(expression=self.expression)


class MacroCallStatement(Statement):
    macro_call: MacroCallExpression

    def get_value(self):
        return SimpleNamespace(
            macro_call=self.macro_call
        )

class MacroNameStatement(Statement):
    macro_name: DefineName

    def get_value(self):
        return SimpleNamespace(
            macro_name=self.macro_name
        )
