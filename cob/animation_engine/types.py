from collections.abc import Callable
from dataclasses import dataclass
from enum import IntEnum
from typing import NewType, TypeAlias

from cob.animation_engine.local_model_piece import LocalModelPiece
from cob.animation_engine.math import RadiansPerFrame, Axis, Radians

PieceIndex = NewType('PieceIndex', int)
PieceIndex_NONE = PieceIndex(-1)

ScriptPieceIndex = NewType('ScriptPieceIndex', PieceIndex)
ScriptPieceIndex_NONE = ScriptPieceIndex(PieceIndex_NONE)

ModelPieceIndex = NewType('ModelPieceIndex', PieceIndex)
ModelPieceIndex_NONE = ModelPieceIndex(PieceIndex_NONE)

ValueIndex = NewType('ValueIndex', int)
WeaponIndex = NewType('WeaponIndex', int)
FunctionIndex = NewType('FunctionIndex', int)

UnitId = NewType('UnitId', int)
WeaponDefId = NewType('WeaponDefId', int)


class AnimType(IntEnum):
    ANone = -1
    ATurn = 0
    ASpin = 1
    AMove = 2

@dataclass
class AnimInfo:
    axis: Axis = 0
    piece: ScriptPieceIndex = 0
    speed: float | Radians = 0
    dest: float | Radians = 0
    accel: RadiansPerFrame = 0
    done: bool = False
    has_waiting: bool = False


AnimContainerType: TypeAlias = list[AnimInfo]

TickAnimFunc: TypeAlias = Callable[[int, LocalModelPiece, AnimInfo], bool]
""" 
    A function that takes the following parameters:
    - tick_rate: int
    - piece: LocalModelPiece
    - anim: AnimInfo
    and returns a boolean indicating whether the animation is done.
"""
