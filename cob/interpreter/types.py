from enum import Enum, auto
from typing import NewType

ThreadId = NewType('ThreadId', int)


class CallInfo:
    function_id: int | None = None
    return_address: int | None = None
    stack_top: int | None = None


class ThreadCallbackType(Enum):
    CBNone = auto()
    CBKilled = auto()
    CBAimWeapon = auto()
    CBAimShield = auto()
