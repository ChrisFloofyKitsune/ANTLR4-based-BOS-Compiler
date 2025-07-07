import logging
from collections.abc import Callable
from typing import Final, TYPE_CHECKING, Generic

from animation_engine import math
from animation_engine.anim_functions import (
    move_toward_target_position,
    turn_toward_target_rotation,
    spin_toward_target_velocity,
)
from animation_engine.data_types import (
    Axis,
    AnimType,
    AnimInfo,
    AnimKey, TransformSubtype,
)
from animation_engine.exceptions import AnimationEngineError
from animation_engine.math import radians, ticks_per_second, radians3, float3

if TYPE_CHECKING:
    from animation_engine.animation_engine import AnimationEngine

_logger = logging.getLogger(__name__)


class Animator(Generic[TransformSubtype]):
    _anims: dict[AnimKey[TransformSubtype], AnimInfo] = {}
    _done_anims: set[AnimKey[TransformSubtype]] = set()

    from animation_engine.animation_engine import AnimationEngine
    _animation_engine: AnimationEngine

    def __init__(self, animation_engine: AnimationEngine):
        self._animation_engine = animation_engine

    def __del__(self):
        # remove all animations
        for anim_key in self._anims.keys():
            self._remove_anim(anim_key)
        self._anims.clear()

    def find_anim(self, anim_key: AnimKey[TransformSubtype]) -> AnimInfo | None:
        return self._anims.get(anim_key, None)

    def _remove_anim(self, anim_key: AnimKey) -> None:
        anim_info = self.find_anim(anim_key)
        if anim_info is None:
            return

        del self._anims[anim_key]

        if anim_info.has_waiting:
            self._animation_engine.notify_animation_finished(anim_key)

        # remove self from active animators if this happened outside a tick update somehow
        if not self._animation_engine.is_ticking() and not self.have_animations():
            self._animation_engine.remove_active_animator(self)

    def _add_anim(
        self,
        anim_key: AnimKey,
        target: float,
        velocity: float,
        accel: float = 0,
    ) -> None:
        piece_index, anim_type, axis = anim_key

        velocity = math.abs(velocity)
        accel = math.abs(accel)

        target_final = 0.0
        match anim_type:
            case AnimType.Move:
                target_final = target
            case AnimType.Turn:
                target_final = math.clamp_rad(target)

                # turn and spin animations are mutually exclusive
                self._remove_anim(AnimKey(piece_index, AnimType.Spin, axis))
            case AnimType.Spin:
                target_final = math.clamp_rad(target)

                # turn and spin animations are mutually exclusive
                self._remove_anim(AnimKey(piece_index, AnimType.Turn, axis))

        anim_info = self.find_anim(anim_key)

        if anim_info is None:
            if not self.have_animations():
                self._animation_engine.add_active_animator(self)

            # create a new animation
            anim_info = AnimInfo(anim_key)
            self._anims[anim_info.key] = anim_info

        # update new/existing animation
        anim_info.target = target_final
        anim_info.velocity = velocity
        anim_info.accel = accel
        anim_info.done = False

    @staticmethod
    def tick_invalid_anim(tick_rate: ticks_per_second, ai: AnimInfo) -> bool:
        raise AnimationEngineError(
            f"Invalid animation type {ai.key.anim_type} for transform {ai.key.transform} on axis {ai.key.axis} was attempted to be ticked"
        )

    @staticmethod
    def tick_move_anim(tick_rate: ticks_per_second, ai: AnimInfo) -> None:
        pos: math.float3 = ai.key.transform.position
        ai.done, pos[ai.key.axis] = move_toward_target_position(
            pos[ai.key.axis], ai.target, ai.velocity,
            tick_rate
        )
        ai.key.transform.position = pos

    @staticmethod
    def tick_turn_anim(tick_rate: ticks_per_second, ai: AnimInfo) -> None:
        rot: math.radians3 = ai.key.transform.rotation
        rot[ai.key.axis] = math.clamp_rad(rot[ai.key.axis])
        ai.done, rot[ai.key.axis] = turn_toward_target_rotation(
            rot[ai.key.axis], ai.target, ai.velocity,
            tick_rate
        )

    @staticmethod
    def tick_spin_anim(tick_rate: ticks_per_second, ai: AnimInfo) -> None:
        rot: math.radians3 = ai.key.transform.rotation
        ai.done, rot[ai.key.axis], ai.velocity = spin_toward_target_velocity(
            rot[ai.key.axis], ai.velocity, ai.target, ai.accel,
            tick_rate
        )
        ai.key.transform.rotation = rot

    __TICK_ANIM_FUNCS: Final[dict[AnimType, Callable[[ticks_per_second, AnimInfo], None]]] = {
        AnimType.Turn: tick_turn_anim,
        AnimType.Spin: tick_spin_anim,
        AnimType.Move: tick_move_anim,
    }

    def tick_progress_all_anims(self, tick_rate: ticks_per_second) -> None:
        """Progress all currently active animations as part of a fixed-update loop

        Parameters
        ----------
            tick_rate: ticks_per_second
                The rate of ticks per second, used to calculate the progress of animations. Should always be the same value.
        """

        current_anim_items = list(self._anims.items())

        for anim_key, anim_info in current_anim_items:
            anim_func = self.__TICK_ANIM_FUNCS.get(anim_info.key.anim_type, Animator.tick_invalid_anim)
            anim_func(tick_rate, anim_info)
            if anim_info.done:
                self._done_anims.add(anim_key)

    def tick_handle_done_anims(self) -> None:
        """
        Iterate over and clean up finished animations.

        As part of the iteration, we also notify the main engine that the animation is finished.

        This may result in new animations and unit script threads being added.
        """

        for done_anim_key in self._done_anims:
            self._remove_anim(done_anim_key)
        self._done_anims.clear()

    def spin(self, transform: TransformSubtype, axis: Axis, target_velocity: float, accel: float) -> None:
        accel = math.abs(accel)
        anim_info = self.find_anim(AnimKey(transform, AnimType.Spin, axis))

        # alter existing animation
        if anim_info is not None:
            anim_info.dest = target_velocity

            if accel > 0.0:
                anim_info.accel = accel
            else:
                anim_info.velocity = target_velocity
                anim_info.accel = 0.0
            return

        # create a new animation
        if accel > 0.0:
            # accelerate to target speed
            self._add_anim(AnimKey(transform, AnimType.Spin, axis), target_velocity, 0.0, accel)
        else:
            # snap to target_speed
            self._add_anim(AnimKey(transform, AnimType.Spin, axis), target_velocity, target_velocity, 0.0)

    def stop_spin(self, transform: TransformSubtype, axis: Axis, decel: float) -> None:
        decel = math.abs(decel)
        anim_key = AnimKey(transform, AnimType.Spin, axis)

        anim_info = self.find_anim(anim_key)
        if anim_info is None:
            return

        if decel > 0.0:
            # decelerate to 0
            anim_info.dest = 0.0
            anim_info.accel = decel
        else:
            # instant stop
            self._remove_anim(anim_key)

    def turn(self, transform: TransformSubtype, axis: Axis, target: radians, velocity: radians) -> None:
        """Turn the transform to the target rotation with a specified velocity."""
        self._add_anim(AnimKey(transform, AnimType.Turn, axis), math.clamp_rad(target), velocity)

    def turn_3d(self, transform: TransformSubtype, target: radians3, velocity: radians | radians3) -> None:
        """Turn the transform to the target rotation with a specified velocity."""
        if not isinstance(velocity, radians3):
            velocity = radians3(velocity)

        for axis in Axis:
            self.turn(transform, target[axis], velocity[axis])

    def turn_now(self, transform: TransformSubtype, axis: Axis, dest: radians) -> None:
        """Turn the transform to the target rotation immediately, without animation."""
        self._remove_anim(AnimKey(transform, AnimType.Turn, axis))
        transform.rotation[axis] = math.clamp_rad(dest)

    def turn_now_3d(self, transform: TransformSubtype, dest: radians3) -> None:
        """Turn the transform to the target rotation immediately, without animation."""
        for axis in Axis:
            self.turn_now(transform, axis, dest[axis])

    def move(self, transform: TransformSubtype, axis: Axis, target: float, velocity: float) -> None:
        """Move the transform to the target position with a specified velocity."""
        self._add_anim(AnimKey(transform, AnimType.Move, axis), target, velocity)

    def move_3d(self, transform: TransformSubtype, target: float3, velocity: float | float3) -> None:
        """Move the transform to the target position with a specified velocity."""
        if not isinstance(velocity, float3):
            velocity = float3(velocity)

        for axis in Axis:
            self.move(transform, axis, target[axis], velocity[axis])

    def move_now(self, transform: TransformSubtype, axis: Axis, dest: float) -> None:
        """Move the transform to the target position immediately, without animation."""
        self._remove_anim(AnimKey(transform, AnimType.Move, axis))
        transform.position[axis] = dest

    def move_now_3d(self, transform: TransformSubtype, dest: float3) -> None:
        """Move the transform to the target position immediately, without animation."""
        for axis in Axis:
            self.move_now(transform, axis, dest[axis])

    def wait_on_anim(self, anim_key: AnimKey) -> bool:
        """Check if an animation is in progress and if so, set the waiting flag and return True.

        This is used by engine modules to block/wait until the animation is finished.
        ``AnimationEngine.notify_animation_finished`` will now be called later.

        Parameters
        ----------
        anim_key: AnimKey
            The key of the animation to check for.

        Returns
        -------
        bool
            True if the animation is in progress and waiting was set, False otherwise.
        """
        anim_info = self.find_anim(anim_key)
        if anim_info is None:
            return False

        if anim_info.done:
            return False

        anim_info.has_waiting = True
        return True

    def is_transform_in_animation(self, transform: TransformSubtype) -> bool:
        return len(self.get_transform_animations(transform)) > 0

    def get_transform_animations(self, transform: TransformSubtype) -> list[AnimInfo[TransformSubtype]]:
        return list(self._anims[anim_key] for anim_key in self._anims if anim_key.transform == transform)

    def have_animations(self) -> bool:
        return len(self._anims) > 0

