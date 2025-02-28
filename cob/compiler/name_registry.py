import enum
from enum import IntEnum

from bos import ast_nodes as nodes
from code_error import CodeError
from code_location import CodeLocation


class NameRegistry:

    class NameType(IntEnum):
        STATIC = 0, 'Static Variable'
        LOCAL = 1, 'Local Variable'
        PIECE = 2, 'Piece Name'
        FUNCTION = 3, 'Function Name'
        ARG = 4, 'Function Argument'

        @enum.property
        def description(self) -> str:
            return self._description

        def __new__(cls, value, description):
            obj = int.__new__(cls, value)
            obj._value_ = value
            obj._description = description
            return obj

    def __init__(self):
        self.__backing_dict: dict[NameRegistry.NameType, dict[nodes.NameNode, int]] = {
            t: dict() for t in NameRegistry.NameType
        }

        self.__lookup_dict: dict[nodes.NameNode, tuple[int, NameRegistry.NameType]] = dict()

    def register(self, name: nodes.NameNode, name_type: NameType):
        lookup_result = self.__lookup_dict.get(name, None)

        if lookup_result is not None:
            _, existing_name_type = lookup_result

            if (
                name_type == existing_name_type
                and name_type in (NameRegistry.NameType.STATIC, NameRegistry.NameType.PIECE)
            ):
                print(
                    f'[WARNING] Duplicate declaration of global name {name_type.description} "{name.name}". Ignoring.',
                    CodeLocation.from_parser_node(name.parser_node)
                )
                return

            raise CodeError(
                f'invalid declaration of {name_type.description} "{name.name}", '
                f'name is already being used by a {existing_name_type.description} declaration',
                CodeLocation.from_parser_node(name.parser_node)
            )

        new_idx = len(self.__backing_dict[name_type])

        # Function arguments share indexes with local variables in function bodies
        if name_type == NameRegistry.NameType.LOCAL:
            new_idx += len(self.__backing_dict[NameRegistry.NameType.ARG])

        self.__backing_dict[name_type][name] = new_idx
        self.__lookup_dict[name] = (new_idx, name_type)

    def get_idx(self, name: nodes.NameNode) -> tuple[int, NameType]:
        result = self.__lookup_dict.get(name, None)

        if result is None:
            raise CodeError(
                f'name "{name.name}" has not been defined',
                CodeLocation.from_parser_node(name.parser_node)
            )

        return result

    def clear_local_names(self):
        self.__backing_dict[NameRegistry.NameType.LOCAL].clear()
        self.__backing_dict[NameRegistry.NameType.ARG].clear()

        self.__lookup_dict = {
            name: (idx, type_) for name, (idx, type_) in self.__lookup_dict.items()
            if type_ not in (NameRegistry.NameType.LOCAL, NameRegistry.NameType.ARG)
        }

    def get_names(self):
        return self.__lookup_dict.copy()

    def get_names_by_type(self, name_type: NameType):
        return self.__backing_dict[name_type].copy()

    def __len__(self):
        return len(self.__lookup_dict)

    def __iter__(self):
        yield from ((n, i, t) for n, (i, t) in self.__lookup_dict.items())
