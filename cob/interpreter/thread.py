from array import array
from enum import Enum, auto
from typing import Self

from cob.cob_file import CobFile
from cob.interpreter.instance import CobInstance
from cob.interpreter.types_ import ThreadId, ThreadCallbackType, CallInfo
from animation_engine.data_types import AnimType


class CobThread:
    class State(Enum):
        Init = auto()
        Sleep = auto()
        Run = auto()
        Dead = auto()
        WaitTurn = auto()
        WaitMove = auto()

    def __init__(self, cob_instance: CobInstance):
        # script instance that owns this thread
        self.cob_instance: CobInstance = cob_instance
        self.cob_file: CobFile = cob_instance.cob_file

        self._id = -1
        self._pc = 0

        self._wake_time = 0
        self._param_count = 0
        self._return_code = -1
        self._cb_param = 0
        self._signal_mask = 0

        self._wait_axis = -1
        self._wait_piece = -1

        self._error_counter = 100

        self._call_stack: list[CallInfo] = []
        self._data_stack = array("L", [])

        self._state = CobThread.State.Init

        self._callback_type = ThreadCallbackType.CBNone

    def __del__(self):
        self.stop()

        self._data_stack.clear()
        self._call_stack.clear()

    # def __copy__(self, other: Self):
    #     pass
    #
    # def __deepcopy__(self, other: Self):
    #     pass

    def start(self, function_id: int, sig_mask: int, args: list[int], schedule: bool) -> None:
        self._state = CobThread.State.Run
        self._pc = self.cob_file.function_ptrs[function_id]

        self._param_count = args[0]
        self._signal_mask = sig_mask

        self._call_stack = self._push_call_stack_new()
        self._call_stack.function_id = function_id
        self._call_stack.return_address = -1
        self._call_stack.stack_top = 0

        if schedule:
            pass
            # TODO: schedule the thread with CobEngine somehow

    def stop(self) -> None:
        pass

    def tick(self) -> bool:
        pass

    def set_id(self, thread_id: ThreadId) -> None:
        pass

    def set_state(self, state: State) -> None:
        pass

    def set_callback(self, cb: ThreadCallbackType, cbp: int) -> None:
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

    def get_id(self) -> ThreadId:
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

    def needs_reschedule(self, anim_type: AnimType) -> bool:
        return (
            (self._state == self.State.WaitMove and anim_type == AnimType.AMove)
            or (self._state == self.State.WaitTurn and anim_type == AnimType.ATurn)
        )

    def is_dead(self) -> bool:
        return self._state == self.State.Dead

    def is_garbage(self) -> bool:
        return self.cob_instance is None

    def is_waiting(self) -> bool:
        return self._wait_axis != -1

    def _external_call(self):
        pass

    def _push_call_stack(self, v: CallInfo) -> None:
        self._call_stack.append(v)

    def _push_data_stack(self, v: int) -> None:
        self._data_stack.append(v)

    def _push_call_stack_new(self) -> CallInfo:
        v = CallInfo()
        self._call_stack.append(v)
        return v

    def _local_function_id(self) -> int:
        return self._call_stack[-1].function_id

    def _local_return_address(self) -> int:
        return self._call_stack[-1].return_address

    def _local_stack_frame(self) -> int:
        return self._call_stack[-1].stack_top

    def _pop_data_stack(self) -> int:
        if len(self._data_stack) == 0:
            return 0
        return self._data_stack.pop(-1)
