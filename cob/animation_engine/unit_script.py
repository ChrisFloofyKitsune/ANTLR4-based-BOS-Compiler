from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import ClassVar

import reactivex

import cob.animation_engine.math as math
from cob.animation_engine.local_model_piece import LocalModelPiece
from cob.animation_engine.math import Radians
from cob.animation_engine.types import (
    AnimContainerType, AnimType, PieceIndex, AnimInfo,
    UnitId, ValueIndex, WeaponIndex, FunctionIndex, WeaponDefId,
    PieceIndex_NONE, ScriptPieceIndex, ModelPieceIndex, RadiansPerFrame
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

    def _find_anim(self, anim_type: AnimType, piece: PieceIndex, axis: math.Axis) -> AnimInfo | None:
        return next((ai for ai in self._anims[anim_type] if ai.piece == piece and ai.axis == axis), None)

    def _remove_anim(self, anim_type: AnimType, anim_info: AnimInfo) -> None:
        if not anim_info in self._anims[anim_type]:
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
        if not self.piece_exists(piece):
            self._show_unit_script_error('[UnitScript.add_anim] invalid script piece index')
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

    def get_emit_dir_pos(self, piece: ScriptPieceIndex) -> tuple[math.float3, math.float3]:
        if not self.piece_exists(piece):
            return math.float3(), math.float3()
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

    def tick_all_anims(self, tick_rate: int) -> None:
        """
        The multithreaded first half of the UnitScript.Tick function first does the heavy lifting of calculating all
        new piece positions according to the animations

        :param tick_rate: delta time to update
        """
        pass

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

        pass

    def tick_move_anim(self, tick_rate, lmp: LocalModelPiece, ai: AnimInfo) -> bool:
        pos: math.float3 = lmp.get_position()
        pos[ai.axis], done = self._move_toward(pos[ai.axis], ai.dest, ai.speed / tick_rate)
        lmp.set_position(pos)
        return done

    def tick_turn_anim(self, tick_rate: int, lmp: LocalModelPiece, ai: AnimInfo) -> bool:
        rot: math.Radians3 = lmp.get_rotation()
        rot[ai.axis] = math.clamp_rad(rot[ai.axis])
        rot[ai.axis], done = self._turn_toward(rot[ai.axis], ai.dest, ai.speed / tick_rate)
        lmp.set_rotation(rot)
        return done

    def tick_spin_anim(self, tick_rate: int, lmp: LocalModelPiece, ai: AnimInfo) -> bool:
        rot: math.Radians3 = lmp.get_rotation()
        rot[ai.axis] = math.clamp_rad(rot[ai.axis])
        rot[ai.axis], ai.speed, done = self._do_spin(rot[ai.axis], ai.dest, ai.speed, ai.accel, tick_rate)
        lmp.set_rotation(rot)
        return done

    def spin(self, piece: PieceIndex, axis: math.Axis, speed: float, accel: float) -> None:
        pass

    def stop_spin(self, piece: PieceIndex, axis: math.Axis, decel: float) -> None:
        pass

    def turn(self, piece: PieceIndex, axis: math.Axis, speed: float, dest: float) -> None:
        pass

    def move(self, piece: PieceIndex, axis: math.Axis, speed: float, dest: float) -> None:
        pass

    def move_now(self, piece: PieceIndex, axis: math.Axis, dest: float) -> None:
        pass

    def turm_now(self, piece: PieceIndex, axis: math.Axis, dest: float) -> None:
        pass

    def needs_wait(self, anim_type: AnimType, piece: PieceIndex, axis: math.Axis) -> bool:
        pass

    def set_visibility(self, piece: PieceIndex, visible: bool) -> None:
        pass

    def emit_sfx(self, sfx_type: int, sfx_piece: PieceIndex) -> bool:
        pass

    def emit_rel_sfx(self, sfx_type: int, rel_pos: math.float3, rel_dir: math.float3) -> bool:
        pass

    def emit_abs_sfx(self, sfx_type: int, abs_pos: math.float3, abs_dir: math.float3,
                     rel_dir: math.float3 = math.FORWARD_VECTOR) -> bool:
        pass

    def attach_unit(self, piece: PieceIndex, unit: UnitId) -> None:
        pass

    def drop_unit(self, unit: UnitId) -> None:
        pass

    def explode(self, piece: PieceIndex, flags: int) -> None:
        pass

    def shatter(self, piece: PieceIndex, pos: math.float3, speed: math.float3) -> None:
        pass

    def show_flare(self, piece: PieceIndex) -> None:
        pass

    def get_unit_val(self, val: ValueIndex, p1: int, p2: int, p3: int, p4: int) -> int:
        pass

    def set_unit_val(self, val: ValueIndex, param: int):
        pass

    def is_in_animation(self, anim_type: AnimType, piece: PieceIndex, axis: math.Axis) -> bool:
        return self._find_anim(anim_type, piece, axis) is not None

    def have_animations(self) -> bool:
        return any(self._anims[anim_type] for anim_type in (AnimType.ATurn, AnimType.ASpin, AnimType.AMove))

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
