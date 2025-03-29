import sys
from abc import ABC, abstractmethod
from types import SimpleNamespace
from typing import Any, Union

from pydantic import BaseModel, computed_field, model_serializer, Field



class ASTNode(BaseModel, ABC):

    @computed_field
    @property
    def node_name(self) -> str:
        return self.__class__.__name__

    @abstractmethod
    def get_value(self) -> Any:
        pass

    @model_serializer()
    def serialize(self) -> dict[str, Any]:
        value = self.get_value()
        if isinstance(value, SimpleNamespace):
            value = dict(vars(value))

        if isinstance(value, dict):
            value = {
                k: (v.model_dump()) if isinstance(v, BaseModel) else v
                for k, v in value.items()
            }

            value = {
                k: [item.model_dump() if isinstance(item, BaseModel) else item for item in v]
                if isinstance(v, list) else v
                for k, v in value.items()
            }

        from bos.ast_nodes.statement_nodes import StatementBlock
        if (
                isinstance(self, StatementBlock)
                and isinstance(value, list)
                and len(value) == 1
        ):
            return value[0].model_dump()


        return {self.node_name: value}

    parser_node: Union[Any, None] = Field(default=None, exclude=True)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.model_dump() == other.model_dump()


class TopLevelNode(ASTNode, ABC):
    ...


class BlockLevelNode(ASTNode, ABC):
    ...


class ValueNode(ASTNode, ABC):
    ...


class PreprocNode(TopLevelNode, BlockLevelNode, ABC):
    ...


class UndefNode(PreprocNode, TopLevelNode, BlockLevelNode, ValueNode, ASTNode):
    contents: Any
    name: str

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        sys.stderr.write(
            f'!! Parser Node was not converted to an AST Node: {self.node_name} !!\n'
        )

    @computed_field
    @property
    def node_name(self) -> str:
        return "Undef__" + self.name

    def get_value(self):
        return self.contents
