from typing import Callable

from unit_animation_engine.math import *
from unit_animation_engine.transform import Transform
from unit_animation_engine.types import ModelPieceIndex, ScriptPieceIndex, AnimInfo


class LocalModelPiece(Transform):

    def get_absolute_pos(self) -> float3:
        return self.model_space_matrix[3].xyz

    def get_emit_dir_pos(self) -> tuple[float3, float3]:
        raise NotImplementedError

    def get_local_model_piece_index(self) -> ModelPieceIndex:
        pass

    def get_script_piece_index(self) -> ScriptPieceIndex:
        pass

    def get_original_offset(self) -> float3:
        pass

    def set_script_visible(self, visible) -> None:
        pass


TickAnimFunc: TypeAlias = Callable[[int, LocalModelPiece, AnimInfo], bool]
"""
A function type for processing animations during a tick.

Parameters:

- tick_rate: int - The rate of ticks per second.
- piece: LocalModelPiece - The model piece being animated.
- anim: AnimInfo - The animation information.

Returns:

- bool: True if the animation is complete, False otherwise.
"""
