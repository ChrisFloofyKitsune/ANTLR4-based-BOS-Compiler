from abc import ABC
from typing import Any


class Unit(ABC):

    local_model: Any

    def get_object_space_pos(self, rel_pos):
        pass

    def get_object_space_vec(self, rel_dir):
        pass

