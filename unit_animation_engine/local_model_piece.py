from unit_animation_engine.math import *
from unit_animation_engine.transform import Transform
from unit_animation_engine.types import ModelPieceIndex, ScriptPieceIndex


class LocalModelPiece(Transform):

    # TODO: integrate 3D model information (vertices and hierarchy)

    def get_absolute_pos(self) -> float3:
        return self.get_model_space_matrix()[3].xyz

    def get_emit_dir_pos(self) -> tuple[float3, float3]:
        raise NotImplementedError

    def get_position(self) -> float3:
        return self._position

    def set_position(self, value: float3) -> None:
        self._dirty = True
        self._position = value

    def get_rotation(self) -> radians3:
        return self._rotation

    def set_rotation(self, value: radians3) -> None:
        self._dirty = True
        self._rotation = value

    def get_local_model_piece_index(self) -> ModelPieceIndex:
        pass

    def get_script_piece_index(self) -> ScriptPieceIndex:
        pass

    def get_original_offset(self) -> float3:
        pass

    def set_script_visible(self, visible) -> None:
        pass
