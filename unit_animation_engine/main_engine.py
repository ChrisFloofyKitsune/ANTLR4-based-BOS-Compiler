from __future__ import annotations
from typing import TYPE_CHECKING

import logging

if TYPE_CHECKING:
    from unit_animation_engine.animator import Animator
from unit_animation_engine.exceptions import UnitEngineError
from unit_animation_engine.script_engine import ScriptEngine, ScriptEngineT
from unit_animation_engine.types_ import AnimKey
from unit_animation_engine.unit import Unit

log = logging.getLogger(__name__)


class MainAnimationEngine:

    __current_animator: Animator | None
    __active_animators: list[Animator]
    __unit_script_engines: dict[type[ScriptEngine], ScriptEngine]
    __ticking: bool

    def __init__(self):
        self.__current_animator = None
        self.__active_animators = []
        self.__unit_script_engines = {}

    def __del__(self):
        self.shutdown()

    def shutdown(self) -> None:
        if self.__ticking:
            log.error(
                'Animation Engine shutdown while it was ticking! This should not happen.',
                stack_info=True
            )

        self.__ticking = False

        self.__active_animators.clear()
        for script_engine in self.__unit_script_engines.values():
            script_engine.shutdown()

    def register_script_engine(self, script_engine_instance: ScriptEngine):
        if self.__ticking:
            raise UnitEngineError("A Script Engine cannot be registered in the middle of a tick!")

        engine_type = type(script_engine_instance)
        if engine_type in self.__unit_script_engines:
            raise UnitEngineError(
                f"A Script Engine of type '{engine_type.__name__}' has already been registered"
            )

        self.__unit_script_engines[engine_type] = script_engine_instance
        script_engine_instance.on_registered(self)

    def get_script_engine(self, script_engine_type: type[ScriptEngineT]) -> ScriptEngineT | None:
        return self.__unit_script_engines.get(script_engine_type, None)

    def add_active_animator(self, animator: Animator):
        if animator == self.__current_animator:
            return

        if not animator in self.__active_animators:
            self.__active_animators.append(animator)

    def remove_active_animator(self, animator: Animator):
        # note: removal of an animator is blocked while it is being ticked
        # another check to see if it needs removal will happen after the tick
        if animator == self.__current_animator:
            return

        if animator in self.__active_animators:
            self.__active_animators.remove(animator)

    def tick(self, delta_time_ms: int) -> None:
        self.__ticking = True
        sub_engine_list = list(self.__unit_script_engines.values())

        for sub_engine in sub_engine_list:
            sub_engine.tick_pre_animation(delta_time_ms)

        # protect against list modification while iterating
        animators_snapshot = list(self.__active_animators)
        self.__tick__update_animations(delta_time_ms, animators_snapshot)
        self.__tick__cleanup_finished_animations(delta_time_ms, animators_snapshot)

        for sub_engine in sub_engine_list:
            sub_engine.tick_post_animation(delta_time_ms)

        self.__ticking = False

    def __tick__update_animations(self, delta_time_ms: int, anims_to_tick: list[Animator]) -> None:
        for animator in anims_to_tick:
            self.__current_animator = animator
            animator.tick_all_anims(delta_time_ms)
        self.__current_animator = None

    def __tick__cleanup_finished_animations(self, delta_time_ms: int, anims_to_tick: list[Animator]) -> None:
        for animator in anims_to_tick:
            self.__current_animator = animator
            # this may end up calling into unit scripts that were waiting on this animation
            animator.tick_anim_finished()
            if not animator.have_animations():
                self.__active_animators.remove(animator)
        self.__current_animator = None

    def notify_animation_finished(self, unit: Unit, anim_key: AnimKey):
        for script_engine in self.__unit_script_engines.values():
            script_engine.notify_animation_finished(unit, anim_key)
