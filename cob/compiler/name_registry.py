import enum
import logging
import traceback
from enum import IntEnum
from typing import TypeVar, Protocol, Generic

from code_error import CodeError
from code_location import CodeLocation

log = logging.getLogger(__name__)


class NameType(IntEnum):
    INVALID = 0, 'Invalid Name'
    STATIC = 1, 'Static Variable'
    LOCAL = 2, 'Local Variable'
    PIECE = 3, 'Piece Name'
    FUNCTION = 4, 'Function Name'
    ARG = 5, 'Function Argument'

    @enum.property
    def description(self) -> str:
        return self._description

    def __new__(cls, value, description):
        obj = int.__new__(cls, value)
        obj._value_ = value
        obj._description = description
        return obj

class Stringable(Protocol):
    def __str__(self) -> str:
        ...

NameValT = TypeVar('NameValT', bound=Stringable)
class NameRegistry(Generic[NameValT]):
    def __init__(self):
        self.__backing_dict: dict[NameType, dict[NameValT, int]] = {
            t: dict() for t in NameType if t.value > 0
        }

        self.__lookup_dict: dict[str, tuple[int, NameType]] = dict()

    def register(self, name: NameValT, name_type: NameType):
        lookup_result = self.__lookup_dict.get(str(name).lower(), None)

        if lookup_result is not None:
            _, existing_name_type = lookup_result
            self.on_name_collision(name, name_type, existing_name_type)
            

        new_idx = len(self.__backing_dict[name_type])

        # Function arguments share indexes with local variables in function bodies
        if name_type == NameType.LOCAL:
            new_idx += len(self.__backing_dict[NameType.ARG])

        self.__backing_dict[name_type][name] = new_idx
        self.__lookup_dict[str(name).lower()] = (new_idx, name_type)

    def on_name_collision(self, name: NameValT, name_type: NameType, existing_type: NameType):
        log.error("Attempt to register name %s of type %s, but it already exists as type %s", name, name_type, existing_type)
        traceback.print_stack()

    def lookup(self, name: NameValT) -> tuple[int, NameType]:
        result = self.__lookup_dict.get(str(name).lower(), None)

        if result is None:
            return self.on_name_missing(name)

        return result

    def on_name_missing(self, name):
        log.error("Attempt to lookup name %s, but it does not exist", name)
        return -1, NameType(0)

    def clear_local_names(self):
        self.__backing_dict[NameType.LOCAL].clear()
        self.__backing_dict[NameType.ARG].clear()

        self.__lookup_dict = {
            name: (idx, type_) for name, (idx, type_) in self.__lookup_dict.items()
            if type_ not in (NameType.LOCAL, NameType.ARG)
        }

    def get_names(self):
        result: list[NameValT] = []
        for inner_dict in self.__backing_dict.values():
            result.extend(inner_dict.keys())
        return result

    def get_names_by_type(self, name_type: NameType) -> dict[NameValT, int]:
        return self.__backing_dict[name_type].copy()
    
    def get_name_strings(self, *name_types: NameType):
        return [n for n, (_, t) in self.__lookup_dict.items() if t in name_types]

    def __len__(self):
        return len(self.__lookup_dict)
