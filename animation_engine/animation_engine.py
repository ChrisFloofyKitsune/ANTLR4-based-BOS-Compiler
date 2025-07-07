from __future__ import annotations

import logging
from copy import copy
from typing import TYPE_CHECKING

from animation_engine.data_types import AnimKey
from animation_engine.engine_module import EngineModule, EngineModuleSubtype
from animation_engine.exceptions import AnimationEngineError
from animation_engine.math import ticks_per_second

if TYPE_CHECKING:
    from animation_engine.animator import Animator

log = logging.getLogger(__name__)


class AnimationEngine:

    __active_animators: list[Animator]
    __ticking_animators: list[Animator]
    __engine_modules: dict[type[EngineModule], EngineModule]
    __ticking: bool

    def __init__(self):
        self.__active_animators = []
        self.__ticking_animators = []
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
        engine_type = type(engine_module_instance)
        if engine_type in self.__engine_modules:
            raise AnimationEngineError(
                f"An Engine Module of type '{engine_type.__name__}' has already been registered"
            )

        self.__engine_modules[engine_type] = engine_module_instance
        engine_module_instance.on_registered(self)

    def get_engine_module(self, script_engine_type: type[EngineModuleSubtype]) -> EngineModuleSubtype | None:
        return self.__engine_modules.get(script_engine_type, None)

    def add_active_animator(self, animator: Animator):
        if not animator in self.__active_animators:
            self.__active_animators.append(animator)

    def remove_active_animator(self, animator: Animator):
        if animator in self.__active_animators:
            self.__active_animators.remove(animator)

    def is_ticking(self):
        """ Returns if the ``AnimationEngine`` is currently processing a tick """
        return self.__ticking

    def get_ticking_animators(self):
        return copy(self.__ticking_animators)

    def tick(self, tick_rate: ticks_per_second) -> None:
        self.__ticking = True
        module_list = list(self.__engine_modules.values())

        for module in module_list:
            module.tick_pre_animation(tick_rate)

        # protect against list modification while iterating
        self.__ticking_animators = copy(self.__active_animators)
        self.__tick__update_animations(tick_rate, self.__ticking_animators)
        self.__tick__cleanup_finished_animations(self.__ticking_animators)
        self.__ticking_animators.clear()

        for module in module_list:
            module.tick_post_animation(tick_rate)

        self.__ticking = False

    def __tick__update_animations(self, tick_rate: ticks_per_second, anims_to_tick: list[Animator]) -> None:
        assert self.__ticking
        for animator in anims_to_tick:
            animator.tick_progress_all_anims(tick_rate)

    def __tick__cleanup_finished_animations(self, animators_to_tick: list[Animator]) -> None:
        for animator in animators_to_tick:
            # this may end up calling into unit scripts that were waiting on this animation
            animator.tick_handle_done_anims()
            if not animator.have_animations():
                self.remove_active_animator(animator)

    def notify_animation_finished(self, anim_key: AnimKey):
        for engine_module in self.__engine_modules.values():
            engine_module.notify_animation_finished(anim_key)
