import inspect
import logging
from copy import deepcopy
from typing import Final, overload, TypeAlias, Callable

from animation_engine import math
from animation_engine.anim_functions import (
    move_toward_target_position,
    turn_toward_target_rotation,
    spin_toward_target_velocity,
)
from animation_engine.exceptions import AnimationEngineError
from animation_engine.local_model import LocalModelPiece
from animation_engine.math import radians, ticks_per_second
from animation_engine.types_ import (
    Axis,
    AnimType,
    AnimInfo,
    ScriptPieceIndex,
    ModelPieceIndex,
    AnimKey,
)
from animation_engine.unit import Unit

_logger = logging.getLogger(__name__)

TickAnimFunc: TypeAlias = Callable[[int, LocalModelPiece, AnimInfo], bool]
"""
A function type for processing animations during a tick.

Parameters:

- tick_rate: int - The rate of ticks per second.
- piece: LocalModelPiece - The model piece being animated.
- anim: AnimInfo - The animation information.

Returns:

- bool: True if the animation is complete, False otherwise.
"""


class Animator:

    _unit: Unit
    _busy: bool

    _anims: dict[AnimKey, AnimInfo] = {}
    _done_anims: dict[AnimKey, AnimInfo] = {}

    from animation_engine.animation_engine import AnimationEngine
    main_engine: AnimationEngine

    def __init__(self, unit: Unit):
        self._unit = unit
        self.pieces = []

    def __del__(self):
        # remove all animations
        for anim_key in self._anims.keys():
            self._remove_anim(self._anims[anim_key])
        self._anims.clear()

    @overload
    def find_anim(self, anim_key: AnimKey) -> AnimInfo | None:
        pass

    @overload
    def find_anim(self, anim_type: AnimType, piece: ScriptPieceIndex, axis: Axis) -> AnimInfo | None:
        pass

    def find_anim(
        self, anim_type_or_key: AnimKey | AnimType, piece: ScriptPieceIndex = None, axis: Axis = None
    ) -> AnimInfo | None:
        if isinstance(anim_type_or_key, AnimKey):
            return self._anims.get(anim_type_or_key, None)
        elif isinstance(anim_type_or_key, AnimType) and piece is not None and axis is not None:
            return self._anims.get(AnimKey(anim_type_or_key, piece, axis), None)
        return None

    def _remove_anim(self, anim_info: AnimInfo | None) -> None:
        if anim_info is None:
            return

        if self._anims.get(anim_info.key, None) != anim_info:
            return

        # We need to unblock threads waiting on this animation, otherwise they will be lost in the void
        # NOTE: anim_finished might result in new anims being added
        self.anim_finished(anim_info.key)

        # no animations left? remove self from the list of active Animators
        if not self.have_animations():
            self.main_engine.remove_active_animator(self)

    def _add_anim(
        self,
        anim_type: AnimType,
        piece: ScriptPieceIndex,
        axis: Axis,
        target: float,
        velocity: float,
        accel: float = 0,
    ) -> None:

        velocity = math.abs(velocity)
        accel = math.abs(accel)

        if not self._piece_exists_guard(piece):
            return

        target_final = 0.0
        match anim_type:
            case AnimType.Move:
                target_final = target
            case AnimType.Turn:
                target_final = math.clamp_rad(target)

                # turn and spin animations are mutually exclusive
                self._remove_anim(self.find_anim(AnimType.Spin, piece, axis))
            case AnimType.Spin:
                target_final = math.clamp_rad(target)

                # turn and spin animations are mutually exclusive
                self._remove_anim(self.find_anim(AnimType.Turn, piece, axis))

        anim_info = self.find_anim(anim_type, piece, axis)

        if anim_info is None:
            if not self.have_animations():
                self.main_engine.add_active_animator(self)

            # create a new animation
            anim_info = AnimInfo(AnimKey(anim_type, piece, axis))
            self._anims[anim_info.key] = anim_info

        # update new/existing animation
        anim_info.target = target_final
        anim_info.velocity = velocity
        anim_info.accel = accel
        anim_info.done = False

    pieces: list[LocalModelPiece]

    def piece_exists(self, script_piece_num: ScriptPieceIndex) -> bool:
        return script_piece_num < len(self.pieces) and self.pieces[script_piece_num] is not None

    def _piece_exists_guard(self, script_piece_num: ScriptPieceIndex) -> bool:
        if not self.piece_exists(script_piece_num):
            func_name = inspect.currentframe().f_back.f_code.co_qualname
            _logger.error(
                "[%s] attempted to use invalid script piece index. Valid range: 0-%d, requested: %d",
                func_name, (len(self.pieces) - 1), script_piece_num,
            )
            return False
        return True

    def get_script_local_model_piece(self, script_piece_num: ScriptPieceIndex) -> LocalModelPiece:
        assert self.piece_exists(script_piece_num)
        return self.pieces[script_piece_num]

    def script_to_model(self, script_piece_num: ScriptPieceIndex) -> ModelPieceIndex | None:
        if not self._piece_exists_guard(script_piece_num):
            return None

        script_model_piece = self.get_script_local_model_piece(script_piece_num)
        return script_model_piece.get_model_piece_index()

    def model_to_script(self, local_model_piece_num: ModelPieceIndex) -> ScriptPieceIndex | None:
        local_model = self._unit.local_model

        if not local_model.has_piece(local_model_piece_num):
            return None

        return local_model.get_piece(local_model_piece_num).get_script_piece_index()

    def get_piece_pos(self, piece: ScriptPieceIndex) -> math.float3:
        if not self._piece_exists_guard(piece):
            return math.float3()

        lmp = self.get_script_local_model_piece(piece)
        return lmp.get_offset() + lmp.position

    def get_piece_matrix(self, piece: ScriptPieceIndex) -> math.matrix44:
        if not self._piece_exists_guard(piece):
            return math.matrix44()
        return deepcopy(self.get_script_local_model_piece(piece).model_space_matrix)

    def get_emit_dir_pos(self, piece: ScriptPieceIndex) -> tuple[math.float3, math.float3] | tuple[None, None]:
        if not self._piece_exists_guard(piece):
            return None, None
        return self.get_script_local_model_piece(piece).get_emit_dir_pos()

    def get_unit(self) -> Unit:
        return self._unit

    @staticmethod
    def tick_invalid_anim(tick_rate: ticks_per_second, lmp: LocalModelPiece, ai: AnimInfo) -> bool:
        raise AnimationEngineError(
            f"Invalid animation type {ai.key.anim_type} for piece {ai.key.piece} on axis {ai.key.axis} was attempted to be ticked"
        )

    @staticmethod
    def tick_move_anim(tick_rate: ticks_per_second, lmp: LocalModelPiece, ai: AnimInfo) -> bool:
        pos: math.float3 = lmp.position
        done, pos[ai.key.axis] = move_toward_target_position(
            pos[ai.key.axis], ai.target, ai.velocity,
            tick_rate
        )
        return done

    @staticmethod
    def tick_turn_anim(tick_rate: ticks_per_second, lmp: LocalModelPiece, ai: AnimInfo) -> bool:
        rot: math.radians3 = lmp.rotation
        rot[ai.key.axis] = math.clamp_rad(rot[ai.key.axis])
        done, rot[ai.key.axis] = turn_toward_target_rotation(
            rot[ai.key.axis], ai.target, ai.velocity,
            tick_rate
        )
        return done

    @staticmethod
    def tick_spin_anim(tick_rate: ticks_per_second, lmp: LocalModelPiece, ai: AnimInfo) -> bool:
        rot: math.radians3 = lmp.rotation
        done, rot[ai.key.axis], ai.velocity = spin_toward_target_velocity(
            rot[ai.key.axis], ai.velocity, ai.target, ai.accel,
            tick_rate
        )
        return done

    __TICK_ANIM_FUNCS: Final[dict[AnimType, TickAnimFunc]] = {
        AnimType.Turn: tick_turn_anim,
        AnimType.Spin: tick_spin_anim,
        AnimType.Move: tick_move_anim,
    }

    def tick_all_anims(self, tick_rate: ticks_per_second) -> None:
        """
        The multithreaded first half of the UnitScript.Tick function first does the heavy lifting of calculating all
        new piece positions according to the animations

        :param tick_rate: update rate
        """

        current_anim_items = list(self._anims.items())

        for anim_key, anim_info in current_anim_items:
            lmp = self.pieces[anim_info.key.piece]
            anim_func = self.__TICK_ANIM_FUNCS.get(anim_info.key.anim_type, Animator.tick_invalid_anim)
            anim_func(tick_rate, lmp, anim_info)
            if anim_info.done:
                self._done_anims[anim_key] = anim_info

    def tick_anim_finished(self) -> None:
        """
        Iterate over and clean up finished animations.

        As part of the iteration, we also notify the main engine that the animation is finished.

        This may result in new animations and unit script threads being added.
        """

        for done_anim_key in self._done_anims:
            self.anim_finished(done_anim_key)
        self._done_anims.clear()

    def spin(self, piece: ScriptPieceIndex, axis: Axis, target_velocity: float, accel: float) -> None:
        accel = math.abs(accel)

        anim_info = self.find_anim(AnimType.Spin, piece, axis)

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
            self._add_anim(AnimType.Spin, piece, axis, target_velocity, 0.0, accel)
        else:
            # snap to target_speed
            self._add_anim(AnimType.Spin, piece, axis, target_velocity, target_velocity, 0.0)

    def stop_spin(self, piece: ScriptPieceIndex, axis: Axis, decel: float) -> None:
        decel = math.abs(decel)

        anim_info = self.find_anim(AnimType.Spin, piece, axis)
        if anim_info is None:
            return

        if decel > 0.0:
            # decelerate to 0
            anim_info.dest = 0.0
            anim_info.accel = decel
        else:
            # instant stop
            self._remove_anim(anim_info)

    def turn(self, piece: ScriptPieceIndex, axis: Axis, target: float, velocity: float) -> None:
        self._add_anim(AnimType.Turn, piece, axis, math.clamp_rad(target), velocity)

    def move(self, piece: ScriptPieceIndex, axis: Axis, target: float, velocity: float) -> None:
        self._add_anim(AnimType.Move, piece, axis, target, velocity)

    def move_now(self, piece: ScriptPieceIndex, axis: Axis, dest: float) -> None:
        if not self._piece_exists_guard(piece):
            return
        self.pieces[piece].position[axis] = dest

    def turn_now(self, piece: ScriptPieceIndex, axis: Axis, dest: radians) -> None:
        if not self._piece_exists_guard(piece):
            return
        self.pieces[piece].rotation[axis] = math.clamp_rad(dest)

    def wait_on_anim(self, anim_key: AnimKey) -> bool:
        """
        Check if an animation is in progress and if so, set the waiting flag and return True.

        This is used by unit scripts to block/wait until the animation is finished.
        :param anim_key: The key of the animation to check for.
        :return: True if the animation is in progress and waiting was set, False otherwise.
        """
        anim_info = self.find_anim(anim_key)
        if anim_info is None:
            return False

        if anim_info.done:
            return False

        anim_info.has_waiting = True
        return True

    def set_visibility(self, piece: ScriptPieceIndex, visible: bool) -> None:
        if not self._piece_exists_guard(piece):
            return
        self.pieces[piece].set_script_visible(visible)

    #
    # def emit_sfx(self, sfx_type: int, sfx_piece: ScriptPieceIndex) -> bool:
    #     if not self.piece_exists_guard(sfx_piece):
    #         return False
    #
    #     # guaranteed to NOT return (None, None) as the piece exists
    #     rel_dir, rel_pos = cast(tuple[math.float3, math.float3], self.get_emit_dir_pos(sfx_piece))
    #     return self.emit_rel_sfx(sfx_type, rel_pos, math.normalize(rel_dir))
    #
    # def emit_rel_sfx(self, sfx_type: int, rel_pos: math.float3, rel_dir: math.float3) -> bool:
    #     obj_space_pos = self._unit.get_object_space_pos(rel_pos)
    #     obj_space_dir = self._unit.get_object_space_vec(rel_dir)
    #     return self.emit_abs_sfx(sfx_type, obj_space_pos, obj_space_dir, rel_dir)
    #
    # def emit_abs_sfx(
    #     self, sfx_type: int, abs_pos: math.float3, abs_dir: math.float3, rel_dir: math.float3 = math.FORWARD_VECTOR
    # ) -> bool:
    #     # renderer specific, leave a hook for something else to take care of it
    #     try:
    #         self.emit_sfx_subject.on_next((sfx_type, abs_pos, abs_dir, rel_dir))
    #     except Exception as ex:
    #         self._show_unit_script_error(f"emit_sfx handler threw an exception: {str(ex)}")
    #         return False
    #     return True

    def is_in_animation(self, anim_type: AnimType, piece: ScriptPieceIndex, axis: Axis) -> bool:
        return self.find_anim(anim_type, piece, axis) is not None

    def have_animations(self) -> bool:
        return len(self._anims) > 0

    def anim_finished(self, anim_key: AnimKey) -> None:
        self.main_engine.notify_animation_finished(self._unit, anim_key)
