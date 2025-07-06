from typing import Final, TypeAlias, NewType

import pyglm as glm

ticks_per_second: TypeAlias = int

SIM_SPEED: Final[ticks_per_second] = 30

int32: TypeAlias = glm.int32
uint32: TypeAlias = glm.uint32

float_velocity: TypeAlias = float
float_accel: TypeAlias = float

float2: TypeAlias = glm.f32vec2
float3: TypeAlias = glm.f32vec3

radians: TypeAlias = float
radians_velocity: TypeAlias = radians
radians_accel: TypeAlias = radians

radians3: TypeAlias = glm.f32vec3

milliseconds: TypeAlias = int

UP_VECTOR: Final[float3] = float3(0.0, 1.0, 0.0)
FORWARD_VECTOR: Final[float3] = float3(0.0, 0.0, 1.0)
RIGHT_VECTOR: Final[float3] = float3(1.0, 0.0, 0.0)

ZERO_VECTOR: Final[float3] = float3(0.0, 0.0, 0.0)
ONES_VECTOR: Final[float3] = float3(1.0, 1.0, 1.0)

X_AXIS: Final[float3] = float3(1.0, 0.0, 0.0)
Y_AXIS: Final[float3] = float3(0.0, 1.0, 0.0)
Z_AXIS: Final[float3] = float3(0.0, 0.0, 1.0)

XY_VECTOR: Final[float3] = float3(1.0, 1.0, 0.0)
XZ_VECTOR: Final[float3] = float3(1.0, 0.0, 1.0)
YZ_VECTOR: Final[float3] = float3(0.0, 1.0, 1.0)

matrix44: TypeAlias = glm.f32mat4x4
WORLD_TO_OBJECT_SPACE: matrix44 = glm.scale((-1, 1, 1))
# as it's just X-axis mirroring, the same matrix works for both
OBJECT_TO_WORLD_SPACE: matrix44 = WORLD_TO_OBJECT_SPACE

MAX_COB_ARGS: Final[int] = 16

COB_SCALE: Final[int] = 65536
COB_SCALE_HALF: Final[int] = COB_SCALE // 2
COB_SCALE_INV: Final[float] = 1.0 / COB_SCALE

PI: Final[radians] = glm.pi()
TWO_PI: Final[radians] = glm.two_pi()
THREE_PI: Final[radians] = 3.0 * PI

RAD_2_TA_ANG: Final[radians] = COB_SCALE_HALF / PI
TA_ANG_2_RAD: Final[radians] = PI / COB_SCALE_HALF

floor = glm.floor
abs = glm.abs
sign = glm.sign
normalize = glm.normalize
mod = lambda a, b: a - b * floor(a / b)


def clamp_rad(f: radians) -> radians:
    f += 0.0  # eliminate -0.0
    f = f - TWO_PI * floor(f / TWO_PI)
    assert sign(f) != -1, "there should be no negative zeros (-0.0) or negatives in general"
    return f


def clamp_rad3(f: radians3) -> radians3:
    return float3(clamp_rad(f.x), clamp_rad(f.y), clamp_rad(f.z))


def pack_xz(x: uint32, z: uint32) -> uint32:
    return uint32(((x & 0xFFFF) << 16) | (z & 0xFFFF))


def unpack_x(xz: uint32) -> uint32:
    return uint32((xz >> 16) & 0xFFFF)


def unpack_z(xz: uint32) -> uint32:
    return uint32(xz & 0xFFFF)


def unpack_xz(xz: uint32) -> tuple[uint32, uint32]:
    return unpack_x(xz), unpack_z(xz)


def milliseconds_to_tick_rate(delta_time_ms: milliseconds) -> ticks_per_second:
    """
    given a time in milliseconds, returns the number of ticks per second (tick rate).

    this is inverse delta_time (1/delta_time)
    therefore, dividing by this is the same as multiplying by delta_time

    :param delta_time_ms:
    :return:
    """
    return 1000 // delta_time_ms

"""
    SIM_SPEED = 30 TPS

    30 ticks    1 second     30 ticks
    ---per--- * ---per--- => ---per--- 
    1 second    1000 ms      1000 ms

    30 ticks       1 tick
    ---per--- => ---per---
    1000 ms        33 ms
    
    
    what milliseconds_to_tick_rate() is doing
    1000 ms    1 tick      30 ticks
    -------- * ---per-- => --------
    1 second   33ms        1 second
    
    what's basically happening inside the Tick Anim functions
    XXX units    1 second    XXX/30 units
    ---------- * -------- ~= --------
    1 second     30 ticks     1 tick
"""