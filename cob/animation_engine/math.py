from enum import IntEnum
from typing import Final, TypeAlias

import pyglm


SIM_SPEED: Final[int] = 30;
INV_SIM_SPEED: Final[float] = 1.0 / SIM_SPEED

float3 = pyglm.f32vec3
Radians: TypeAlias = float
Radians3: TypeAlias = pyglm.f32vec3

RadiansPerFrame: TypeAlias = Radians

UP_VECTOR: Final[float3] = float3(0.0, 1.0, 0.0)
FORWARD_VECTOR: Final[float3] = float3(0.0, 0.0, 1.0)
RIGHT_VECTOR: Final[float3] = float3(1.0, 0.0, 0.0)

ZERO_VECTOR: Final[float3] = float3(0.0, 0.0, 0.0)
ONES_VECTOR: Final[float3] = float3(1.0, 1.0, 1.0)

XY_VECTOR: Final[float3] = float3(1.0, 1.0, 0.0)
XZ_VECTOR: Final[float3] = float3(1.0, 0.0, 1.0)
YZ_VECTOR: Final[float3] = float3(0.0, 1.0, 1.0)

matrix44 = pyglm.f32mat4x4

MAX_COB_ARGS: Final[int] = 16

COB_SCALE: Final[int] = 65536
COB_SCALE_HALF: Final[int] = COB_SCALE // 2
COB_SCALE_INV: Final[float] = 1.0 / COB_SCALE

PI: Final[Radians] = pyglm.pi()
TWO_PI: Final[Radians] = pyglm.two_pi()
THREE_PI: Final[Radians] = 3.0 * PI

RAD_2_TA_ANG: Final[Radians] = COB_SCALE_HALF / PI
TA_ANG_2_RAD: Final[Radians] = PI / COB_SCALE_HALF

floor = pyglm.floor
abs = pyglm.abs
sign = pyglm.sign
modf = pyglm.modf()


class Axis(IntEnum):
    X = 0
    Y = 1
    Z = 2


def clamp_rad(f: Radians) -> Radians:
    f += 0.0  # eliminate -0.0
    f = f - TWO_PI * pyglm.floor(f / TWO_PI)
    assert pyglm.sign(f) != -1, 'there should be no negative zeros (-0.0) or negatives in general'
    return f


def clamp_rad3(f: Radians3) -> Radians3:
    return float3(clamp_rad(f.x), clamp_rad(f.y), clamp_rad(f.z))


def pack_xz(x: pyglm.uint32, z: pyglm.uint32) -> pyglm.uint32:
    return pyglm.uint32(((x & 0xFFFF) << 16) | (z & 0xFFFF))


def unpack_x(xz: pyglm.uint32) -> pyglm.uint32:
    return pyglm.uint32((xz >> 16) & 0xFFFF)


def unpack_z(xz: pyglm.uint32) -> pyglm.uint32:
    return pyglm.uint32(xz & 0xFFFF)


def unpack_xz(xz: pyglm.uint32) -> tuple[pyglm.uint32, pyglm.uint32]:
    return unpack_x(xz), unpack_z(xz)
