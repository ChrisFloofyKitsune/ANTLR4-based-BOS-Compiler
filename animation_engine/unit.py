import typing
from abc import ABC, abstractmethod
from typing import ClassVar

from animation_engine.local_model import LocalModel
from animation_engine.data_types import UnitId


class Unit(ABC):
    _next_unit_id_num: ClassVar[int] = 1


    local_model: LocalModel

    _id: UnitId

    def __init__(self, unit_name: str = 'unnamed'):
        self._id = UnitId(Unit._next_unit_id_num, unit_name)

    @property
    def id(self) -> UnitId:
        return self._id

    @abstractmethod
    def get_unit_value(self, value_name: str):
        ...

    @abstractmethod
    def set_unit_value(self, value_name: str, value: typing.Any):
        ...

    def get_object_space_pos(self, rel_pos):
        pass

    def get_object_space_vec(self, rel_dir):
        pass
