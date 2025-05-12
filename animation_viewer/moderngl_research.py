import ctypes
import textwrap
from pathlib import Path

import moderngl
import pyglet.window
from pyglm import glm

from animation_viewer.camera_window import CameraWindow
from animation_viewer.texture_dds import TextureDDS
from unit_animation_engine.fixed_tick_runner import FixedTickRunner
from unit_animation_engine.local_model import LocalModel
from unit_animation_engine.s3o import S3OModel


class MGLWindow(CameraWindow):
    gl_version = (4, 6)
    window_size = (800, 800)
    aspect_ratio = 1.0
    clear_color = (0.2, 0.2, 0.2, 1.0)
    resource_dir = Path(__file__).parent

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.wnd.mouse_exclusivity = True
        self.camera.velocity *= 4
        self.camera.position = glm.vec3(0, 0, 100)

        self.prog = self.load_program(
            vertex_shader="basic_unit_shader.vert.glsl",
            fragment_shader="basic_unit_shader.frag.glsl",
        )

        with open("E:/bar_dev/Beyond-All-Reason/objects3d/Units/legcom.s3o", 'rb') as f:
            self.s3o_legcom = S3OModel.from_bytes(f.read())

        with open("E:/bar_dev/Beyond-All-Reason/unittextures/leg_color.dds", 'rb') as f:
            self.leg_color_texture = TextureDDS.from_bytes(f.read())
        self.leg_color_texture.load_into_opengl()

        self.legcom_model = LocalModel.from_s3o_model(self.s3o_legcom, "legcom")
        self.legcom_vao = self.legcom_model.build_vao()

        self.piece_matrices_data = bytearray()
        for transform in self.legcom_model.piece_list:
            self.piece_matrices_data.extend(transform.model_space_matrix.to_bytes())
        self.piece_matrices_buffer = self.ctx.buffer(self.piece_matrices_data)

        self.piece_select = -1

        self.label = pyglet.text.Label(
            "legcom",
            font_name='Cascadia Mono',
            font_size=16,
            y=self.wnd.height,
            anchor_y='top',
            multiline=True,
            width=10000
        )

        self.tick_info_label = pyglet.text.Label(
            "tick_info",
            font_name='Cascadia Mono',
            anchor_y="bottom",
            font_size=16,
            multiline=True,
            width=10000
        )

        self.fixed_tick_runner = FixedTickRunner(self.fixed_update)

    def on_key_event(self, key, action, modifiers):
        super().on_key_event(key, action, modifiers)
        if action == self.wnd.keys.ACTION_PRESS:
            match key:
                case self.wnd.keys.LEFT:
                    self.piece_select = max(-1, self.piece_select - 1)
                case self.wnd.keys.RIGHT:
                    self.piece_select = min(len(self.legcom_model.piece_list) - 1, self.piece_select + 1)

    def fixed_update(self, tick_info: FixedTickRunner.TickInfo):
        self.tick_info_label.text = textwrap.dedent(
            f"""
            ticks: {tick_info.fixed_tick_count}
            fixed time : {tick_info.fixed_time_elapsed: >10.2f}
            actual time: {tick_info.actual_time_elapsed: >10.2f}
            """
        ).strip()

    def on_render(self, time: float, frametime: float):
        self.fixed_tick_runner.update(frametime)

        self.ctx.enable_only(moderngl.CULL_FACE | moderngl.DEPTH_TEST)

        model_view = glm.identity(glm.mat4)

        self.prog["u_projection"].write(self.camera.projection.matrix)
        self.prog["u_view"].write(self.camera.matrix)
        self.prog["u_model"].write(model_view)
        self.prog["dbg_piece_select"].write(ctypes.c_int(self.piece_select))

        self.piece_matrices_data = bytearray()
        for transform in self.legcom_model.piece_list:
            self.piece_matrices_data.extend(transform.model_space_matrix.to_bytes())

        self.piece_matrices_buffer.clear()
        self.piece_matrices_buffer.write(self.piece_matrices_data)
        self.piece_matrices_buffer.bind_to_storage_buffer(0)

        self.leg_color_texture.use()
        self.legcom_vao.render(self.prog)

        self.ctx.disable(moderngl.CULL_FACE | moderngl.DEPTH_TEST)

        if self.piece_select == -1:
            self.label.text = self.legcom_model.model_name
        else:
            piece = self.legcom_model.piece_list[self.piece_select]
            scale = glm.vec3()
            orientation = glm.quat()
            translation = glm.vec3()
            skew = glm.vec3()
            perspective_ = glm.vec4()
            glm.decompose(piece.model_space_matrix, scale, orientation, translation, skew, perspective_)

            rotation = glm.eulerAngles(orientation) / glm.pi() * 180

            self.label.text = textwrap.dedent(
                f"""
                {self.legcom_model.model_name}
                {piece.model_piece_index}
                T: {translation.x: >z5.2f}, {translation.y: >z5.2f}, {translation.z: >z5.2f}
                R: {rotation.x: >z5.1f}, {rotation.y: >z5.1f}, {rotation.z: >z5.1f}
                """
            ).strip()
        self.label.draw()
        self.tick_info_label.draw()


if __name__ == "__main__":
    MGLWindow.run()
