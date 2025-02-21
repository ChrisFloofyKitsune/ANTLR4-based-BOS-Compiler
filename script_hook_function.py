import enum
from collections.abc import Sequence, Mapping
from enum import IntEnum, nonmember

MAX_WEAPONS_PER_UNIT = 32


class ScriptHookFunction(IntEnum):
    """
    Enum used for quick lookup of special call-in/call-out Unit Script functions
    
    The hook functions are discovered by name and put into an index on a per Unit Script basis for fast lookup
    """
    _ignore_ = "_idx _wpn_idx _locals"

    CREATE = 0, 'Create'
    DESTROY = 1, 'Destroy'
    START_MOVING = 2, 'StartMoving'
    STOP_MOVING = 3, 'StopMoving'
    ACTIVATE = 4, 'Activate'
    KILLED = 5, 'Killed'
    DEACTIVATE = 6, 'Deactivate'
    SET_DIRECTION = 7, 'SetDirection'
    SET_SPEED = 8, 'SetSpeed'
    ROCK_UNIT = 9, 'RockUnit'
    HIT_BY_WEAPON = 10, 'HitByWeapon'
    MOVE_RATE0 = 11, 'MoveRate0'
    MOVE_RATE1 = 12, 'MoveRate1'
    MOVE_RATE2 = 13, 'MoveRate2'
    MOVE_RATE3 = 14, 'MoveRate3'
    SET_SFX_OCCUPY = 15, 'setSFXoccupy'
    HIT_BY_WEAPON_ID = 16, 'HitByWeaponId'
    QUERY_LANDING_PAD_COUNT = 17, 'QueryLandingPadCount'
    QUERY_LANDING_PAD = 18, 'QueryLandingPad'
    FALLING = 19, 'Falling'
    LANDED = 20, 'Landed'
    BEGIN_TRANSPORT = 21, 'BeginTransport'
    QUERY_TRANSPORT = 22, 'QueryTransport'
    TRANSPORT_PICKUP = 23, 'TransportPickup'
    START_UNLOAD = 24, 'StartUnload'
    END_TRANSPORT = 25, 'EndTransport'
    TRANSPORT_DROP = 26, 'TransportDrop'
    SET_MAX_RELOAD_TIME = 27, 'SetMaxReloadTime'
    START_BUILDING = 28, 'StartBuilding'
    STOP_BUILDING = 29, 'StopBuilding'
    QUERY_NANO_PIECE = 30, 'QueryNanoPiece'
    QUERY_BUILD_INFO = 31, 'QueryBuildInfo'
    GO = 32, 'Go'
    FUNC_LAST = nonmember(33)

    # Weapon functions repeated MAX_WEAPONS_PER_UNIT times
    QUERY_WEAPON = nonmember((33, 'QueryWeapon{:d}'))
    AIM_WEAPON = nonmember((34, 'AimWeapon{:d}'))
    AIM_FROM_WEAPON = nonmember((35, 'AimFromWeapon{:d}'))
    FIRE_WEAPON = nonmember((36, 'FireWeapon{:d}'))
    END_BURST = nonmember((37, 'EndBurst{:d}'))
    SHOT = nonmember((38, 'Shot{:d}'))
    BLOCK_SHOT = nonmember((39, 'BlockShot{:d}'))
    TARGET_WEIGHT = nonmember((40, 'TargetWeight{:d}'))

    WEAPON_FUNC_LAST = nonmember(41)
    NUM_WEAPON_FUNCS = nonmember(WEAPON_FUNC_LAST - FUNC_LAST)
    NUM_UNIT_FUNCS = nonmember(FUNC_LAST + (MAX_WEAPONS_PER_UNIT * NUM_WEAPON_FUNCS))

    # generate weapon functions
    _locals = locals()
    for _idx in range(0, MAX_WEAPONS_PER_UNIT):
        _wpn_idx = _idx * NUM_WEAPON_FUNCS
        _locals[f'QUERY_WEAPON{_idx + 1}'] = (QUERY_WEAPON[0] + _wpn_idx, QUERY_WEAPON[1].format(_idx + 1))
        _locals[f'AIM_WEAPON{_idx + 1}'] = (AIM_WEAPON[0] + _wpn_idx, AIM_WEAPON[1].format(_idx + 1))
        _locals[f'AIM_FROM_WEAPON{_idx + 1}'] = (AIM_FROM_WEAPON[0] + _wpn_idx, AIM_FROM_WEAPON[1].format(_idx + 1))
        _locals[f'FIRE_WEAPON{_idx + 1}'] = (FIRE_WEAPON[0] + _wpn_idx, FIRE_WEAPON[1].format(_idx + 1))
        _locals[f'END_BURST{_idx + 1}'] = (END_BURST[0] + _wpn_idx, END_BURST[1].format(_idx + 1))
        _locals[f'SHOT{_idx + 1}'] = (SHOT[0] + _wpn_idx, SHOT[1].format(_idx + 1))
        _locals[f'BLOCK_SHOT{_idx + 1}'] = (BLOCK_SHOT[0] + _wpn_idx, BLOCK_SHOT[1].format(_idx + 1))
        _locals[f'TARGET_WEIGHT{_idx + 1}'] = (TARGET_WEIGHT[0] + _wpn_idx, TARGET_WEIGHT[1].format(_idx + 1))

    @classmethod
    def query_weapon(cls, weapon_idx: int):
        if weapon_idx < 0 or weapon_idx >= MAX_WEAPONS_PER_UNIT:
            raise ValueError(f'Invalid weapon index: {weapon_idx}')
        return getattr(cls, f'QUERY_WEAPON{weapon_idx + 1}')

    @classmethod
    def aim_weapon(cls, weapon_idx: int):
        if weapon_idx < 0 or weapon_idx >= MAX_WEAPONS_PER_UNIT:
            raise ValueError(f'Invalid weapon index: {weapon_idx}')
        return getattr(cls, f'AIM_WEAPON{weapon_idx + 1}')

    @classmethod
    def aim_from_weapon(cls, weapon_idx: int):
        if weapon_idx < 0 or weapon_idx >= MAX_WEAPONS_PER_UNIT:
            raise ValueError(f'Invalid weapon index: {weapon_idx}')
        return getattr(cls, f'AIM_FROM_WEAPON{weapon_idx + 1}')

    @classmethod
    def fire_weapon(cls, weapon_idx: int):
        if weapon_idx < 0 or weapon_idx >= MAX_WEAPONS_PER_UNIT:
            raise ValueError(f'Invalid weapon index: {weapon_idx}')
        return getattr(cls, f'FIRE_WEAPON{weapon_idx + 1}')

    @classmethod
    def end_burst(cls, weapon_idx: int):
        if weapon_idx < 0 or weapon_idx >= MAX_WEAPONS_PER_UNIT:
            raise ValueError(f'Invalid weapon index: {weapon_idx}')
        return getattr(cls, f'END_BURST{weapon_idx + 1}')

    @classmethod
    def shot(cls, weapon_idx: int):
        if weapon_idx < 0 or weapon_idx >= MAX_WEAPONS_PER_UNIT:
            raise ValueError(f'Invalid weapon index: {weapon_idx}')
        return getattr(cls, f'SHOT{weapon_idx + 1}')

    @classmethod
    def block_shot(cls, weapon_idx: int):
        if weapon_idx < 0 or weapon_idx >= MAX_WEAPONS_PER_UNIT:
            raise ValueError(f'Invalid weapon index: {weapon_idx}')
        return getattr(cls, f'BLOCK_SHOT{weapon_idx + 1}')

    @classmethod
    def target_weight(cls, weapon_idx: int):
        if weapon_idx < 0 or weapon_idx >= MAX_WEAPONS_PER_UNIT:
            raise ValueError(f'Invalid weapon index: {weapon_idx}')
        return getattr(cls, f'TARGET_WEIGHT{weapon_idx + 1}')

    def __new__(cls, *args, **_kwargs):
        obj = int.__new__(cls, args[0])
        obj._value_ = args[0]
        obj._func_name = args[1]
        return obj

    @enum.property
    def func_name(self):
        return self._func_name


__script_names = [func.func_name for func in ScriptHookFunction]
__script_map = {func.func_name: func for func in ScriptHookFunction}

# Support the old naming scheme

__script_map["QueryPrimary"] = ScriptHookFunction.query_weapon(0)
__script_map["QuerySecondary"] = ScriptHookFunction.query_weapon(1)
__script_map["QueryTertiary"] = ScriptHookFunction.query_weapon(2)

__script_map["AimPrimary"] = ScriptHookFunction.aim_weapon(0)
__script_map["AimSecondary"] = ScriptHookFunction.aim_weapon(1)
__script_map["AimTertiary"] = ScriptHookFunction.aim_weapon(2)

__script_map["AimFromPrimary"] = ScriptHookFunction.aim_from_weapon(0)
__script_map["AimFromSecondary"] = ScriptHookFunction.aim_from_weapon(1)
__script_map["AimFromTertiary"] = ScriptHookFunction.aim_from_weapon(2)

__script_map["FirePrimary"] = ScriptHookFunction.fire_weapon(0)
__script_map["FireSecondary"] = ScriptHookFunction.fire_weapon(1)
__script_map["FireTertiary"] = ScriptHookFunction.fire_weapon(2)


def get_function_number(name: str):
    """ special function name -> lookup index """
    return __script_map.get(name, None)


def get_function_name(number: int | ScriptHookFunction):
    """ lookup index -> special function name """
    if isinstance(number, ScriptHookFunction):
        return number.func_name

    return __script_names[number] if 0 <= number < len(__script_names) else ''


SCRIPT_NAMES: Sequence[str] = __script_names
SCRIPT_MAP: Mapping[str, ScriptHookFunction] = __script_map

if __name__ == '__main__':
    print('\nENUM VALS')
    print([*ScriptHookFunction])
    print('\n[SCRIPT_NAMES]')
    print(SCRIPT_NAMES)
    print('\n{SCRIPT_MAP}')
    print(SCRIPT_MAP)

    print('\nget_function_name(0...NUM_UNIT_FUNCS)')
    for idx in range(ScriptHookFunction.NUM_UNIT_FUNCS):
        print(f'{idx:3} -> {get_function_name(idx)}')

    print('\nget_function_number(...)')
    for func in ScriptHookFunction:
        print(f'{func.func_name:20} -> {get_function_number(func.func_name)}')
    
    print('\nget_function_number(...) with legacy names')
    for extra_name, func_name in [
        ('QueryPrimary', 'QueryWeapon1'),
        ('QuerySecondary', 'QueryWeapon2'),
        ('QueryTertiary', 'QueryWeapon3'),
        ('AimPrimary', 'AimWeapon1'),
        ('AimSecondary', 'AimWeapon2'),
        ('AimTertiary', 'AimWeapon3'),
        ('AimFromPrimary', 'AimFromWeapon1'),
        ('AimFromSecondary', 'AimFromWeapon2'),
        ('AimFromTertiary', 'AimFromWeapon3'),
        ('FirePrimary', 'FireWeapon1'),
        ('FireSecondary', 'FireWeapon2'),
        ('FireTertiary', 'FireWeapon3'),
    ]:
        assert get_function_number(extra_name) == get_function_number(func_name)
        print(f'{extra_name:20} -> {get_function_number(extra_name)}')
