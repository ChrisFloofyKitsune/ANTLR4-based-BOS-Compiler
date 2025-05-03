from pathlib import Path

import moderngl
import moderngl_window as mglw
from moderngl_window import geometry as mglw_geometry
from moderngl_window.opengl.vao import VAO
from moderngl_window.scene.camera import KeyboardCamera
from pyglm import glm
import numpy as np

from animation_viewer.texture_dds import TextureDDS
from unit_animation_engine.s3o import S3OModel


class CameraWindow(mglw.WindowConfig):
    """Base class with built-in 3D camera support"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.camera = KeyboardCamera(self.wnd.keys, aspect_ratio=self.wnd.aspect_ratio)
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


class MGLWindow(CameraWindow):
    gl_version = (4, 6)
    window_size = (800, 800)
    aspect_ratio = 1.0
    clear_color = (0.25, 0.25, 0.25, 1.0)
    resource_dir = Path(__file__).parent

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.wnd.mouse_exclusivity = True
        self.cube = mglw_geometry.cube(size=(2, 2, 2))
        self.prog = self.load_program(
            vertex_shader="basic_unit_shader.vert.glsl",
            fragment_shader="basic_unit_shader.frag.glsl",
        )

        with open("E:/bar_dev/Beyond-All-Reason/objects3d/Units/legcom.s3o", 'rb') as f:
            self.s3o_legcom = S3OModel.from_bytes(f.read())

        with open("E:/bar_dev/Beyond-All-Reason/unittextures/leg_color.dds", 'rb') as f:
            self.leg_color_texture = TextureDDS.from_bytes(f.read())
        self.leg_color_texture.load_into_opengl()

        vertex_data = []
        indices = []
        for piece in self.s3o_legcom.pieces():
            index_offset = len(vertex_data)
            for vertex in piece.vertices:
                vertex_data.append((vertex.position, vertex.normal, vertex.tex_coords))
            indices.extend(idx + index_offset for idx in piece.indices)

        vertex_data = np.array(vertex_data, dtype='3f4, 3f4, 2f4')
        indices = np.array(indices, dtype='u4')

        self.legcom_vao = VAO("geometry:legcom")
        self.legcom_vao.buffer(vertex_data, '3f4 3f4 2f4', ['in_position', 'in_normal', 'in_uv'])
        self.legcom_vao.index_buffer(indices)

    def on_render(self, time: float, frametime: float):
        self.ctx.enable_only(moderngl.CULL_FACE | moderngl.DEPTH_TEST)

        model_view = glm.scale(glm.vec3(0.25))

        self.prog["u_projection"].write(self.camera.projection.matrix)
        self.prog["u_view"].write(self.camera.matrix)
        self.prog["u_model"].write(model_view)
        self.prog["u_normal_matrix"].write(glm.transpose(glm.inverse(glm.mat3(model_view))))

        self.leg_color_texture.use()
        self.legcom_vao.render(self.prog)


if __name__ == "__main__":
    MGLWindow.run()
