from array import array
from enum import Enum, auto
from typing import Self

from cob.animation_engine.unit_script import AnimType
from cob.cob_file import CobFile


class CobThread:

    class State(Enum):
        Init = auto()
        Sleep = auto()
        Run = auto()
        WaitTurn = auto()
        WaitMove = auto()

    def __init__(self):
        pass

    def __del__(self):
        pass

    # def __copy__(self, other: Self):
    #     pass
    #
    # def __deepcopy__(self, other: Self):
    #     pass

    def tick(self) -> bool:
        pass

    def start(self, function_id: int, sig_mask: int, args: list[int], schedule: bool) -> None:
        pass

    def stop(self) -> None:
        pass

    def set_id(self, thread_id: int) -> None:
        pass

    def set_state(self, state: State) -> None:
        pass

    def set_callback(self, cb: CobInstance.ThreadCallbackType, cbp: int) -> None:
        pass

    def check_stack(self, size: int, warn: bool) -> int:
        pass

    def init_stack(self, n: int, t: Self) -> None:
        pass

    def show_error(self, msg: str) -> None:
        pass

    def anim_finished(self, type: AnimType, piece: int, axis: int) -> None:
        pass

    def get_name(self) -> str:
        pass

    def get_id(self) -> int:
        pass

    def get_stack_val(self, pos: int) -> int:
        pass

    def get_wake_time(self) -> int:
        pass

    def get_ret_code(self) -> int:
        pass

    def get_signal_mask(self) -> int:
        pass

    def get_state(self) -> State:
        pass

    def reschedule(self, anim_type: AnimType) -> bool:
        pass

    def is_dead(self) -> bool:
        pass

    def is_garbage(self) -> bool:
        pass

    def is_waiting(self) -> bool:
        pass

    # script instance that owns this thread
    cob_instance: CobInstance
    cob_file: CobFile

    class CallInfo:
        function_id: int | None = None
        return_address: int | None = None
        stack_top: int | None = None

    def _lua_call(self):
        pass

    def _push_call_stack(self, v: CallInfo) -> None:
        pass

    def _push_data_stack(self, v: int) -> None:
        pass

    def _push_call_stack_new(self) -> CallInfo:
        pass

    def _local_function_id(self) -> int:
        pass

    def _local_return_address(self) -> int:
        pass

    def _local_stack_frame(self) -> int:
        pass

    def _pop_data_stack(self) -> int:
        pass

    _id: int = -1
    _pc: int = 0

    _wake_time: int = 0
    _param_count: int = 0
    _return_code: int = -1
    _cb_param: int = 0
    _signal_mask: int = 0

    _wait_axis: int = -1
    _wait_piece: int = -1

    _error_counter: int = 100

    _lua_args: list[int] = [0]

    _call_stack: list[CallInfo] = []
    _data_stack: array[int] = array("L", [0])

    _state: State = State.Init

    _callback_type: CobInstance.ThreadCallbackType = CobInstance.ThreadCallbackType.CB_NONE
