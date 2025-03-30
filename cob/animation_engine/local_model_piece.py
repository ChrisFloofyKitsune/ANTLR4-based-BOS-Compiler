from abc import ABC, abstractmethod

from cob.animation_engine.math import *
from cob.animation_engine.types import PieceIndex, ModelPieceIndex, ScriptPieceIndex


class LocalModelPiece(ABC):

    @abstractmethod
    def get_absolute_pos(self) -> float3:
        raise NotImplementedError

    @abstractmethod
    def get_model_space_matrix(self) -> matrix44:
        raise NotImplementedError

    @abstractmethod
    def get_emit_dir_pos(self) -> tuple[float3, float3]:
        raise NotImplementedError

    @abstractmethod
    def get_position(self) -> float3:
        raise NotImplementedError

    @abstractmethod
    def set_position(self, next_pos: float3) -> None:
        pass

    @abstractmethod
    def get_rotation(self) -> Radians3:
        pass

    @abstractmethod
    def set_rotation(self, next_rot: Radians3) -> None:
        pass

    @abstractmethod
    def get_local_model_piece_index(self) -> ModelPieceIndex:
        pass

    @abstractmethod
    def get_script_piece_index(self) -> ScriptPieceIndex:
        pass

    @abstractmethod
    def get_original_offset(self) -> float3:
        pass

    @abstractmethod
    def set_script_visible(self, visible) -> None:
        pass
