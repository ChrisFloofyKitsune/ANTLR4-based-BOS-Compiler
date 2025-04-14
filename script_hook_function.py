import enum
from collections.abc import Sequence, Mapping
from enum import IntEnum, nonmember
from functools import lru_cache
from typing import cast, Self, Any

MAX_WEAPONS_PER_UNIT = 32


class ScriptHookFunction(IntEnum):
    """
    Enum used for quick lookup of special call-in/call-out Unit Script functions

    The hook functions are discovered by name and put into an index on a per-"Unit Script" basis for fast lookup
    """

    CREATE = 0, "Create"
    DESTROY = 1, "Destroy"
    START_MOVING = 2, "StartMoving"
    STOP_MOVING = 3, "StopMoving"
    ACTIVATE = 4, "Activate"
    KILLED = 5, "Killed"
    DEACTIVATE = 6, "Deactivate"
    SET_DIRECTION = 7, "SetDirection"
    SET_SPEED = 8, "SetSpeed"
    ROCK_UNIT = 9, "RockUnit"
    HIT_BY_WEAPON = 10, "HitByWeapon"
    MOVE_RATE0 = 11, "MoveRate0"
    MOVE_RATE1 = 12, "MoveRate1"
    MOVE_RATE2 = 13, "MoveRate2"
    MOVE_RATE3 = 14, "MoveRate3"
    SET_SFX_OCCUPY = 15, "setSFXoccupy"
    HIT_BY_WEAPON_ID = 16, "HitByWeaponId"
    QUERY_LANDING_PAD_COUNT = 17, "QueryLandingPadCount"
    QUERY_LANDING_PAD = 18, "QueryLandingPad"
    FALLING = 19, "Falling"
    LANDED = 20, "Landed"
    BEGIN_TRANSPORT = 21, "BeginTransport"
    QUERY_TRANSPORT = 22, "QueryTransport"
    TRANSPORT_PICKUP = 23, "TransportPickup"
    START_UNLOAD = 24, "StartUnload"
    END_TRANSPORT = 25, "EndTransport"
    TRANSPORT_DROP = 26, "TransportDrop"
    SET_MAX_RELOAD_TIME = 27, "SetMaxReloadTime"
    START_BUILDING = 28, "StartBuilding"
    STOP_BUILDING = 29, "StopBuilding"
    QUERY_NANO_PIECE = 30, "QueryNanoPiece"
    QUERY_BUILD_INFO = 31, "QueryBuildInfo"
    GO = 32, "Go"
    FUNC_LAST = cast(int, nonmember(33))

    # Weapon functions repeated MAX_WEAPONS_PER_UNIT times
    QUERY_WEAPON = nonmember((33, "QueryWeapon"))
    AIM_WEAPON = nonmember((34, "AimWeapon"))
    AIM_FROM_WEAPON = nonmember((35, "AimFromWeapon"))
    FIRE_WEAPON = nonmember((36, "FireWeapon"))
    END_BURST = nonmember((37, "EndBurst"))
    SHOT = nonmember((38, "Shot"))
    BLOCK_SHOT = nonmember((39, "BlockShot"))
    TARGET_WEIGHT = nonmember((40, "TargetWeight"))

    WEAPON_FUNC_LAST = cast(int, nonmember(41))
    NUM_WEAPON_FUNCS = cast(int, nonmember(WEAPON_FUNC_LAST - FUNC_LAST))
    NUM_UNIT_FUNCS = cast(int, nonmember(FUNC_LAST + (MAX_WEAPONS_PER_UNIT * NUM_WEAPON_FUNCS)))

    # generate weapon function enums
    __locals = cast(dict[str, Any], locals())
    for __idx in range(0, MAX_WEAPONS_PER_UNIT):
        __wpn_idx = __idx * NUM_WEAPON_FUNCS
        for __base in (
            "QUERY_WEAPON",
            "AIM_WEAPON",
            "AIM_FROM_WEAPON",
            "FIRE_WEAPON",
            "END_BURST",
            "SHOT",
            "BLOCK_SHOT",
            "TARGET_WEIGHT",
        ):
            __base_idx, __base_name = cast(tuple[int, str], __locals[__base])
            __locals[f"{__base}{__idx + 1}"] = (__base_idx + __wpn_idx, __base_name + str(__idx + 1))
    del __locals, __idx, __wpn_idx, __base, __base_idx, __base_name

    def __new__(cls, *args, **_kwargs):
        obj = int.__new__(cls, args[0])
        obj._value_ = args[0]
        obj._func_name_ = args[1]
        return obj

    def __repr__(self):
        return f"<{self.__class__.__name__}.{self._name_}: {self._value_}, {self._func_name_}>"

    @enum.property
    def func_id(self):
        return self._value_

    @enum.property
    def func_name(self):
        return self._func_name_

    @classmethod
    def query_weapon(cls, weapon_idx: int):
        if weapon_idx < 0 or weapon_idx >= MAX_WEAPONS_PER_UNIT:
            raise ValueError(f"Invalid weapon index: {weapon_idx}")
        return getattr(cls, f"QUERY_WEAPON{weapon_idx + 1}")

    @classmethod
    def aim_weapon(cls, weapon_idx: int):
        if weapon_idx < 0 or weapon_idx >= MAX_WEAPONS_PER_UNIT:
            raise ValueError(f"Invalid weapon index: {weapon_idx}")
        return getattr(cls, f"AIM_WEAPON{weapon_idx + 1}")

    @classmethod
    def aim_from_weapon(cls, weapon_idx: int):
        if weapon_idx < 0 or weapon_idx >= MAX_WEAPONS_PER_UNIT:
            raise ValueError(f"Invalid weapon index: {weapon_idx}")
        return getattr(cls, f"AIM_FROM_WEAPON{weapon_idx + 1}")

    @classmethod
    def fire_weapon(cls, weapon_idx: int):
        if weapon_idx < 0 or weapon_idx >= MAX_WEAPONS_PER_UNIT:
            raise ValueError(f"Invalid weapon index: {weapon_idx}")
        return getattr(cls, f"FIRE_WEAPON{weapon_idx + 1}")

    @classmethod
    def end_burst(cls, weapon_idx: int):
        if weapon_idx < 0 or weapon_idx >= MAX_WEAPONS_PER_UNIT:
            raise ValueError(f"Invalid weapon index: {weapon_idx}")
        return getattr(cls, f"END_BURST{weapon_idx + 1}")

    @classmethod
    def shot(cls, weapon_idx: int):
        if weapon_idx < 0 or weapon_idx >= MAX_WEAPONS_PER_UNIT:
            raise ValueError(f"Invalid weapon index: {weapon_idx}")
        return getattr(cls, f"SHOT{weapon_idx + 1}")

    @classmethod
    def block_shot(cls, weapon_idx: int):
        if weapon_idx < 0 or weapon_idx >= MAX_WEAPONS_PER_UNIT:
            raise ValueError(f"Invalid weapon index: {weapon_idx}")
        return getattr(cls, f"BLOCK_SHOT{weapon_idx + 1}")

    @classmethod
    def target_weight(cls, weapon_idx: int):
        if weapon_idx < 0 or weapon_idx >= MAX_WEAPONS_PER_UNIT:
            raise ValueError(f"Invalid weapon index: {weapon_idx}")
        return getattr(cls, f"TARGET_WEIGHT{weapon_idx + 1}")

    __script_names: list[str] = []
    __script_map: dict[str, "ScriptHookFunction"] = {}

    @classmethod
    def __static__init__(cls):
        cls.__script_names = [func.func_name for func in ScriptHookFunction]
        cls.__script_map = {func.func_name: func for func in ScriptHookFunction}

        # Support the old naming scheme
        cls.__script_map["QueryPrimary"] = ScriptHookFunction.query_weapon(0)
        cls.__script_map["QuerySecondary"] = ScriptHookFunction.query_weapon(1)
        cls.__script_map["QueryTertiary"] = ScriptHookFunction.query_weapon(2)

        cls.__script_map["AimPrimary"] = ScriptHookFunction.aim_weapon(0)
        cls.__script_map["AimSecondary"] = ScriptHookFunction.aim_weapon(1)
        cls.__script_map["AimTertiary"] = ScriptHookFunction.aim_weapon(2)

        cls.__script_map["AimFromPrimary"] = ScriptHookFunction.aim_from_weapon(0)
        cls.__script_map["AimFromSecondary"] = ScriptHookFunction.aim_from_weapon(1)
        cls.__script_map["AimFromTertiary"] = ScriptHookFunction.aim_from_weapon(2)

        cls.__script_map["FirePrimary"] = ScriptHookFunction.fire_weapon(0)
        cls.__script_map["FireSecondary"] = ScriptHookFunction.fire_weapon(1)
        cls.__script_map["FireTertiary"] = ScriptHookFunction.fire_weapon(2)

    @classmethod
    def lookup(cls, identifier: int | str) -> Self:
        """lookup the matching ScriptHookFunction enum value"""
        if isinstance(identifier, str):
            try:
                return cls.script_map()[identifier]
            except KeyError as err:
                raise ValueError(f"Function name '{identifier}' not found in function_map.") from err
        elif isinstance(identifier, int):
            if 0 <= identifier < len(cls.script_names()):
                return cls(identifier)
            else:
                raise ValueError(f"Function index '{identifier}' out of range.")
        else:
            raise TypeError(f"Invalid type '{type(identifier)}' for identifier.")

    @classmethod
    def get_function_number(cls, name: str):
        """special function name -> lookup index"""
        return cls.script_map().get(name, None)

    @classmethod
    def get_function_name(cls, number: int | Self):
        """lookup index -> special function name"""
        if isinstance(number, cls):
            return number.func_name

        return cls.script_names()[number] if 0 <= number < len(cls.script_names()) else ""

    @classmethod
    @lru_cache(1)
    def script_names(cls) -> Sequence[str]:
        return cast(Sequence[str], cls.__script_names)

    @classmethod
    @lru_cache(1)
    def script_map(cls) -> Mapping[str, Self]:
        return cast(Mapping[str, Self], cls.__script_map)


ScriptHookFunction.__static__init__()

if __name__ == "__main__":

    def __main__():
        print("\nENUM VALS")
        print([*ScriptHookFunction])
        print("\n[Script Names]")
        print(ScriptHookFunction.script_names())
        print("\n{Script Map}")
        print(ScriptHookFunction.script_map())

        print("\nget_function_name(0...NUM_UNIT_FUNCS)")
        for idx in range(ScriptHookFunction.NUM_UNIT_FUNCS):
            print(f"{idx:3} -> {ScriptHookFunction.get_function_name(idx)}")

        print("\nlookup(0...NUM_UNIT_FUNCS)")
        for idx in range(ScriptHookFunction.NUM_UNIT_FUNCS):
            print(f"{idx:3} -> {repr(ScriptHookFunction.lookup(idx))}")

        print("\nget_function_number(...)")
        for func in ScriptHookFunction:
            print(f"{func.func_name:20} -> {ScriptHookFunction.get_function_number(func.func_name)}")

        print("\nget_function_number(...) with legacy names")
        for extra_name, func_name in [
            ("QueryPrimary", "QueryWeapon1"),
            ("QuerySecondary", "QueryWeapon2"),
            ("QueryTertiary", "QueryWeapon3"),
            ("AimPrimary", "AimWeapon1"),
            ("AimSecondary", "AimWeapon2"),
            ("AimTertiary", "AimWeapon3"),
            ("AimFromPrimary", "AimFromWeapon1"),
            ("AimFromSecondary", "AimFromWeapon2"),
            ("AimFromTertiary", "AimFromWeapon3"),
            ("FirePrimary", "FireWeapon1"),
            ("FireSecondary", "FireWeapon2"),
            ("FireTertiary", "FireWeapon3"),
        ]:
            assert ScriptHookFunction.get_function_number(extra_name) == ScriptHookFunction.get_function_number(
                func_name
            )
            print(f"{extra_name:20} -> {ScriptHookFunction.get_function_number(extra_name)}")

        print("\nlookup(...) with names")
        for func_name in ScriptHookFunction.script_names():
            print(f"{func_name:20} -> {repr(ScriptHookFunction.lookup(func_name))}")

        print("\nlookup(...) with legacy names")
        for extra_name, func_name in [
            ("QueryPrimary", "QueryWeapon1"),
            ("QuerySecondary", "QueryWeapon2"),
            ("QueryTertiary", "QueryWeapon3"),
            ("AimPrimary", "AimWeapon1"),
            ("AimSecondary", "AimWeapon2"),
            ("AimTertiary", "AimWeapon3"),
            ("AimFromPrimary", "AimFromWeapon1"),
            ("AimFromSecondary", "AimFromWeapon2"),
            ("AimFromTertiary", "AimFromWeapon3"),
            ("FirePrimary", "FireWeapon1"),
            ("FireSecondary", "FireWeapon2"),
            ("FireTertiary", "FireWeapon3"),
        ]:
            assert ScriptHookFunction.lookup(extra_name) == ScriptHookFunction.lookup(func_name)
            print(f"{extra_name:20} -> {repr(ScriptHookFunction.lookup(extra_name))}")

    __main__()
