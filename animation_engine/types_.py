import enum
from dataclasses import dataclass
from typing import NamedTuple


class IdWithName(int):
    name: str = ""

    def __new__(cls, value: int, name: str):
        val = int.__new__(cls, value)
        val.name = name
        return val

    def __repr__(self):
        return f'{self.__class__.__name__}({int(self)}, "{self.name}")'


# @formatter:off
class ScriptPieceIndex(IdWithName): pass
class ModelPieceIndex(IdWithName): pass
class ValueIndex(IdWithName): pass
class WeaponIndex(IdWithName): pass
class FunctionIndex(IdWithName): pass

class UnitId(IdWithName): pass
class WeaponDefId(IdWithName): pass
# @formatter:on

class Axis(enum.IntEnum):
    """
    Enumeration for the axes of rotation or movement.
    """
    X = 0
    Y = 1
    Z = 2


class AnimType(enum.IntEnum):
    """
    Enumeration for different types of animations.
    """
    Turn = 0
    Spin = 1
    Move = 2


class AnimKey(NamedTuple):
    """
    A unique key for identifying an animation.
    (AnimType, ScriptPieceIndex, Axis)
    """
    anim_type: AnimType
    piece: ScriptPieceIndex
    axis: Axis


@dataclass
class AnimInfo:
    key: AnimKey

    target: float = 0

    position: float = 0
    velocity: float = 0
    accel: float = 0

    done: bool = False
    has_waiting: bool = False
