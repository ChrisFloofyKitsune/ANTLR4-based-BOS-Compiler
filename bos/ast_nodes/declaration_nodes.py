from abc import ABC
from types import SimpleNamespace
from typing import Generator

from bos.ast_nodes.base_nodes import ASTNode, TopLevelNode
from bos.ast_nodes.statement_nodes import StatementBlock
from bos.ast_nodes.name_nodes import PieceName, VarName, FuncName, ArgName


class File(ASTNode):
    top_level_nodes: list[TopLevelNode]

    @property
    def declarations(self):
        return [n for n in self.top_level_nodes if isinstance(n, Declaration)]

    @property
    def piece_declarations(self):
        return [d for d in self.top_level_nodes if isinstance(d, PieceDeclaration)]

    @property
    def static_var_declarations(self):
        return [d for d in self.top_level_nodes if isinstance(d, StaticVarDeclaration)]

    @property
    def function_declarations(self):
        return [d for d in self.top_level_nodes if isinstance(d, FuncDeclaration)]

    def __iter__(self) -> Generator[TopLevelNode, None, None]:
        yield from self.top_level_nodes


class Declaration(TopLevelNode, ABC):
    ...


class PieceDeclaration(Declaration):
    names: list[PieceName]

    def __iter__(self) -> Generator[PieceName, None, None]:
        yield from self.names


class StaticVarDeclaration(Declaration):
    names: list[VarName]

    def __iter__(self) -> Generator[VarName, None, None]:
        yield from self.names


class FuncDeclaration(Declaration):
    name: FuncName
    args: list[ArgName]
    block: StatementBlock
