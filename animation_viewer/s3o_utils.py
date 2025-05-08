from __future__ import annotations

import struct

from moderngl_window.opengl.vao import VAO
from pyglm import glm

from unit_animation_engine.s3o import S3OPiece, S3OModel
from unit_animation_engine.transform import Transform


def build_vao_from_s3o_model(model_name, s3o_model):
    vertex_data = []
    indices = []

    for piece in s3o_model.pieces:
        piece_offset = piece.parent_offset
        parent = piece.parent
        while parent:
            piece_offset = piece_offset + parent.parent_offset
            parent = parent.parent

        index_offset = len(vertex_data)
        indices.extend(struct.pack('l', idx + index_offset) for idx in piece.indices)

        for vertex in piece.vertices:
            vertex_bytes = (
                vertex.position.to_bytes() + vertex.normal.to_bytes() + vertex.tex_coords.to_bytes()
                + glm.ivec2(piece.index, piece.parent.index if piece.parent else -1).to_bytes()
            )
            vertex_data.append(vertex_bytes)

    vao = VAO(f"geometry:{model_name}")
    vao.buffer(
        b''.join(vertex_data),
        '3f4 3f4 2f4 2i4',
        ['in_position', 'in_normal', 'in_uv', 'in_piece_info']
    )
    vao.index_buffer(b''.join(indices))
    return vao


def transforms_from_s3o_model(s3o_model: S3OModel) -> dict[S3OPiece, Transform]:
    transforms = {}
    for piece in s3o_model.pieces:
        transforms[piece] = Transform(
            base_matrix=glm.translate(piece.parent_offset),
            parent=transforms.get(piece.parent, None)
        )
    return transforms
