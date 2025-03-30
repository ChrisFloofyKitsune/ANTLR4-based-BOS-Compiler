import inspect
from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import ClassVar, Final, cast

import reactivex

import cob.animation_engine.math as math
from cob.animation_engine.local_model_piece import LocalModelPiece
from cob.animation_engine.math import Radians
from cob.animation_engine.types import (
    AnimContainerType, AnimType, PieceIndex, AnimInfo,
    UnitId, ValueIndex, WeaponIndex, FunctionIndex, WeaponDefId,
    PieceIndex_NONE, ScriptPieceIndex, ModelPieceIndex, RadiansPerFrame, TickAnimFunc
)
from cob.animation_engine.unit import Unit


class UnitScript(ABC):
    needs_animating_subject: ClassVar[reactivex.Subject['UnitScript']] = reactivex.Subject()
    done_animating_subject: ClassVar[reactivex.Subject['UnitScript']] = reactivex.Subject()

    _unit: Unit
    _busy: bool

    _anims: list[AnimContainerType] = [AnimContainerType()] * (AnimType.AMove + 1)
    _done_anims: list[AnimContainerType] = [AnimContainerType()] * (AnimType.AMove + 1)

    _has_set_sfx_occupy: bool = False
    _has_rock_unit: bool = False
    _has_start_building: bool = False

    @staticmethod
    def _move_toward(cur: float, dest: float, speed: float) -> tuple[float, bool]:
        """
        Updates move animations
        :param cur: value to update
        :param dest: final value
        :param speed: max increment per tick
        :return: new position; True if destination is reached, False otherwise
        """
        delta = dest - cur

        if math.abs(delta) < speed:
            return dest, True

        return cur + (speed * math.sign(delta)), False

    @staticmethod
    def _turn_toward(cur: Radians, dest: Radians, speed: Radians) -> tuple[Radians, bool]:
        """
        Updates turn animations
        :param cur: value to update
        :param dest: final value
        :param speed: max increment per tick
        :return new rotation; True if destination was reached, False otherwise
        """
        assert 0 <= cur < math.TWO_PI, "current angle is out of bounds"
        assert 0 <= dest < math.TWO_PI, "destination angle is out of bounds"

        delta = math.modf(dest - cur + math.THREE_PI, math.TWO_PI) - math.PI

        if math.abs(delta) < speed:
            return dest, True

        return math.clamp_rad(cur + (speed * math.sign(delta))), False

    @staticmethod
    def _do_spin(cur: Radians, dest: Radians, speed: Radians, accel: RadiansPerFrame, divisor: int) -> tuple[
        Radians, Radians, bool]:
        """
        Updates spin animations
        :param cur: value to update
        :param dest: the final desired speed (NOT the final angle!)
        :param speed: is updated if it is not equal to dest
        :param accel: is the acceleration (or deceleration) to apply
        :param divisor: is the delta_time, it is not added before the call because speed may have to be updated
        :return: new rotation; new speed; True if desired speed is 0 and it is reached, False otherwise
        """
        delta = dest - speed

        # update speed
        if math.abs(delta) <= accel:
            speed = dest
        else:
            speed += accel * (math.SIM_SPEED * 1 / divisor) * math.sign(delta)

        # update angle
        cur = math.clamp_rad(cur + (speed / divisor))
        return cur, speed, (speed == dest == 0)

    def _find_anim(self, anim_type: AnimType, piece: ScriptPieceIndex, axis: math.Axis) -> AnimInfo | None:
        return next((ai for ai in self._anims[anim_type] if ai.piece == piece and ai.axis == axis), None)

    def _remove_anim(self, anim_type: AnimType, anim_info: AnimInfo) -> None:
        if anim_info not in self._anims[anim_type]:
            return

        # We need to unblock threads waiting on this animation, otherwise they will be lost in the void
        # NOTE: AnimFinished might result in new anims being added
        if anim_info.has_waiting:
            self.anim_finished(anim_type, anim_info.piece, anim_info.axis)

        idx = self._anims[anim_type].index(anim_info)
        self._anims[anim_type][idx] = self._anims[anim_type].pop()

        if self.have_animations():
            return

        self.done_animating_subject.on_next(self)

    def _add_anim(self, anim_type: AnimType, piece: ScriptPieceIndex, axis: math.Axis, speed: float, dest: float,
                  accel: RadiansPerFrame) -> None:
        if not self.piece_exists_guard(piece):
            return

        dest_final = 0.0
        match anim_type:
            case AnimType.AMove:
                dest_final = self.pieces[piece].get_original_offset()[axis] + dest
            case AnimType.ATurn:
                dest_final = dest

                # turn and spin animations are mutually exclusive
                if (existing_spin_anim := self._find_anim(AnimType.ASpin, piece, axis)) is not None:
                    self._remove_anim(AnimType.ASpin, existing_spin_anim)
            case AnimType.ASpin:
                dest_final = math.clamp_rad(dest)

                # turn and spin animations are mutually exclusive
                if (existing_turn_anim := self._find_anim(AnimType.ATurn, piece, axis)) is not None:
                    self._remove_anim(AnimType.ATurn, existing_turn_anim)

        anim_info = self._find_anim(anim_type, piece, axis)

        if anim_info is None:
            if not self.have_animations():
                self.needs_animating_subject.on_next(self)

            # create a new animation
            anim_info = AnimInfo()
            anim_info.axis = axis
            anim_info.piece = piece
            self._anims[anim_type].append(anim_info)

        # update new/existing animation
        anim_info.dest = dest_final
        anim_info.speed = speed
        anim_info.accel = accel
        anim_info.done = False

    @abstractmethod
    def _show_script_error(self, msg: str) -> None:
        pass

    def _show_unit_script_error(self, msg: str) -> None:
        self._show_script_error(f'error="{msg}"')

    pieces: list[LocalModelPiece]

    def piece_exists(self, script_piece_num: ScriptPieceIndex) -> bool:
        return script_piece_num < len(self.pieces) and self.pieces[script_piece_num] is not None

    def piece_exists_guard(self, script_piece_num: ScriptPieceIndex) -> bool:
        if not self.piece_exists(script_piece_num):
            func_name = inspect.currentframe().f_back.f_code.co_qualname
            self._show_unit_script_error(f'[{func_name}] invalid script piece index')
            return False
        return True

    def get_script_local_model_piece(self, script_piece_num: ScriptPieceIndex) -> LocalModelPiece:
        assert self.piece_exists(script_piece_num)
        return self.pieces[script_piece_num]

    def script_to_model(self, script_piece_num: ScriptPieceIndex) -> ModelPieceIndex:
        if not self.piece_exists(script_piece_num):
            return PieceIndex_NONE

        script_model_piece = self.get_script_local_model_piece(script_piece_num)
        return script_model_piece.get_local_model_piece_index()

    def model_to_script(self, local_model_piece_num: ModelPieceIndex) -> ScriptPieceIndex:
        local_model = self._unit.local_model

        if not local_model.has_piece(local_model_piece_num):
            return PieceIndex_NONE

        return local_model.get_piece(local_model_piece_num).get_script_piece_index()

    def get_piece_pos(self, piece: ScriptPieceIndex) -> math.float3:
        if not self.piece_exists(piece):
            return math.float3()
        return self.get_script_local_model_piece(piece).get_absolute_pos()

    def get_piece_matrix(self, piece: ScriptPieceIndex) -> math.matrix44:
        if not self.piece_exists(piece):
            return math.matrix44()
        return self.get_script_local_model_piece(piece).get_model_space_matrix()

    def get_emit_dir_pos(self, piece: ScriptPieceIndex) -> tuple[math.float3, math.float3] | tuple[None, None]:
        if not self.piece_exists_guard(piece):
            return None, None
        return self.get_script_local_model_piece(piece).get_emit_dir_pos()

    def __init__(self, unit: Unit):
        self._unit = unit
        self._busy = False
        self._has_set_sfx_occupy = False
        self._has_rock_unit = False
        self._has_start_building = False

        self.pieces = []

    @abstractmethod
    def __del__(self):
        if not self.have_animations():
            return

        self.done_animating_subject.on_next(self)

    def is_busy(self) -> bool:
        return self._busy

    def get_unit(self) -> Unit:
        return self._unit

    @staticmethod
    def tick_move_anim(tick_rate, lmp: LocalModelPiece, ai: AnimInfo) -> bool:
        pos: math.float3 = lmp.get_position()
        pos[ai.axis], done = UnitScript._move_toward(pos[ai.axis], ai.dest, ai.speed / tick_rate)
        lmp.set_position(pos)
        return done

    @staticmethod
    def tick_turn_anim(tick_rate: int, lmp: LocalModelPiece, ai: AnimInfo) -> bool:
        rot: math.Radians3 = lmp.get_rotation()
        rot[ai.axis] = math.clamp_rad(rot[ai.axis])
        rot[ai.axis], done = UnitScript._turn_toward(rot[ai.axis], ai.dest, ai.speed / tick_rate)
        lmp.set_rotation(rot)
        return done

    @staticmethod
    def tick_spin_anim(tick_rate: int, lmp: LocalModelPiece, ai: AnimInfo) -> bool:
        rot: math.Radians3 = lmp.get_rotation()
        rot[ai.axis] = math.clamp_rad(rot[ai.axis])
        rot[ai.axis], ai.speed, done = UnitScript._do_spin(rot[ai.axis], ai.dest, ai.speed, ai.accel, tick_rate)
        lmp.set_rotation(rot)
        return done

    __TICK_ANIM_FUNCS: Final[dict[AnimType, TickAnimFunc]] = {
        AnimType.ATurn: tick_turn_anim,
        AnimType.ASpin: tick_spin_anim,
        AnimType.AMove: tick_move_anim,
    }

    def tick_all_anims(self, delta_time: int) -> None:
        """
        The multithreaded first half of the UnitScript.Tick function first does the heavy lifting of calculating all
        new piece positions according to the animations

        :param delta_time: delta time to update
        """
        tick_rate: int = 1000 // delta_time
        for anim_type in (AnimType.ATurn, AnimType.ASpin, AnimType.AMove):
            current_anims = self._anims[anim_type]
            current_func = self.__TICK_ANIM_FUNCS[anim_type]
            current_done_anims = self._done_anims[anim_type]

            idx = 0
            while idx < len(current_anims):
                anim_info = current_anims[idx]
                lmp = self.pieces[anim_info.piece]

                anim_info.done = current_func(tick_rate, lmp, anim_info)
                if anim_info.done:
                    if anim_info.has_waiting:
                        current_done_anims.append(anim_info)

                    idx = current_anims.index(anim_info)
                    current_anims[idx] = self._anims[anim_type].pop()
                    continue
            idx += 1

    def tick_anim_finished(self, tick_rate: int) -> bool:
        """
        The single threaded second half of this function does the removal of finished animations,
        and it also is responsible for unblocking the listeners and returning whether we have animations or not.

        This is not multithreaded as it guarantees that AnimFinished will be called in consistent order for
        all anims for all participants of the simulation, and guarantees that the order of the animating
        vector in UnitScriptEngine.Tick is preserved.

        :param tick_rate: delta time to update
        :return: true if there are still active animations
        """

        # Tell listeners to unblock, and remove finished animations from the unit/script.
        for anim_type in (AnimType.ATurn, AnimType.ASpin, AnimType.AMove):
            current_done_anims = self._done_anims[anim_type]
            for anim_info in current_done_anims:
                self.anim_finished(anim_type, anim_info.piece, anim_info.axis)
            current_done_anims.clear()

        return self.have_animations()

    def spin(self, piece: ScriptPieceIndex, axis: math.Axis, speed: float, accel: float) -> None:
        anim_info = self._find_anim(AnimType.ASpin, piece, axis)

        # alter existing animation
        if anim_info is not None:
            anim_info.dest = speed

            if accel > 0.0:
                anim_info.accel = accel
            else:
                anim_info.speed = speed
                anim_info.accel = 0.0
            return

        # create a new animation
        if accel <= 0.0:
            self._add_anim(AnimType.ASpin, piece, axis, speed, speed, 0.0)
        else:
            self._add_anim(AnimType.ASpin, piece, axis, 0.0, speed, accel)

    def stop_spin(self, piece: ScriptPieceIndex, axis: math.Axis, decel: float) -> None:
        anim_info = self._find_anim(AnimType.ASpin, piece, axis)

        if anim_info is None:
            return

        if decel <= 0.0:
            # instant stop
            self._remove_anim(AnimType.ASpin, anim_info)
        else:
            # decelerate to 0
            anim_info.dest = 0.0
            anim_info.accel = decel

    def turn(self, piece: ScriptPieceIndex, axis: math.Axis, speed: float, dest: float) -> None:
        self._add_anim(AnimType.ATurn, piece, axis, speed, math.clamp_rad(dest), 0.0)

    def move(self, piece: ScriptPieceIndex, axis: math.Axis, speed: float, dest: float) -> None:
        self._add_anim(AnimType.AMove, piece, axis, math.abs(speed), dest, 0.0)

    def move_now(self, piece: ScriptPieceIndex, axis: math.Axis, dest: float) -> None:
        if not self.piece_exists_guard(piece):
            return

        lmp = self.pieces[piece]

        pos = lmp.get_position()
        offset = lmp.get_original_offset()

        pos[axis] = offset[axis] + dest

        lmp.set_position(pos)

    def turn_now(self, piece: ScriptPieceIndex, axis: math.Axis, dest: Radians) -> None:
        if not self.piece_exists_guard(piece):
            return

        lmp = self.pieces[piece]

        rot = lmp.get_rotation()
        rot[axis] = math.clamp_rad(dest)

        lmp.set_rotation(rot)

    def needs_wait(self, anim_type: AnimType, piece: ScriptPieceIndex, axis: math.Axis) -> bool:
        anim_info = self._find_anim(anim_type, piece, axis)
        if anim_info is None:
            return False

        if anim_info.done:
            return False

        anim_info.has_waiting = True
        return True

    def set_visibility(self, piece: ScriptPieceIndex, visible: bool) -> None:
        if not self.piece_exists_guard(piece):
            return
        self.pieces[piece].set_script_visible(visible)

    def emit_sfx(self, sfx_type: int, sfx_piece: ScriptPieceIndex) -> bool:
        if not self.piece_exists_guard(sfx_piece):
            return False

        # guaranteed to NOT return (None, None) as the piece exists
        rel_dir, rel_pos = cast(tuple[math.float3, math.float3], self.get_emit_dir_pos(sfx_piece))
        return self.emit_rel_sfx(sfx_type, rel_pos, math.normalize(rel_dir))

    def emit_rel_sfx(self, sfx_type: int, rel_pos: math.float3, rel_dir: math.float3) -> bool:
        obj_space_pos = self._unit.get_object_space_pos(rel_pos)
        obj_space_dir = self._unit.get_object_space_vec(rel_dir)
        return self.emit_abs_sfx(sfx_type, obj_space_pos, obj_space_dir, rel_dir)

    emit_sfx_subject: ClassVar[reactivex.Subject] = reactivex.Subject()

    def emit_abs_sfx(
            self, sfx_type: int,
            abs_pos: math.float3, abs_dir: math.float3,
            rel_dir: math.float3 = math.FORWARD_VECTOR
    ) -> bool:
        # renderer specific, leave a hook for something else to take care of it
        try:
            self.emit_sfx_subject.on_next((sfx_type, abs_pos, abs_dir, rel_dir))
        except Exception as ex:
            self._show_unit_script_error(f'emit_sfx handler threw an exception: {str(ex)}')
            return False
        return True

    def attach_unit(self, piece: ScriptPieceIndex, unit: UnitId) -> None:
        # -1 here means that the unit should be completely hidden
        if not (piece == -1 or self.piece_exists_guard(piece)):
            return
        return self._attach_unit_impl(piece, unit)

    @abstractmethod
    def _attach_unit_impl(self, piece: ScriptPieceIndex, unit: UnitId) -> None:
        raise NotImplementedError

    def drop_unit(self, unit: UnitId) -> None:
        self._drop_unit_impl(unit)

    @abstractmethod
    def _drop_unit_impl(self, unit: UnitId) -> None:
        raise NotImplementedError

    def explode(self, piece: ScriptPieceIndex, flags: int) -> None:
        if not self.piece_exists_guard(piece):
            return
        self._explode_impl(piece, flags)

    @abstractmethod
    def _explode_impl(self, piece: ScriptPieceIndex, flags: int) -> None:
        raise NotImplementedError

    def shatter(self, piece: ScriptPieceIndex, pos: math.float3, speed: math.float3) -> None:
        if not self.piece_exists_guard(piece):
            return
        self._shatter_impl(piece, pos, speed)

    @abstractmethod
    def _shatter_impl(self, piece: ScriptPieceIndex, pos: math.float3, speed: math.float3) -> None:
        raise NotImplementedError

    def show_flare(self, piece: ScriptPieceIndex) -> None:
        if not self.piece_exists_guard(piece):
            return
        self._show_flare_impl(piece)

    @abstractmethod
    def _show_flare_impl(self, piece: ScriptPieceIndex) -> None:
        raise NotImplementedError

    def get_unit_val(self, val: ValueIndex, p1: int, p2: int, p3: int, p4: int) -> int:
        return self._get_unit_val_impl(val, p1, p2, p3, p4)

    @abstractmethod
    def _get_unit_val_impl(self, val: ValueIndex, p1: int, p2: int, p3: int, p4: int) -> int:
        raise NotImplementedError

    def set_unit_val(self, val: ValueIndex, param: int):
        self._set_unit_val_impl(val, param)

    @abstractmethod
    def _set_unit_val_impl(self, val: ValueIndex, param: int) -> None:
        raise NotImplementedError

    def is_in_animation(self, anim_type: AnimType, piece: ScriptPieceIndex, axis: math.Axis) -> bool:
        return self._find_anim(anim_type, piece, axis) is not None

    def have_animations(self) -> bool:
        return any(
            len(self._anims[anim_type]) > 0
            for anim_type in (AnimType.ATurn, AnimType.ASpin, AnimType.AMove)
        )

    def has_set_sfx_occupy(self) -> bool:
        return self._has_set_sfx_occupy

    def has_rock_unit(self) -> bool:
        return self._has_rock_unit

    def has_start_building(self) -> bool:
        return self._has_start_building

    # region: call-ins

    @abstractmethod
    def has_block_shot(self, weapon_num: WeaponIndex) -> bool:
        return False

    @abstractmethod
    def has_target_weight(self, weapon_num: WeaponIndex) -> bool:
        return False

    @abstractmethod
    def raw_call(self, function_id: FunctionIndex) -> None:
        raise NotImplementedError

    @abstractmethod
    def create(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def killed(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def wind_changed(self, heading: float, speed: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def extraction_rate_changed(self, speed: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def world_rock_unit(self, rock_dir: math.float3) -> None:
        raise NotImplementedError

    @abstractmethod
    def rock_unit(self, rock_dir: math.float3) -> None:
        raise NotImplementedError

    @abstractmethod
    def world_hit_by_weapon(self, hit_dir: math.float3, weapon_def_id: WeaponDefId, damage: float) -> float:
        raise NotImplementedError

    @abstractmethod
    def hit_by_weapon(self, hit_dir: math.float3, weapon_def_id: WeaponDefId, damage: float) -> float:
        raise NotImplementedError

    @abstractmethod
    def set_sfx_occupy(self, cur_terrain_type: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def query_landing_pads(self) -> Sequence[PieceIndex]:
        raise NotImplementedError

    @abstractmethod
    def begin_transport(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def query_transport(self) -> PieceIndex:
        raise NotImplementedError

    @abstractmethod
    def transport_pickup(self, unit: UnitId) -> None:
        raise NotImplementedError

    @abstractmethod
    def transport_drop(self, unit: UnitId, pos: math.float3) -> None:
        raise NotImplementedError

    @abstractmethod
    def start_building_direction(self, heading: float, pitch: float) -> None:
        raise NotImplementedError

    @abstractmethod
    def query_nano_piece(self) -> PieceIndex:
        raise NotImplementedError

    @abstractmethod
    def query_build_info(self) -> PieceIndex:
        raise NotImplementedError

    @abstractmethod
    def destroy(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def start_moving(self, reversing: bool) -> None:
        raise NotImplementedError

    @abstractmethod
    def stop_moving(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def start_skidding(self, velocity: math.float3) -> None:
        raise NotImplementedError

    @abstractmethod
    def stop_skidding(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def change_heading(self, delta_heading: Radians) -> None:
        raise NotImplementedError

    @abstractmethod
    def start_unload(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def end_transport(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def start_building(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def stop_building(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def falling(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def landed(self) -> None:
        pass

    @abstractmethod
    def activate(self) -> None:
        pass

    @abstractmethod
    def deactivate(self) -> None:
        pass

    @abstractmethod
    def move_rate(self, cur_rate: int) -> None:
        pass

    @abstractmethod
    def fire_weapon(self, weapon_num: WeaponIndex) -> None:
        pass

    @abstractmethod
    def end_burst(self, weapon_num: WeaponIndex) -> None:
        pass

    # endregion: call-ins

    # region: weapon call-ins
    @abstractmethod
    def query_weapon(self, weapon_num: WeaponIndex) -> PieceIndex:
        raise NotImplementedError

    @abstractmethod
    def aim_weapon(self, weapon_num: WeaponIndex, heading: Radians, pitch: Radians) -> None:
        raise NotImplementedError

    @abstractmethod
    def aim_shield_weapon(self, weapon_num: WeaponIndex) -> None:
        raise NotImplementedError

    @abstractmethod
    def aim_from_weapon(self, weapon_num: WeaponIndex) -> PieceIndex:
        raise NotImplementedError

    @abstractmethod
    def shot(self, weapon_num: WeaponIndex) -> None:
        raise NotImplementedError

    @abstractmethod
    def block_shot(self, weapon_num: WeaponIndex, target_unit: Unit) -> None:
        raise NotImplementedError

    @abstractmethod
    def target_weight(self, weapon_num: WeaponIndex, target_unit: Unit) -> float:
        raise NotImplementedError

    @abstractmethod
    def anim_finished(self, anim_type: AnimType, piece: PieceIndex, axis: math.Axis) -> None:
        raise NotImplementedError
