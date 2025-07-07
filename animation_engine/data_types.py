import enum
from dataclasses import dataclass
from typing import NamedTuple, TypeVar, Generic, TYPE_CHECKING
from animation_engine.transform import Transform


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

TransformSubtype = TypeVar("TransformSubtype", bound=Transform)
class AnimKey(NamedTuple, Generic[TransformSubtype]):
    """
    A unique key for identifying an animation.
    (Transform, AnimType, Axis)
    """
    transform: TransformSubtype
    anim_type: AnimType
    axis: Axis


@dataclass
class AnimInfo(Generic[TransformSubtype]):
    key: AnimKey[TransformSubtype]

    target: float = 0

    velocity: float = 0
    accel: float = 0

    done: bool = False
    has_waiting: bool = False
