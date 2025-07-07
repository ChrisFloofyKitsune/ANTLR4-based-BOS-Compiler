from __future__ import annotations
from typing import TYPE_CHECKING

from abc import ABC, abstractmethod
from typing import TypeVar

if TYPE_CHECKING:
    from animation_engine.math import ticks_per_second
    from animation_engine.transform import Transform
    from animation_engine.animation_engine import AnimationEngine
    from animation_engine.data_types import AnimKey


class EngineModule(ABC):

    _main_engine: AnimationEngine

    def on_registered(self, main_engine: AnimationEngine):
        self._main_engine = main_engine

    def on_shutdown(self):
        pass

    @abstractmethod
    def tick_pre_animation(self, tick_rate: ticks_per_second) -> None:
        pass

    @abstractmethod
    def tick_post_animation(self, tick_rate: ticks_per_second) -> None:
        pass

    @abstractmethod
    def notify_animation_finished(self, anim_key: AnimKey) -> None:
        pass

    @abstractmethod
    def shutdown(self) -> None:
        pass


EngineModuleSubtype = TypeVar("EngineModuleSubtype", bound=EngineModule)
