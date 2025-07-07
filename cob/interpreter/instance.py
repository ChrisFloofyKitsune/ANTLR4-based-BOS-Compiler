from typing import override, Sequence

from cob.cob_file import CobFile
from cob.interpreter.thread import CobThread
from cob.interpreter.types_ import ThreadCallbackType
from script_hook_function import ScriptHookFunction
from animation_engine.math import uint32, MAX_COB_ARGS, float3
from animation_engine.data_types import (
    WeaponIndex, FunctionIndex, WeaponDefId, AnimatorPieceIndex, UnitId, ValueIndex,
    AnimType, Axis,
)
from animation_engine.unit import Unit


class CobInstance(UnitScript):

    def _map_script_to_model_pieces(self, local_model: LocalModel) -> None:
        pass

    @override
    def _show_script_error(self, msg: str) -> None:
        pass

    cob_file: CobFile

    static_vars: list[uint32]

    thread_ids: list[int]

    def __init__(self, cob_file: CobFile, unit: Unit):
        super().__init__(unit)
        self.cob_file = cob_file

        self._map_script_to_model_pieces(unit.local_model)

        self._has_set_sfx_occupy = self.has_function(ScriptHookFunction.SET_SFX_OCCUPY)
        self._has_rock_unit = self.has_function(ScriptHookFunction.ROCK_UNIT)
        self._has_start_building = self.has_function(ScriptHookFunction.START_BUILDING)

        self.static_vars.clear()
        self.static_vars.extend([uint32(0)] * cob_file.static_var_count)

    @override
    def __del__(self):
        pass

    def has_function(self, script_function: ScriptHookFunction):
        return script_function in self.cob_file.script_function_index

    def add_thread_id(self, thread_id: int) -> None:
        self.thread_ids.append(thread_id)

    def remove_thread_id(self, thread_id: int) -> None:
        if thread_id in self.thread_ids:
            self.thread_ids.remove(thread_id)

    @override
    def has_block_shot(self, weapon_num: WeaponIndex) -> bool:
        return self.has_function(ScriptHookFunction.block_shot(weapon_num))

    @override
    def has_target_weight(self, weapon_num: WeaponIndex) -> bool:
        return self.has_function(ScriptHookFunction.target_weight(weapon_num))

    def call(
        self, function: ScriptHookFunction, args: list[int] = None, cb: ThreadCallbackType = None, cb_param: int = None
    ) -> int:
        function_id = function.func_id
        return self._real_call(function_id, args or [], cb or ThreadCallbackType.CBNone, cb_param or 0)

    @override
    def raw_call(self, function_id: FunctionIndex, args: list[int] = None) -> None:
        self._real_call(function_id, args or [], ThreadCallbackType.CBNone, 0)

    def _real_call(self, function_id: FunctionIndex, args: list[int], cb: ThreadCallbackType, cb_param: int) -> int:
        if len(args) < MAX_COB_ARGS:
            args.extend([0] * (MAX_COB_ARGS - len(args)))

        if function_id < 0 or function_id >= len(self.cob_file.function_map):
            # function doesn't exist, but the callback should still be called`
            if cb != ThreadCallbackType.CBNone:
                self.thread_callback(cb, -1, cb_param)
                return -1

        new_cob_thread = CobThread(self)
        new_cob_thread.set_id(CobInstance.cob_engine.generate_thread_id())

        if cb != ThreadCallbackType.CBNone:
            new_cob_thread.set_callback(cb, cb_param)

        new_cob_thread.start(function_id, args, False)
        new_cob_thread.Tick()

        try:
            if new_cob_thread.is_dead():
                # thread completed in one tick, process the results
                num_args = args[0]
                ret_args = new_cob_thread.check_stack(
                    num_args, function_id != self.cob_file.script_function_index[ScriptHookFunction.START_MOVING]
                )

                # retrieve out parameters
                for i in range(MAX_COB_ARGS):
                    if i < ret_args:
                        args[i] = new_cob_thread.get_stack_val(i)
                    else:
                        args[i] = 0

                # stop the thread, triggering the callback
                new_cob_thread.stop()
                return new_cob_thread.get_ret_code() or 0
            else:
                # thread still needs to run, add it to the queue
                self.cob_engine.add_thread(new_cob_thread)
                return 1
        finally:
            # handle any spawned threads
            self.cob_engine.process_queued_threads()

    @override
    def create(self) -> None:
        pass

    @override
    def killed(self) -> None:
        pass

    @override
    def wind_changed(self, heading: float, speed: float) -> None:
        pass

    @override
    def extraction_rate_changed(self, speed: float) -> None:
        pass

    @override
    def world_rock_unit(self, rock_dir: float3) -> None:
        pass

    @override
    def rock_unit(self, rock_dir: float3) -> None:
        pass

    @override
    def world_hit_by_weapon(self, hit_dir: float3, weapon_def_id: WeaponDefId, damage: float) -> float:
        pass

    @override
    def hit_by_weapon(self, hit_dir: float3, weapon_def_id: WeaponDefId, damage: float) -> float:
        pass

    @override
    def set_sfx_occupy(self, cur_terrain_type: int) -> None:
        pass

    @override
    def query_landing_pads(self) -> Sequence[AnimatorPieceIndex]:
        pass

    @override
    def begin_transport(self) -> None:
        pass

    @override
    def _attach_unit_impl(self, piece: AnimatorPieceIndex, unit: UnitId) -> None:
        pass

    @override
    def _drop_unit_impl(self, unit: UnitId) -> None:
        pass

    @override
    def _explode_impl(self, piece: AnimatorPieceIndex, flags: int) -> None:
        pass

    @override
    def _shatter_impl(self, piece: AnimatorPieceIndex, pos: float3, speed: float3) -> None:
        pass

    @override
    def _show_flare_impl(self, piece: AnimatorPieceIndex) -> None:
        pass

    @override
    def _get_unit_val_impl(self, val: ValueIndex, p1: int, p2: int, p3: int, p4: int) -> int:
        pass

    @override
    def _set_unit_val_impl(self, val: ValueIndex, param: int) -> None:
        pass

    @override
    def perform_call_in(self, script_hook_function: ScriptHookFunction, args: list[uint32]) -> list[uint32]:
        function_id = self.cob_file.get_function_id(script_hook_function)
        raise NotImplementedError()

    @override
    def anim_finished(self, anim_type: AnimType, piece: AnimatorPieceIndex, axis: Axis) -> None:
        pass
