import enum
from enum import IntEnum
from typing import Any

from bos.ast_nodes import Keyword, ExpressionOperator


class CobOpCode(IntEnum):
    MOVE = 0x10001000, 2, 2
    TURN = 0x10002000, 2, 2
    SPIN = 0x10003000, 2, 2
    STOP_SPIN = 0x10004000, 2, 1
    SHOW = 0x10005000, 1, 0
    HIDE = 0x10006000, 1, 0
    CACHE = 0x10007000, 1, 0
    DONT_CACHE = 0x10008000, 1, 0
    MOVE_NOW = 0x1000B000, 2, 1
    TURN_NOW = 0x1000C000, 2, 1
    SHADE = 0x1000D000, 1, 0
    DONT_SHADE = 0x1000E000, 1, 0
    EMIT_SFX = 0x1000F000, 1, 1

    WAIT_FOR_TURN = 0x10011000, 2, 0
    WAIT_FOR_MOVE = 0x10012000, 2, 0
    SLEEP = 0x10013000, 0, 1

    PUSH_CONSTANT = 0x10021001, 1, 0
    PUSH_LOCAL_VAR = 0x10021002, 1, 0
    PUSH_STATIC = 0x10021004, 1, 0
    CREATE_LOCAL_VAR = 0x10022000, 0, 0
    POP_LOCAL_VAR = 0x10023002, 1, 1
    POP_STATIC = 0x10023004, 1, 0
    POP_STACK = 0x10024000, 0, 0

    ADD = 0x10031000, 0, 2
    SUB = 0x10032000, 0, 2
    MUL = 0x10033000, 0, 2
    DIV = 0x10034000, 0, 2
    MOD = 0x10034001, 0, 2
    BITWISE_AND = 0x10035000, 0, 2
    BITWISE_OR = 0x10036000, 0, 2
    BITWISE_XOR = 0x10037000, 0, 2
    BITWISE_NOT = 0x10038000, 0, 1

    RAND = 0x10041000, 0, 2
    GET_UNIT_VALUE = 0x10042000, 0, 1
    GET = 0x10043000, 0, 5

    SET_LESS = 0x10051000, 0, 2
    SET_LESS_OR_EQUAL = 0x10052000, 0, 2
    SET_GREATER = 0x10053000, 0, 2
    SET_GREATER_OR_EQUAL = 0x10054000, 0, 2
    SET_EQUAL = 0x10055000, 0, 2
    SET_NOT_EQUAL = 0x10056000, 0, 2
    LOGICAL_AND = 0x10057000, 0, 2
    LOGICAL_OR = 0x10058000, 0, 2
    LOGICAL_XOR = 0x10059000, 0, 2
    LOGICAL_NOT = 0x1005A000, 0, 1

    START_SCRIPT = 0x10061000, 2, 0
    CALL_SCRIPT = 0x10062000, 2, 0
    REAL_CALL = 0x10062001, 2, 0
    LUA_CALL = 0x10062002, 2, 0
    JUMP = 0x10064000, 1, 0
    RETURN = 0x10065000, 0, 1
    JUMP_NOT_EQUAL = 0x10066000, 1, 1
    SIGNAL = 0x10067000, 0, 1
    SET_SIGNAL_MASK = 0x10068000, 0, 1

    EXPLODE = 0x10071000, 1, 1
    PLAY_SOUND = 0x10072000, 1, 1

    SET = 0x10082000, 0, 2
    ATTACH_UNIT = 0x10083000, 0, 3
    DROP_UNIT = 0x10084000, 0, 1

    BAD_OP_PLACEHOLDER = -0x8000_0000, 0, 0  # aka: 0xFFFF_FFFF

    @enum.property
    def num_params(self):
        return self.num_immediate_params + self.num_stack_params

    @enum.property
    def num_immediate_params(self):
        return self.__num_immediate_params

    @enum.property
    def num_stack_params(self):
        return self.__num_stack_params

    def __new__(cls, hex_code: int, num_immediate_params, num_stack_params):
        obj: Any = int.__new__(cls, hex_code)
        obj._value_ = hex_code
        obj.__num_immediate_params = num_immediate_params
        obj.__num_stack_params = num_stack_params
        return obj

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self.name}: 0x{self:08X}>"

    @classmethod
    def from_keyword(cls, keyword: Keyword):
        match keyword:
            case Keyword.TURN:
                return CobOpCode.TURN
            case Keyword.MOVE:
                return CobOpCode.MOVE
            case Keyword.SPIN:
                return CobOpCode.SPIN
            case Keyword.STOP_SPIN:
                return CobOpCode.STOP_SPIN
            case Keyword.WAIT_FOR_TURN:
                return CobOpCode.WAIT_FOR_TURN
            case Keyword.WAIT_FOR_MOVE:
                return CobOpCode.WAIT_FOR_MOVE
            case Keyword.SET:
                return CobOpCode.SET
            case Keyword.GET:
                return CobOpCode.GET
            case Keyword.CALL_SCRIPT:
                return CobOpCode.CALL_SCRIPT
            case Keyword.START_SCRIPT:
                return CobOpCode.START_SCRIPT
            case Keyword.EMIT_SFX:
                return CobOpCode.EMIT_SFX
            case Keyword.SLEEP:
                return CobOpCode.SLEEP
            case Keyword.HIDE:
                return CobOpCode.HIDE
            case Keyword.SHOW:
                return CobOpCode.SHOW
            case Keyword.EXPLODE:
                return CobOpCode.EXPLODE
            case Keyword.SIGNAL:
                return CobOpCode.SIGNAL
            case Keyword.SET_SIGNAL_MASK:
                return CobOpCode.SET_SIGNAL_MASK
            case Keyword.ATTACH_UNIT:
                return CobOpCode.ATTACH_UNIT
            case Keyword.DROP_UNIT:
                return CobOpCode.DROP_UNIT
            case Keyword.RETURN:
                return CobOpCode.RETURN
            case Keyword.CACHE:
                return CobOpCode.CACHE
            case Keyword.DONT_CACHE:
                return CobOpCode.DONT_CACHE
            case Keyword.DONT_SHADOW:
                return CobOpCode.DONT_SHADE
            case Keyword.DONT_SHADE:
                return CobOpCode.DONT_SHADE
            case Keyword.PLAY_SOUND:
                return CobOpCode.PLAY_SOUND
        return None

    @classmethod
    def from_expression_op(cls, op: ExpressionOperator):
        match op:
            case ExpressionOperator.MULT:
                return CobOpCode.MUL
            case ExpressionOperator.DIV:
                return CobOpCode.DIV
            case ExpressionOperator.MOD:
                return CobOpCode.MOD
            case ExpressionOperator.ADD:
                return CobOpCode.ADD
            case ExpressionOperator.MINUS:
                return CobOpCode.SUB
            case ExpressionOperator.COMP_LESS:
                return CobOpCode.SET_LESS
            case ExpressionOperator.COMP_LESS_EQUAL:
                return CobOpCode.SET_LESS_OR_EQUAL
            case ExpressionOperator.COMP_GREATER:
                return CobOpCode.SET_GREATER
            case ExpressionOperator.COMP_GREATER_EQUAL:
                return CobOpCode.SET_GREATER_OR_EQUAL
            case ExpressionOperator.COMP_EQUAL:
                return CobOpCode.SET_EQUAL
            case ExpressionOperator.COMP_NOT_EQUAL:
                return CobOpCode.SET_NOT_EQUAL
            case ExpressionOperator.BITWISE_AND:
                return CobOpCode.BITWISE_AND
            case ExpressionOperator.BITWISE_OR:
                return CobOpCode.BITWISE_OR
            case ExpressionOperator.BITWISE_XOR:
                return CobOpCode.BITWISE_XOR
            case ExpressionOperator.LOGICAL_AND:
                return CobOpCode.LOGICAL_AND
            case ExpressionOperator.LOGICAL_OR:
                return CobOpCode.LOGICAL_OR
            case ExpressionOperator.LOGICAL_XOR:
                return CobOpCode.LOGICAL_XOR
            case ExpressionOperator.LOGICAL_NOT:
                return CobOpCode.LOGICAL_NOT

        raise ValueError(f"Invalid / unsupported expression op: {op}")


if __name__ == "__main__":
    print(
        "\n".join(
            [
                f"{op.name:>20}: {hex(op.value):>11} #imm {op.num_immediate_params} #stk {op.num_stack_params}"
                for op in CobOpCode
            ]
        )
    )
