from __future__ import annotations

import struct

from moderngl_window.opengl.vao import VAO

from animation_engine.math import *
from animation_engine.s3o import S3OPiece, S3OModel
from animation_engine.transform import Transform
from animation_engine.types_ import ModelPieceIndex, ScriptPieceIndex


class LocalModel:

    model_name: str

    base_model: S3OModel
    root_piece: LocalModelPiece
    piece_list: list[LocalModelPiece]
    piece_name_map: dict[str, LocalModelPiece]

    @classmethod
    def from_s3o_model(cls, s3o_model: S3OModel, name="<unnamed>"):
        current_piece_index = 0

        piece_list = []
        piece_name_map = {}

        for piece in s3o_model:
            model_index = ModelPieceIndex(current_piece_index, piece.name)
            lmp = LocalModelPiece(piece, model_index)

            piece_list.append(lmp)
            piece_name_map[piece.name] = lmp

            current_piece_index += 1

            if piece.parent:
                lmp.parent = piece_name_map[piece.parent.name]

        local_model = cls()
        local_model.model_name = name
        local_model.base_model = s3o_model
        local_model.root_piece = piece_list[0]
        local_model.piece_list = piece_list
        local_model.piece_name_map = piece_name_map

        return local_model

    def build_vao(self):
        vertex_data = []
        indices = []

        for piece in self.piece_list:
            index_offset = len(vertex_data)
            indices.extend(struct.pack('l', idx + index_offset) for idx in piece.base_model_piece.indices)

            for vertex in piece.base_model_piece.vertices:
                vertex_bytes = (
                    vertex.position.to_bytes() + vertex.normal.to_bytes() + vertex.tex_coords.to_bytes()
                    + glm.ivec2(int(piece.model_piece_index), int(piece.parent.model_piece_index) if piece.parent else -1).to_bytes()
                )
                vertex_data.append(vertex_bytes)

        vao = VAO(f"geometry:{self.model_name}")
        vao.buffer(
            b''.join(vertex_data),
            '3f4 3f4 2f4 2i4',
            ['in_position', 'in_normal', 'in_uv', 'in_piece_info']
        )
        vao.index_buffer(b''.join(indices))
        return vao


class LocalModelPiece(Transform):

    base_model_piece: S3OPiece
    model_piece_index: ModelPieceIndex
    script_piece_index: ScriptPieceIndex | None = None

    def __init__(self, base_model_piece: S3OPiece, model_piece_index: ModelPieceIndex):
        super().__init__()
        self.base_matrix=glm.translate(base_model_piece.parent_offset)
        self.base_model_piece = base_model_piece
        self.model_piece_index = model_piece_index

    def get_absolute_pos(self) -> float3:
        return self.model_space_matrix[3].xyz

    def get_emit_dir_pos(self) -> tuple[float3, float3]:
        match len(self.base_model_piece.vertices):
            case 0:
                return float3(0), float3(0, 0, 1)
            case 1:
                return float3(0), glm.normalize(self.base_model_piece.vertex_pos(0))
            case _:
                return (
                    self.base_model_piece.vertex_pos(0),
                    glm.normalize(self.base_model_piece.vertex_pos(1) - self.base_model_piece.vertex_pos(0))
                )

    def get_offset(self) -> float3:
        return self.base_matrix @ float3(0)

    def set_script_visible(self, visible) -> None:
        pass
