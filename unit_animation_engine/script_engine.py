from __future__ import annotations
from typing import TYPE_CHECKING

from abc import ABC, abstractmethod
from typing import TypeVar

if TYPE_CHECKING:
    from unit_animation_engine.main_engine import MainAnimationEngine
    from unit_animation_engine.types_ import AnimKey
    from unit_animation_engine.unit import Unit


class ScriptEngine(ABC):

    _main_engine: MainAnimationEngine

    def on_registered(self, main_engine: MainAnimationEngine):
        self._main_engine = main_engine

    def on_shutdown(self):
        pass

    @abstractmethod
    def tick_pre_animation(self, delta_time_ms: int) -> None:
        pass

    @abstractmethod
    def tick_post_animation(self, delta_time_ms: int) -> None:
        pass

    @abstractmethod
    def notify_animation_finished(self, unit: Unit, anim_info: AnimKey) -> None:
        pass

    @abstractmethod
    def shutdown(self) -> None:
        pass


ScriptEngineT = TypeVar("ScriptEngineT", bound=ScriptEngine)
