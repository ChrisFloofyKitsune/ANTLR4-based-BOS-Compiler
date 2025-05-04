import struct

import moderngl_window as mglw
from moderngl_window.opengl.vao import VAO
from moderngl_window.scene import KeyboardCamera
from pyglm import glm

from unit_animation_engine.s3o import S3OPiece
from unit_animation_engine.transform import Transform


def build_vao_from_s3o_model(model_name, s3o_model):
    vertex_data = []
    indices = []
    piece_id_map = {}
    for piece_id, piece in enumerate(s3o_model.pieces()):
        piece_id_map[piece] = piece_id

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
                + glm.ivec2(piece_id, piece_id_map.get(piece.parent, -1)).to_bytes()
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


def transforms_from_s3o_model(s3o_model) -> dict[S3OPiece, Transform]:
    transforms = {}
    for piece in s3o_model.pieces():
        transforms[piece] = Transform(
            position=piece.parent_offset,
            parent=transforms.get(piece.parent, None)
        )
    return transforms


class CameraWindow(mglw.WindowConfig):
    """Base class with built-in 3D camera support"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera = KeyboardCamera(
            self.wnd.keys,
            aspect_ratio=self.wnd.aspect_ratio,
            fov=45.0,
            near=0.1,
            far=1000.0,
        )
        self.camera_enabled = True

    def on_key_event(self, key, action, modifiers):
        keys = self.wnd.keys

        if self.camera_enabled:
            self.camera.key_input(key, action, modifiers)

        if action == keys.ACTION_PRESS:
            if key == keys.C:
                self.camera_enabled = not self.camera_enabled
                self.wnd.mouse_exclusivity = self.camera_enabled
                self.wnd.cursor = not self.camera_enabled
            if key == keys.SPACE:
                self.timer.toggle_pause()

    def on_mouse_position_event(self, x: int, y: int, dx, dy):
        if self.camera_enabled:
            self.camera.rot_state(-dx, -dy)

    def on_resize(self, width: int, height: int):
        self.camera.projection.update(aspect_ratio=self.wnd.aspect_ratio)

    def on_mouse_scroll_event(self, x_offset: float, y_offset: float) -> None:
        velocity = self.camera.velocity + y_offset
        self.camera.velocity = max(velocity, 1.0)
