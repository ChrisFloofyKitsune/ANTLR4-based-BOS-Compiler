from abc import ABC

from animation_engine.local_model import LocalModel


class Unit(ABC):

    local_model: LocalModel

    def get_object_space_pos(self, rel_pos):
        pass

    def get_object_space_vec(self, rel_dir):
        pass
