from collections.abc import Sequence, Mapping
from enum import IntEnum

MAX_WEAPONS_PER_UNIT = 32


class CobFunction(IntEnum):
    """ Enum used for quick lookup of special call-in/call-out COB functions (determined by function name) """
    CREATE = 0
    DESTROY = 1
    START_MOVING = 2
    STOP_MOVING = 3
    ACTIVATE = 4
    KILLED = 5
    DEACTIVATE = 6
    SET_DIRECTION = 7
    SET_SPEED = 8
    ROCK_UNIT = 9
    HIT_BY_WEAPON = 10
    MOVE_RATE0 = 11
    MOVE_RATE1 = 12
    MOVE_RATE2 = 13
    MOVE_RATE3 = 14
    SET_SFX_OCCUPY = 15
    HIT_BY_WEAPON_ID = 16
    QUERY_LANDING_PAD_COUNT = 17
    QUERY_LANDING_PAD = 18
    FALLING = 19
    LANDED = 20
    BEGIN_TRANSPORT = 21
    QUERY_TRANSPORT = 22
    TRANSPORT_PICKUP = 23
    START_UNLOAD = 24
    END_TRANSPORT = 25
    TRANSPORT_DROP = 26
    SET_MAX_RELOAD_TIME = 27
    START_BUILDING = 28
    STOP_BUILDING = 29
    QUERY_NANO_PIECE = 30
    QUERY_BUILD_INFO = 31
    GO = 32
    FUNC_LAST = 33

    # Special functions repeated MAX_WEAPONS_PER_UNIT times
    QUERY_WEAPON = 34
    AIM_WEAPON = 35
    AIM_FROM_WEAPON = 36
    FIRE_WEAPON = 37
    END_BURST = 38
    SHOT = 39
    BLOCK_SHOT = 40
    TARGET_WEIGHT = 41

    WEAPON_FUNC_LAST = 42
    WEAPON_FUNCS = WEAPON_FUNC_LAST - FUNC_LAST
    NUM_UNIT_FUNCS = FUNC_LAST + (MAX_WEAPONS_PER_UNIT * WEAPON_FUNCS)


__script_names = [''] * CobFunction.NUM_UNIT_FUNCS

__script_names[CobFunction.CREATE] = 'Create'
__script_names[CobFunction.DESTROY] = "Destroy"
__script_names[CobFunction.START_MOVING] = "StartMoving"
__script_names[CobFunction.STOP_MOVING] = "StopMoving"
__script_names[CobFunction.ACTIVATE] = "Activate"
__script_names[CobFunction.KILLED] = "Killed"
__script_names[CobFunction.DEACTIVATE] = "Deactivate"
__script_names[CobFunction.SET_DIRECTION] = "SetDirection"
__script_names[CobFunction.SET_SPEED] = "SetSpeed"
__script_names[CobFunction.ROCK_UNIT] = "RockUnit"
__script_names[CobFunction.HIT_BY_WEAPON] = "HitByWeapon"
__script_names[CobFunction.MOVE_RATE0] = "MoveRate0"
__script_names[CobFunction.MOVE_RATE1] = "MoveRate1"
__script_names[CobFunction.MOVE_RATE2] = "MoveRate2"
__script_names[CobFunction.MOVE_RATE3] = "MoveRate3"
__script_names[CobFunction.SET_SFX_OCCUPY] = "setSFXoccupy"
__script_names[CobFunction.HIT_BY_WEAPON_ID] = "HitByWeaponId"

__script_names[CobFunction.QUERY_LANDING_PAD_COUNT] = "QueryLandingPadCount"
__script_names[CobFunction.QUERY_LANDING_PAD] = "QueryLandingPad"
__script_names[CobFunction.FALLING] = "Falling"
__script_names[CobFunction.LANDED] = "Landed"
__script_names[CobFunction.BEGIN_TRANSPORT] = "BeginTransport"
__script_names[CobFunction.QUERY_TRANSPORT] = "QueryTransport"
__script_names[CobFunction.TRANSPORT_PICKUP] = "TransportPickup"
__script_names[CobFunction.START_UNLOAD] = "StartUnload"
__script_names[CobFunction.END_TRANSPORT] = "EndTransport"
__script_names[CobFunction.TRANSPORT_DROP] = "TransportDrop"
__script_names[CobFunction.SET_MAX_RELOAD_TIME] = "SetMaxReloadTime"
__script_names[CobFunction.START_BUILDING] = "StartBuilding"
__script_names[CobFunction.STOP_BUILDING] = "StopBuilding"
__script_names[CobFunction.QUERY_NANO_PIECE] = "QueryNanoPiece"
__script_names[CobFunction.QUERY_BUILD_INFO] = "QueryBuildInfo"
__script_names[CobFunction.GO] = "Go"

# Weapon aiming stuff
for i in range(MAX_WEAPONS_PER_UNIT):
    WEAPON_NUM = str(i + 1)
    idx = CobFunction.WEAPON_FUNCS * i

    __script_names[CobFunction.QUERY_WEAPON + idx] = f"QueryWeapon{WEAPON_NUM}"
    __script_names[CobFunction.AIM_WEAPON + idx] = f"AimWeapon{WEAPON_NUM}"
    __script_names[CobFunction.AIM_FROM_WEAPON + idx] = f"AimFromWeapon{WEAPON_NUM}"
    __script_names[CobFunction.FIRE_WEAPON + idx] = f"FireWeapon{WEAPON_NUM}"
    __script_names[CobFunction.END_BURST + idx] = f"EndBurst{WEAPON_NUM}"
    __script_names[CobFunction.SHOT + idx] = f"Shot{WEAPON_NUM}"
    __script_names[CobFunction.BLOCK_SHOT + idx] = f"BlockShot{WEAPON_NUM}"
    __script_names[CobFunction.TARGET_WEIGHT + idx] = f"TargetWeight{WEAPON_NUM}"

__script_map = {name: CobFunction(idx) for idx, name in enumerate(__script_names)}

# Support the old naming scheme

__script_map["QueryPrimary"]: CobFunction.QUERY_WEAPON
__script_map["QuerySecondary"]: CobFunction.QUERY_WEAPON + CobFunction.WEAPON_FUNCS * 1
__script_map["QueryTertiary"]: CobFunction.QUERY_WEAPON + CobFunction.WEAPON_FUNCS * 2

__script_map["AimPrimary"]: CobFunction.AIM_WEAPON
__script_map["AimSecondary"]: CobFunction.AIM_WEAPON + CobFunction.WEAPON_FUNCS * 1
__script_map["AimTertiary"]: CobFunction.AIM_WEAPON + CobFunction.WEAPON_FUNCS * 2

__script_map["AimFromPrimary"]: CobFunction.AIM_FROM_WEAPON
__script_map["AimFromSecondary"]: CobFunction.AIM_FROM_WEAPON + CobFunction.WEAPON_FUNCS * 1
__script_map["AimFromTertiary"]: CobFunction.AIM_FROM_WEAPON + CobFunction.WEAPON_FUNCS * 2

__script_map["FirePrimary"]: CobFunction.FIRE_WEAPON
__script_map["FireSecondary"]: CobFunction.FIRE_WEAPON + CobFunction.WEAPON_FUNCS * 1
__script_map["FireTertiary"]: CobFunction.FIRE_WEAPON + CobFunction.WEAPON_FUNCS * 2


def get_script_number(name: str):
    """ special function name -> lookup index """
    return __script_map.get(name, -1)


def get_script_name(number: int | CobFunction):
    """ lookup index -> special function name """
    return __script_names[number] if 0 <= number < len(__script_names) else ''


SCRIPT_NAMES: Sequence[str] = __script_names
SCRIPT_MAP: Mapping[str, CobFunction] = __script_map
