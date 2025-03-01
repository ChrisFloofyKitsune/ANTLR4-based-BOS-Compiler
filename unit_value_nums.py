from enum import IntEnum


class UnitValue(IntEnum):
    """ Indices of set/get value"""
    ACTIVATION = 1  # set or get
    STANDINGMOVEORDERS = 2  # set or get
    STANDINGFIREORDERS = 3  # set or get
    HEALTH = 4  # get (0-100%)
    INBUILDSTANCE = 5  # set or get
    BUSY = 6  # set or get (used by misc. special case missions like transport ships)
    PIECE_XZ = 7  # get
    PIECE_Y = 8  # get
    UNIT_XZ = 9  # get
    UNIT_Y = 10  # get
    UNIT_HEIGHT = 11  # get
    XZ_ATAN = 12  # get atan of packed x,z coords
    XZ_HYPOT = 13  # get hypot of packed x,z coords
    ATAN = 14  # get ordinary two-parameter atan
    HYPOT = 15  # get ordinary two-parameter hypot
    GROUND_HEIGHT = 16  # get land height, 0 if below water
    BUILD_PERCENT_LEFT = 17  # get 0 = unit is built and ready, 1-100 = How much is left to build
    YARD_OPEN = 18  # set or get (change which plots we occupy when building opens and closes)
    BUGGER_OFF = 19  # set or get (ask other units to clear the area)
    ARMORED = 20  # set or get

    # WEAPON_AIM_ABORTED = 21
    # WEAPON_READY       = 22
    # WEAPON_LAUNCH_NOW  = 23
    # FINISHED_DYING     = 26
    # ORIENTATION        = 27

    IN_WATER = 28
    CURRENT_SPEED = 29
    # MAGIC_DEATH      = 31

    VETERAN_LEVEL = 32
    ON_ROAD = 34

    MAX_ID = 70
    MY_ID = 71
    UNIT_TEAM = 72
    UNIT_BUILD_PERCENT_LEFT = 73
    UNIT_ALLIED = 74
    MAX_SPEED = 75
    CLOAKED = 76
    WANT_CLOAK = 77
    GROUND_WATER_HEIGHT = 78  # get land height, negative if below water
    UPRIGHT = 79  # set or get
    POW = 80  # get
    PRINT = 81  # get, so multiple args can be passed
    HEADING = 82  # get
    TARGET_ID = 83  # get
    LAST_ATTACKER_ID = 84  # get
    LOS_RADIUS = 85  # set or get
    AIR_LOS_RADIUS = 86  # set or get
    RADAR_RADIUS = 87  # set or get
    JAMMER_RADIUS = 88  # set or get
    SONAR_RADIUS = 89  # set or get
    SONAR_JAM_RADIUS = 90  # set or get
    SEISMIC_RADIUS = 91  # set or get
    DO_SEISMIC_PING = 92  # get
    CURRENT_FUEL = 93  # set or get
    TRANSPORT_ID = 94  # get
    SHIELD_POWER = 95  # set or get
    STEALTH = 96  # set or get
    CRASHING = 97  # set or get, returns whether aircraft isCrashing state
    CHANGE_TARGET = 98  # set, the value it's set to determines the affected weapon
    CEG_DAMAGE = 99  # set
    COB_ID = 100  # get
    PLAY_SOUND = 101  # get, so multiple args can be passed
    KILL_UNIT = 102  # get KILL_UNIT(unitId, SelfDestruct=true, Reclaimed=false)
    SET_WEAPON_UNIT_TARGET = 106  # get (fake set)
    SET_WEAPON_GROUND_TARGET = 107  # get (fake set)
    SONAR_STEALTH = 108  # set or get
    REVERSING = 109  # get

    LUA0 = 110
    LUA1 = 111
    LUA2 = 112
    LUA3 = 113
    LUA4 = 114
    LUA5 = 115
    LUA6 = 116
    LUA7 = 117
    LUA8 = 118
    LUA9 = 119

    FLANK_B_MODE = 120  # set or get
    FLANK_B_DIR = 121  # set or get, set is through get for multiple args
    FLANK_B_MOBILITY_ADD = 122  # set or get
    FLANK_B_MAX_DAMAGE = 123  # set or get
    FLANK_B_MIN_DAMAGE = 124  # set or get
    WEAPON_RELOADSTATE = 125  # get (with fake set)
    WEAPON_RELOADTIME = 126  # get (with fake set)
    WEAPON_ACCURACY = 127  # get (with fake set)
    WEAPON_SPRAY = 128  # get (with fake set)
    WEAPON_RANGE = 129  # get (with fake set)
    WEAPON_PROJECTILE_SPEED = 130  # get (with fake set)
    COB_MIN = 131  # get
    COB_MAX = 132  # get
    ABS = 133  # get
    GAME_FRAME = 134  # get
    KSIN = 135  # get (kiloSine    : 1024*sin(x))
    KCOS = 136  # get (kiloCosine  : 1024*cos(x))
    KTAN = 137  # get (kiloTangent : 1024*tan(x))
    SQRT = 138  # get (square root)


if __name__ == '__main__':
    print([v.name for v in UnitValue])
