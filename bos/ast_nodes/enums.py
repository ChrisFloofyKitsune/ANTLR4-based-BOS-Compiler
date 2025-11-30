import operator
from enum import StrEnum, IntEnum


class ExpressionOperator(StrEnum):
    MULT = '*', operator.mul
    DIV = '/', operator.truediv
    MOD = '%', operator.mod
    ADD = '+', operator.add
    MINUS = '-', operator.sub

    COMP_LESS = '<', operator.lt
    COMP_LESS_EQUAL = '<=', operator.le
    COMP_GREATER = '>', operator.gt
    COMP_GREATER_EQUAL = '>=', operator.ge
    COMP_EQUAL = '==', operator.eq
    COMP_NOT_EQUAL = '!=', operator.ne

    BITWISE_AND = '&', lambda a, b: (int(a) & int(b)) & 0xFFFFFFFF
    BITWISE_OR = '|', lambda a, b: (int(a) | int(b)) & 0xFFFFFFFF
    BITWISE_XOR = '^', lambda a, b: (int(a) ^ int(b)) & 0xFFFFFFFF

    LOGICAL_AND = '&&', lambda a, b: operator.truth(a) and operator.truth(b)
    LOGICAL_OR = '||', lambda a, b: operator.truth(a) or operator.truth(b)
    LOGICAL_XOR = '^^', lambda a, b: operator.truth(a) != operator.truth(b)
    LOGICAL_NOT = '!', lambda a: not operator.truth(a)

    def eval(self, *args):
        return self._eval_func(*args)

    def __new__(cls, value, eval_func):
        obj = str.__new__(cls, value)
        obj._value_ = value
        obj._eval_func = eval_func
        return obj

    def __repr__(self):
        return f'ExpressionOp.{self.name}'


class Keyword(StrEnum):
    TURN = 'turn'
    AROUND = 'around'
    MOVE = 'move'
    ALONG = 'along'
    TO = 'to'
    FROM = 'from'
    NOW = 'now'
    SPEED = 'speed'
    SPIN = 'spin'
    ACCELERATE = 'accelerate'
    STOP_SPIN = 'stop-spin'
    DECELERATE = 'decelerate'
    WAIT_FOR_TURN = 'wait-for-turn'
    WAIT_FOR_MOVE = 'wait-for-move'
    SET = 'set'
    GET = 'get'
    CALL_SCRIPT = 'call-script'
    START_SCRIPT = 'start-script'
    EMIT_SFX = 'emit-sfx'
    SLEEP = 'sleep'
    HIDE = 'hide'
    SHOW = 'show'
    EXPLODE = 'explode'
    TYPE = 'type'
    SIGNAL = 'signal'
    SET_SIGNAL_MASK = 'set-signal-mask'
    ATTACH_UNIT = 'attach-unit'
    DROP_UNIT = 'drop-unit'
    RETURN = 'return'
    CACHE = 'cache'
    DONT_CACHE = 'dont-cache'
    DONT_SHADOW = 'dont-shade'
    DONT_SHADE = 'dont-shade'
    PLAY_SOUND = 'play-sound'

    def __repr__(self):
        return f'Keyword.{self.name}'


class AxisEnum(IntEnum):
    X = 0
    Y = 1
    Z = 2

    @staticmethod
    def from_str(string: str):
        match string[0].lower():
            case 'x':
                return AxisEnum.X
            case 'y':
                return AxisEnum.Y
            case 'z':
                return AxisEnum.Z

        return None

    def __repr__(self):
        return f'AxisEnum.{self.name}'
