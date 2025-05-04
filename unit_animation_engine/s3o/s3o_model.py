from __future__ import annotations

import struct
from enum import Enum
from typing import NamedTuple, Self


from unit_animation_engine.math import float3, float2
from unit_animation_engine import math

_S3OHeader_struct = struct.Struct("< 12s i 5f 4i")
"""
* magic bytes "Spring unit\\\\0"
* version
* radius, height, mid.x, mid.y, mid.z
* root_piece_offset, collision_data_offset (0, unimplemented), texture1_offset, texture2_offset
"""

_S3OPiece_struct = struct.Struct("< 10i 3f")
"""
* name_offset, num_children, num_vertices, vertices_offset, vertex_type (0, unimplemented),
  primitive_type, num_face_indices, face_indices_offset, collision_data_offset (0, unimplemented)
* offset.x, offset.y, offset.z

primitive_type
    * 0: triangles
    * 1: triangle strips (end of current strip marked with 0xffffffff)
    * 2: quads
"""

_S3OVertex_struct = struct.Struct("< 3f 3f 2f")
"""
* position
* normal
* tex_coord
"""

_S3OChildOffset_struct = struct.Struct("< i")
_S3OIndex_struct = struct.Struct("< i")

def extract_null_terminated_string(data: bytes, offset: int) -> str:
    """
    :param data: raw bytes
    :param offset: offset into bytes
    :return: bytes up to (not including) '\0' decoded as utf8 string
    """
    if offset == 0:
        return b"".decode()
    else:
        return data[offset:data.index(b'\x00', offset)].decode()

class S3OVertex(NamedTuple):
    position: float3 = float3()
    normal: float3 = float3()
    tex_coords: float2 = float2()

    def with_position(self, position: float3):
        return S3OVertex(position, self.normal, self.tex_coords)

    def with_normal(self, normal: float3):
        return S3OVertex(self.position, normal, self.tex_coords)

    @property
    def ambient_occlusion(self) -> float:
        # ao is packed into the last ~7-8 bits of the texture U coordinate as a miniscule fractional value
        # #BlameBeherith for this fractional float value abuse
        return (self.tex_coords[0] * 2 ** 14) % 1.0

    @ambient_occlusion.setter
    def ambient_occlusion(self, value) -> None:
        # don't use full range so that rounding errors don't eat the packed in ao
        value = min(0.98, max(0.02, value))

        self.tex_coords[0] = (math.floor(self.tex_coords[0] * (2 ** 14)) / 2 ** 14) + (value / (2 ** 14))


class S3OPiece:
    class PrimitiveType(Enum):
        Triangles = 0
        TriangleStrips = 1
        Quads = 2

    name: str

    parent: S3OPiece | None
    parent_offset: float3

    children: list['S3OPiece']

    vertices: list[S3OVertex]
    indices: list[int]
    primitive_type: PrimitiveType

    def __init__(self):
        self.name = 'unnamed'

        self.parent = None
        self.parent_offset = float3()

        self.children = list()

        self.vertices = list()
        self.indices = list()
        self.primitive_type = S3OPiece.PrimitiveType.Triangles

    @classmethod
    def from_bytes(cls, data: bytes, offset: int, parent: 'S3OPiece | None' = None) -> Self:
        piece = S3OPiece()

        if data == b'':
            return piece

        name_offset, num_children, children_offset, num_vertices, \
            vertex_offset, vertex_type, primitive_type, num_indices, \
            index_offset, collision_data_offset, \
            x_offset, y_offset, z_offset = _S3OPiece_struct.unpack_from(data, offset)

        piece.name = extract_null_terminated_string(data, name_offset)

        piece.parent = parent
        piece.parent_offset = float3(x_offset, y_offset, z_offset)

        piece.primitive_type = primitive_type

        piece.vertices = []
        for i in range(num_vertices):
            current_offset = vertex_offset + _S3OVertex_struct.size * i
            vertex = _S3OVertex_struct.unpack_from(data, current_offset)

            position = float3(vertex[:3])
            normal = float3(vertex[3:6])
            tex_coords = float2(vertex[6:])

            piece.vertices.append(S3OVertex(position, normal, tex_coords))

        piece.indices = []
        for i in range(num_indices):
            current_offset = index_offset + _S3OIndex_struct.size * i
            index, = _S3OIndex_struct.unpack_from(data, current_offset)
            piece.indices.append(index)

        piece.children = []
        for i in range(num_children):
            cur_offset = children_offset + _S3OChildOffset_struct.size * i
            child_offset, = _S3OChildOffset_struct.unpack_from(data, cur_offset)
            piece.children.append(S3OPiece.from_bytes(data, child_offset, piece))

        return piece

    def triangulate_faces(self):
        idx_len = len(self.indices)

        match self.primitive_type:
            case S3OPiece.PrimitiveType.Triangles:
                pass
            case S3OPiece.PrimitiveType.TriangleStrips:
                if idx_len < 3:
                    self.primitive_type = S3OPiece.PrimitiveType.Triangles
                    self.indices.clear()
                    return

                new_idx: list[int] = []

                for i in range(idx_len - 2):
                    # indices can instead be end-of-strip markers (-1)
                    if all(idx != -1 for idx in self.indices[i:i + 2]):
                        new_idx.extend(self.indices[i:i + 2])

                self.primitive_type = S3OPiece.primitive_type.Triangles
                self.indices = new_idx

            case S3OPiece.PrimitiveType.Quads:
                if len(self.indices) % 4 != 0:
                    self.primitive_type = S3OPiece.PrimitiveType.Triangles
                    self.indices.clear()
                    return

                new_idx: list[int] = []
                for i in range(0, idx_len, 4):
                    new_idx.extend(self.indices[i:i + 2])
                    new_idx.extend(self.indices[i + n] for n in [0, 2, 3])

                self.primitive_type = S3OPiece.PrimitiveType.Triangles
                self.indices = new_idx


class S3OModel:
    collision_radius: float
    height: float
    midpoint: float3
    texture_path_1: str
    texture_path_2: str
    root_piece: S3OPiece

    @classmethod
    def from_bytes(cls, data: bytes) -> Self:
        header = _S3OHeader_struct.unpack_from(data, 0)

        magic, version, radius, height, mid_x, mid_y, mid_z, \
            root_piece_offset, collision_data_offset, tex1_offset, \
            tex2_offset = header

        assert (magic == b'Spring unit\x00')
        assert (version == 0)
        assert (collision_data_offset == 0)

        s3o = S3OModel()

        s3o.collision_radius = radius
        s3o.height = height
        s3o.midpoint = float3(mid_x, mid_y, mid_z)

        s3o.texture_path_1 = extract_null_terminated_string(data, tex1_offset)
        s3o.texture_path_2 = extract_null_terminated_string(data, tex2_offset)

        s3o.root_piece = S3OPiece.from_bytes(data, root_piece_offset)

        s3o.root_piece.triangulate_faces()

        return s3o

    def pieces(self) -> list[S3OPiece]:
        pieces = []

        def traverse(piece: S3OPiece):
            pieces.append(piece)
            for child in piece.children:
                traverse(child)

        traverse(self.root_piece)
        return pieces

    def find_piece(self, search_name: str) -> S3OPiece | None:
        for piece in self.pieces():
            if piece.name == search_name:
                return piece
        return None