from __future__ import annotations

from copy import deepcopy
from typing import TypeVar, Generic, Final

T = TypeVar("T")


class CheckpointValue(Generic[T]):
    _NO_CHECKPOINT_VALUE: Final[object] = object()

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
        return self._value(instance)

    def __set__(self, instance: object, value):
        self._set_value(instance, value)

    def _value(self, instance: object) -> T | None:
        if self._name not in instance.__dict__:
            new_val = deepcopy(self._default)
            instance.__dict__[self._name] = new_val
            return new_val
        else:
            return instance.__dict__[self._name]

    def _set_value(self, instance: object, value: T) -> None:
        instance.__dict__[self._name] = deepcopy(value)

    def _checkpoint_value(self, instance: object) -> T:
        return instance.__dict__.get(self._checkpoint_value_name, CheckpointValue._NO_CHECKPOINT_VALUE)

    def _set_checkpoint_value(self, instance: object, value: T) -> None:
        instance.__dict__[self._checkpoint_value_name] = deepcopy(value)

    def check_value_changed(self, instance: object) -> bool:
        return self._checkpoint_value(instance) != self._value(instance)

    def set_checkpoint(self, instance: object) -> None:
        self._set_checkpoint_value(instance, self._value(instance))
