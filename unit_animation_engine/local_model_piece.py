from typing import Callable

from unit_animation_engine.math import *
from unit_animation_engine.transform import Transform
from unit_animation_engine.types_ import ModelPieceIndex, ScriptPieceIndex, AnimInfo


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



