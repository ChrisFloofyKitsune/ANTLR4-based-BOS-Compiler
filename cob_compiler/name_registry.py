from __future__ import annotations

import enum
import logging
from enum import Enum
from typing import Generic, NamedTuple, Protocol, TypeVar, Literal

log = logging.getLogger(__name__)

StackType = Literal['piece', 'static', 'function', 'local']


class NameType(Enum):
    INVALID = 'Invalid Name', None
    PIECE = 'Piece Name', 'piece'
    STATIC_VAR = 'Static Variable', 'static'
    FUNCTION = 'Function Name', 'function'
    ARGUMENT = 'Function Argument', 'local'  # Arguments share the same stack as local variables
    LOCAL_VAR = 'Local Variable', 'local'  # different enums just for the sake of clarity and better error messages

    @enum.property
    def description(self) -> str:
        return self._description

    @enum.property
    def stack(self) -> StackType:
        return self._stack

    def __new__(cls, description, stack: StackType):
        obj = object.__new__(cls)
        obj._description = description
        obj._stack = stack
        return obj


class Stringable(Protocol):
    def __str__(self) -> str:
        ...


NameValT = TypeVar('NameValT', bound=Stringable)


class NameEntry(NamedTuple, Generic[NameValT]):
    name_type: NameType
    key: str
    index: int
    name_value: NameValT


class NameRegistry(Generic[NameValT]):
    def __init__(self):
        self._backing_dict: dict[StackType, dict[str, NameEntry]] = {
            'piece':    {},
            'static':   {},
            'function': {},
            'local':    {},
        }

        self._lookup_dict: dict[str, NameEntry[NameValT]] = {}
        self._locals_lookup: dict[str, NameEntry[NameValT]] = {}

    def register(self, name_value: NameValT, name_type: NameType):
        key = str(name_value).lower()

        if existing_entry := self._locals_lookup.get(key, self._lookup_dict.get(key, None)):
            action, msg = self.on_name_collision(name_value, name_type, existing_entry)
            match action:
                case 'ignore':
                    log.warning(msg)
                    return
                case 'warn':
                    log.error(msg)
                case 'error':
                    raise ValueError(msg)

        name_stack = name_type.stack
        new_entry = NameEntry(
            name_type=name_type,
            key=key,
            index=len(self._backing_dict[name_stack]),
            name_value=name_value,
        )

        self._backing_dict[name_stack][name_value] = new_entry

        if name_stack == 'local':
            self._locals_lookup[key] = new_entry
        else:
            self._lookup_dict[key] = new_entry

    def on_name_collision(
        self,
        name: NameValT,
        new_name_type: NameType,
        existing_entry: NameEntry[NameValT],
    ) -> tuple[Literal['ignore', 'warn', 'error'], str]:

        if new_name_type.stack == existing_entry.name_type.stack:
            return (
                'ignore',
                (
                    "Name duplication: "
                    "Duplicate name %s of type %s, already exists in stack %s. "
                    "Ignoring the new registration."
                ) % (
                    name,
                    new_name_type,
                    new_name_type.stack,
                ),
            )

        if new_name_type.stack == 'local':
            return (
                'warn',
                (
                    "Name shadowing: "
                    "Local name %s of type %s is shadowing existing name of type %s!! "
                    "This may lead to unexpected behavior."
                ) % (
                    name,
                    new_name_type.description,
                    existing_entry.name_type.description,
                ),
            )

        return (
            'error',
            (
                "Name collision: "
                "Attempt to register name %s of type %s, but it already exists as type %s! "
                "Cannot reconcile name collision!"
            ) % (
                name,
                new_name_type.description,
                existing_entry.name_type.description,
            ),
        )

    def lookup(self, name: NameValT) -> NameEntry[NameValT]:
        key = str(name).lower()
        result = self._locals_lookup.get(key, self._lookup_dict.get(key, None))
        return result if result else self.on_name_missing(name)

    def on_name_missing(self, name):
        log.error("Attempt to lookup name %s, but it does not exist", name)
        return NameEntry(
            name_type=NameType.INVALID,
            name_value=None,
            key="invalid name: " + name,
            index=-1,
        )

    def clear_local_names(self):
        self._backing_dict['local'].clear()
        self._locals_lookup.clear()

    def get_names(self):
        return [name for scope in self._backing_dict.values() for name in scope.keys()]

    def get_names_by_type(self, *name_types: NameType) -> dict[NameValT, int]:
        return {
            entry.name_value: entry.index
            for name_type in name_types
            for entry in self._backing_dict[name_type.stack].values()
        }

    def get_name_strings(self, *name_types: NameType):
        return [str(name) for name in self.get_names_by_type(*name_types).keys()]

    def __len__(self):
        return len(self._lookup_dict)
