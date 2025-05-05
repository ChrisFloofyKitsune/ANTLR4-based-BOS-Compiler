from __future__ import annotations

from copy import deepcopy
from typing import TypeVar, Generic, Final

T = TypeVar("T")


class WatchedValue(Generic[T]):
    _NO_CHECKPOINT_VALUE: Final = object()

    _name: str
    _checkpoint_value_name: str
    _default: T | None

    def __init__(self, default: T | None = None):
        self._default = default

    def __set_name__(self, owner, name):
        self._name = name
        self._checkpoint_value_name = "_checkpoint_value_" + name

    def __get__(self, instance, owner=None):
        if instance is None:
            return self

        val = self._value(instance)
        if self._checkpoint_value(instance) is WatchedValue._NO_CHECKPOINT_VALUE:
            self._set_checkpoint_value(instance, val)

        return val

    def __set__(self, instance: object, value):
        self._set_value(instance, value)

    def _value(self, instance: object) -> T | None:
        val = instance.__dict__.get(self._name)
        if val is None:
            new_val = deepcopy(self._default)
            instance.__dict__[self._name] = new_val
            return new_val
        else:
            return val

    def _set_value(self, instance: object, value: T) -> None:
        instance.__dict__[self._name] = deepcopy(value)

    def _checkpoint_value(self, instance: object) -> T | WatchedValue._NO_CHECKPOINT_VALUE:
        return instance.__dict__.get(self._checkpoint_value_name, WatchedValue._NO_CHECKPOINT_VALUE)

    def _set_checkpoint_value(self, instance: object, value: T) -> None:
        instance.__dict__[self._checkpoint_value_name] = deepcopy(value)

    def check_dirty(self, instance: object) -> bool:
        if self._checkpoint_value(instance) is WatchedValue._NO_CHECKPOINT_VALUE:
            return False
        return self._checkpoint_value(instance) != self._value(instance)

    def clear_dirty(self, instance: object) -> None:
        self._set_checkpoint_value(instance, WatchedValue._NO_CHECKPOINT_VALUE)
