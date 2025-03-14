from enum import StrEnum, IntEnum


class ExpressionOp(StrEnum):
    MULT = '*'
    DIV = '/'
    MOD = '%'
    ADD = '+'
    MINUS = '-'

    COMP_LESS = '<'
    COMP_LESS_EQUAL = '<='
    COMP_GREATER = '>'
    COMP_GREATER_EQUAL = '>='
    COMP_EQUAL = '=='
    COMP_NOT_EQUAL = '!='

    BITWISE_AND = '&'
    BITWISE_OR = '|'
    BITWISE_XOR = '^'

    LOGICAL_AND = '&&'
    LOGICAL_OR = '||'
    LOGICAL_XOR = '^^'
    LOGICAL_NOT = '!'

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
