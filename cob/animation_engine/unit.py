from abc import ABC

from cob.animation_engine.LocalModel import LocalModel


class Unit(ABC):

    local_model: LocalModel

