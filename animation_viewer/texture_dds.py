from __future__ import annotations

import ctypes
import enum
import struct
import typing
import warnings

import moderngl
import typing_extensions
from dataclasses import dataclass
import numpy as np

import pyglet.gl as GL

_DDS_header_struct = struct.Struct('<7L 11L 32s 4L L')
"""
https://learn.microsoft.com/en-us/windows/win32/direct3ddds/dds-header

typedef struct {
  DWORD           dwSize;
  DWORD           dwFlags;
  DWORD           dwHeight;
  DWORD           dwWidth;
  DWORD           dwPitchOrLinearSize;
  DWORD           dwDepth;
  DWORD           dwMipMapCount;
  DWORD           dwReserved1[11];
  DDS_PIXELFORMAT ddspf;
  DWORD           dwCaps;
  DWORD           dwCaps2;
  DWORD           dwCaps3;
  DWORD           dwCaps4;
  DWORD           dwReserved2;
} DDS_HEADER;
"""

_DDS_pixel_format_struct = struct.Struct('<2L 4s 5L')
"""
https://learn.microsoft.com/en-us/windows/win32/direct3ddds/dds-pixelformat

struct DDS_PIXELFORMAT {
  DWORD dwSize;
  DWORD dwFlags;
  DWORD dwFourCC;
  DWORD dwRGBBitCount;
  DWORD dwRBitMask;
  DWORD dwGBitMask;
  DWORD dwBBitMask;
  DWORD dwABitMask;
};
"""


class DDSHeaderFlags(enum.Flag):
    CAPS = 0x1
    HEIGHT = 0x2
    WIDTH = 0x4
    PITCH = 0x8
    PIXEL_FORMAT = 0x1000
    MIPMAP_COUNT = 0x20000
    LINEAR_SIZE = 0x80000
    DEPTH = 0x800000


@dataclass
class DDSHeader:
    flags: DDSHeaderFlags
    height: int
    width: int
    pitch_or_linear_size: int
    depth: int
    mip_map_count: int
    reserved1: tuple[int, int, int, int, int, int, int, int, int, int, int]
    pixel_format: PixelFormat
    caps: int
    caps2: int
    caps3: int
    caps4: int
    reserved2: int

    @classmethod
    def from_bytes(cls, data: bytes) -> DDSHeader:
        header_data = _DDS_header_struct.unpack(data)
        return cls(
            flags=DDSHeaderFlags(header_data[1]),
            height=header_data[2],
            width=header_data[3],
            pitch_or_linear_size=header_data[4],
            depth=header_data[5],
            mip_map_count=header_data[6],
            reserved1=typing.cast(tuple[int, int, int, int, int, int, int, int, int, int, int], header_data[7:18]),
            pixel_format=PixelFormat.from_bytes(header_data[18]),
            caps=header_data[19],
            caps2=header_data[20],
            caps3=header_data[21],
            caps4=header_data[22],
            reserved2=header_data[23]
        )

class PixelFormatFourCC(enum.Enum):
    DXT1 = b'DXT1'
    DXT3 = b'DXT3'
    DXT5 = b'DXT5'


class PixelFormatFlags(enum.Flag):
    ALPHA_PIXELS = 0x1
    ALPHA = 0x2
    FOURCC = 0x4
    RGB = 0x40
    YUV = 0x200
    LUMINANCE = 0x20000


@dataclass
class PixelFormat:
    flags: PixelFormatFlags
    four_cc: PixelFormatFourCC
    rgb_bit_count: int
    r_bit_mask: int
    g_bit_mask: int
    b_bit_mask: int
    a_bit_mask: int

    @classmethod
    def from_bytes(cls, data: bytes) -> PixelFormat:
        pixel_format_data = _DDS_pixel_format_struct.unpack(data)
        return cls(
            flags=PixelFormatFlags(pixel_format_data[1]),
            four_cc=PixelFormatFourCC(pixel_format_data[2]),
            rgb_bit_count=pixel_format_data[3],
            r_bit_mask=pixel_format_data[4],
            g_bit_mask=pixel_format_data[5],
            b_bit_mask=pixel_format_data[6],
            a_bit_mask=pixel_format_data[7],
        )


class TextureDDS:
    class GLInternalFormat(enum.IntEnum):
        RGB_DXT1 = GL.GL_COMPRESSED_RGB_S3TC_DXT1_EXT
        RGBA_DXT1 = GL.GL_COMPRESSED_RGBA_S3TC_DXT1_EXT
        RGBA_DXT3 = GL.GL_COMPRESSED_RGBA_S3TC_DXT3_EXT
        RGBA_DXT5 = GL.GL_COMPRESSED_RGBA_S3TC_DXT5_EXT

    header: DDSHeader
    texture_data: np.ndarray

    gl_texture_id: int | None
    gl_internal_format: GLInternalFormat

    def __init__(self):
        self.header = None
        self.texture_data = None
        self.gl_texture_id = None
        self.gl_internal_format = None

    def __del__(self):
        if self.gl_texture_id is not None:
            GL.glDeleteTextures(1, ctypes.byref(ctypes.c_uint(self.gl_texture_id)))
            self.gl_texture_id = None

    @classmethod
    def from_bytes(cls, data: typing_extensions.Buffer) -> TextureDDS:
        if data[:4] != b'DDS ':
            raise ValueError("Not a DDS file? (missing magic bytes 'DDS ')")

        if len(data[4:]) < _DDS_header_struct.size:
            raise ValueError("Bad DDS file (no space for header)")

        result = TextureDDS()
        result.header = DDSHeader.from_bytes(data[4:4 + _DDS_header_struct.size])
        result.texture_data = np.frombuffer(data[4 + _DDS_header_struct.size:], dtype='b')

        match result.header.pixel_format.four_cc:
            case PixelFormatFourCC.DXT1:
                result.gl_internal_format = TextureDDS.GLInternalFormat.RGBA_DXT1
            case PixelFormatFourCC.DXT3:
                result.gl_internal_format = TextureDDS.GLInternalFormat.RGBA_DXT3
            case PixelFormatFourCC.DXT5:
                result.gl_internal_format = TextureDDS.GLInternalFormat.RGBA_DXT5
            case other:
                raise ValueError(f"Unsupported DDS format: {other}")

        return result

    def load_into_opengl(self):
        if self.gl_texture_id is not None:
            return

        # ensure that at least the base level (0) is loaded
        mipmap_count = max(1, self.header.mip_map_count)

        tex_id = ctypes.c_uint(0)
        GL.glGenTextures(1, ctypes.byref(tex_id))
        self.gl_texture_id = tex_id.value
        GL.glBindTexture(GL.GL_TEXTURE_2D, self.gl_texture_id)

        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_BASE_LEVEL, 0)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAX_LEVEL, mipmap_count - 1)

        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)

        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MIN_FILTER, GL.GL_LINEAR_MIPMAP_LINEAR)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_MAG_FILTER, GL.GL_LINEAR)

        width = self.header.width
        height = self.header.height
        block_size = 8 if self.gl_internal_format == TextureDDS.GLInternalFormat.RGB_DXT1 else 16

        GL.glTexStorage2D(GL.GL_TEXTURE_2D, mipmap_count, self.gl_internal_format.value, width, height)

        offset = 0
        tex_ptr = ctypes.c_void_p(self.texture_data.ctypes.data)
        for i in range(mipmap_count):
            if width == 0 or height == 0:
                warnings.warn(
                    f"Warning: DDS texture {self.gl_texture_id} has mipmap level {i} with zero dimensions."
                    f" ({mipmap_count} total levels supposed to exist)"
                )
                break

            size = ((width + 3) // 4) * ((height + 3) // 4) * block_size

            GL.glCompressedTexSubImage2D(
                GL.GL_TEXTURE_2D,
                i, 0, 0, width, height,
                self.gl_internal_format.value,
                size,
                ctypes.c_void_p(tex_ptr.value + offset),
            )

            offset += size
            width = max(1, width // 2)
            height = max(1, height // 2)

    def load_mgl(self):
        self.load_into_opengl()
        mgl_tex = moderngl.get_context().external_texture(
            self.gl_texture_id,
            (self.header.width, self.header.height),
            4,
            0,
            'f1'
        )
        setattr(mgl_tex, '_base_dds_texture_obj', self)
        return mgl_tex

    def use(self):
        if self.gl_texture_id is None:
            raise ValueError("Texture not loaded into OpenGL")

        GL.glBindTexture(GL.GL_TEXTURE_2D, self.gl_texture_id)