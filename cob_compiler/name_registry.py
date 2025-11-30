import enum
from enum import auto
import logging
import traceback
from enum import IntEnum
from typing import TypeVar, Protocol, Generic

log = logging.getLogger(__name__)


class NameType(IntEnum):
    # @formatter:off
    PIECE      = auto(), 'Piece Name'
    STATIC_VAR = auto(), 'Static Variable'
    FUNCTION   = auto(), 'Function Name'
    ARGUMENT   = auto(), 'Function Argument'
    LOCAL_VAR  = auto(), 'Local Variable'
    # @formatter:on

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
        self._backing_dict: dict[NameType, dict[NameValT, int]] = {
            t: dict() for t in NameType if t.value > 0
        }

        self._lookup_dict: dict[str, tuple[int, NameType]] = dict()

    def register(self, name: NameValT, name_type: NameType):
        lookup_result = self._lookup_dict.get(str(name).lower(), None)

        if lookup_result is not None:
            _, existing_name_type = lookup_result
            self.on_name_collision(name, name_type, existing_name_type)

        new_idx = len(self._backing_dict[name_type])

        # Function arguments share indexes with local variables in function bodies
        if name_type == NameType.LOCAL_VAR:
            new_idx += len(self._backing_dict[NameType.ARGUMENT])

        self._backing_dict[name_type][name] = new_idx
        self._lookup_dict[str(name).lower()] = (new_idx, name_type)

    def on_name_collision(self, name: NameValT, name_type: NameType, existing_type: NameType):
        log.error(
            "Attempt to register name %s of type %s, but it already exists as type %s",
            name, name_type.description, existing_type.description,
        )
        traceback.print_stack()

    def lookup(self, name: NameValT) -> tuple[int, NameType]:
        result = self._lookup_dict.get(str(name).lower(), None)

        if result is None:
            return self.on_name_missing(name)

        return result

    def on_name_missing(self, name):
        log.error("Attempt to lookup name %s, but it does not exist", name)
        return -1, NameType(0)

    def clear_local_names(self):
        self._backing_dict[NameType.LOCAL_VAR].clear()
        self._backing_dict[NameType.ARGUMENT].clear()

        self._lookup_dict = {
            name: (idx, type_) for name, (idx, type_) in self._lookup_dict.items()
            if type_ not in (NameType.LOCAL_VAR, NameType.ARGUMENT)
        }

    def get_names(self):
        result: list[NameValT] = []
        for inner_dict in self._backing_dict.values():
            result.extend(inner_dict.keys())
        return result

    def get_names_by_type(self, *name_types: NameType) -> dict[NameValT, int]:
        result = dict()
        for name_type in name_types:
            result.update(self._backing_dict[name_type])
        return result

    def get_name_strings(self, *name_types: NameType):
        return [str(name) for name in self.get_names_by_type(*name_types).keys()]

    def __len__(self):
        return len(self._lookup_dict)
