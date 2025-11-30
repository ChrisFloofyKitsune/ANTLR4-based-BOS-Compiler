import sys
from abc import ABC, abstractmethod
from types import SimpleNamespace
from typing import Any, Optional

import tree_sitter
from pydantic import BaseModel, computed_field, model_serializer, Field, ConfigDict
from pydantic_core.core_schema import SerializerFunctionWrapHandler


class ASTNode(BaseModel):
    """
    Base class for all BOS Abstract Syntax Tree (AST) nodes.

    The groups of what kind of ASTNodes are valid where
    are encoded and checked via Python subclassing
    and (in some cases) multiple inheritance.

    Pydantic is used to make runtime type enforcement quick and easy.
    """
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
    )

    parser_node: Optional[tree_sitter.Node] = Field(default=None, exclude=True)

    @property
    def node_name(self) -> str:
        return self.__class__.__name__

    @model_serializer(mode='wrap')
    def serialize(self, nxt: SerializerFunctionWrapHandler) -> dict[str, dict[str, Any]]:
        return {self.node_name: nxt(self)}

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.model_dump() == other.model_dump()


class TopLevelNode(ASTNode, ABC):
    """
    Nodes that can appear at the top level of a BOS file.
    """
    ...


class BlockLevelNode(ASTNode, ABC):
    """
    Nodes that can appear inside blocks (function bodies).
    """
    ...


class ValueNode(ASTNode, ABC):
    """
    Nodes that represent values.
    """
    ...


class PreprocNode(TopLevelNode, BlockLevelNode, ABC):
    """
    Nodes that represent preprocessor directives.

    These can appear anywhere.
    """
    ...


class UndefNode(PreprocNode, TopLevelNode, BlockLevelNode, ValueNode, ASTNode):
    """
    Node representing a Tree Sitter parser node that could not be converted to an AST node.
    """
    contents: Any
    name: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        sys.stderr.write(
            f'!! Parser Node was not converted to an AST Node: {self.node_name} !!\n',
        )

    @property
    def node_name(self) -> str:
        return "Undef__" + self.name
