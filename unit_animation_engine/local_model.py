from abc import ABC, abstractmethod

from cob.animation_engine.local_model_piece import LocalModelPiece
from cob.animation_engine.types import ModelPieceIndex


class LocalModel(ABC):

    @abstractmethod
    def has_piece(self, model_piece_num: ModelPieceIndex) -> bool:
        pass

    @abstractmethod
    def get_piece(self, model_piece_num: ModelPieceIndex) -> LocalModelPiece:
        pass