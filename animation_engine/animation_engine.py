from __future__ import annotations
from typing import TYPE_CHECKING

import logging

from animation_engine.math import ticks_per_second

if TYPE_CHECKING:
    from animation_engine.animator import Animator
from animation_engine.exceptions import AnimationEngineError
from animation_engine.engine_module import EngineModule, EngineModuleT
from animation_engine.types_ import AnimKey
from animation_engine.unit import Unit

log = logging.getLogger(__name__)


class AnimationEngine:

    __current_animator: Animator | None
    __active_animators: list[Animator]
    __engine_modules: dict[type[EngineModule], EngineModule]
    __ticking: bool

    def __init__(self):
        self.__current_animator = None
        self.__active_animators = []
        self.__engine_modules = {}

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
        for engine_module in self.__engine_modules.values():
            engine_module.shutdown()

    def register_engine_module(self, engine_module_instance: EngineModule):
        if self.__ticking:
            raise AnimationEngineError("An Engine Module cannot be registered in the middle of a tick!")

        engine_type = type(engine_module_instance)
        if engine_type in self.__engine_modules:
            raise AnimationEngineError(
                f"An Engine Module of type '{engine_type.__name__}' has already been registered"
            )

        self.__engine_modules[engine_type] = engine_module_instance
        engine_module_instance.on_registered(self)

    def get_script_engine(self, script_engine_type: type[EngineModuleT]) -> EngineModuleT | None:
        return self.__engine_modules.get(script_engine_type, None)

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

    def tick(self, tick_rate: ticks_per_second) -> None:
        self.__ticking = True
        module_list = list(self.__engine_modules.values())

        for module in module_list:
            module.tick_pre_animation(tick_rate)

        # protect against list modification while iterating
        animators_snapshot = list(self.__active_animators)
        self.__tick__update_animations(tick_rate, animators_snapshot)
        self.__tick__cleanup_finished_animations(tick_rate, animators_snapshot)

        for module in module_list:
            module.tick_post_animation(tick_rate)

        self.__ticking = False

    def __tick__update_animations(self, tick_rate: ticks_per_second, anims_to_tick: list[Animator]) -> None:
        for animator in anims_to_tick:
            self.__current_animator = animator
            animator.tick_all_anims(tick_rate)
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
        for engine_module in self.__engine_modules.values():
            engine_module.notify_animation_finished(unit, anim_key)
