from dataclasses import dataclass
from enum import IntEnum
from typing import NewType, NamedTuple

from unit_animation_engine import math
from unit_animation_engine.math import RadiansPerFrame, Axis, radians

PieceIndex = NewType("PieceIndex", int)
PieceIndex_NONE = PieceIndex(-1)

ScriptPieceIndex = NewType("ScriptPieceIndex", PieceIndex)
ScriptPieceIndex_NONE = ScriptPieceIndex(PieceIndex_NONE)

ModelPieceIndex = NewType("ModelPieceIndex", PieceIndex)
ModelPieceIndex_NONE = ModelPieceIndex(PieceIndex_NONE)

ValueIndex = NewType("ValueIndex", int)
WeaponIndex = NewType("WeaponIndex", int)
FunctionIndex = NewType("FunctionIndex", int)

UnitId = NewType("UnitId", int)
WeaponDefId = NewType("WeaponDefId", int)

Milliseconds = NewType("Milliseconds", int)
TicksPerSecond = NewType("TicksPerSecond", int)


class AnimType(IntEnum):
    """
    Enumeration for different types of animations.
    """
    ANone = -1
    ATurn = 0
    ASpin = 1
    AMove = 2


class AnimKey(NamedTuple):
    """
    A unique key for identifying an animation.
    (AnimType, ScriptPieceIndex, Axis)
    """
    anim_type: AnimType
    piece: ScriptPieceIndex
    axis: math.Axis


@dataclass
class AnimInfo:
    """
    Stores information about an animation.
    """

    anim_type: AnimType = AnimType.ANone
    piece: ScriptPieceIndex = 0
    axis: Axis = 0
    speed: float | radians = 0
    dest: float | radians = 0
    accel: RadiansPerFrame = 0
    done: bool = False
    has_waiting: bool = False

    def get_anim_key(self) -> AnimKey:
        """ Get a key used to index/deduplicate this animation info"""
        return AnimKey(self.anim_type, self.piece, self.axis)



