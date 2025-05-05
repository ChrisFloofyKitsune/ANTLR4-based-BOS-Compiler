from pathlib import Path

import moderngl
from pyglm import glm

from animation_viewer.texture_dds import TextureDDS
from animation_viewer.s3o_utils import build_vao_from_s3o_model, transforms_from_s3o_model
from animation_viewer.camera_window import CameraWindow
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

        self.legcom_transforms = transforms_from_s3o_model(self.s3o_legcom)
        self.legcom_vao = build_vao_from_s3o_model("legcom", self.s3o_legcom)

        self.piece_matrices_data = bytearray()
        for transform in self.legcom_transforms.values():
            self.piece_matrices_data.extend(transform.model_space_matrix.to_bytes())
        self.piece_matrices_buffer = self.ctx.buffer(self.piece_matrices_data)

    def on_render(self, time: float, frametime: float):
        self.ctx.enable_only(moderngl.CULL_FACE | moderngl.DEPTH_TEST)

        model_view = glm.identity(glm.mat4)

        self.prog["u_projection"].write(self.camera.projection.matrix)
        self.prog["u_view"].write(self.camera.matrix)
        self.prog["u_model"].write(model_view)
        self.prog["u_normal_matrix"].write(glm.transpose(glm.inverse(glm.mat3(model_view))))

        pelvis_transform = self.legcom_transforms[self.s3o_legcom.find_piece("pelvis")]
        pelvis_transform.rotation.y += glm.radians(50 * frametime)

        torso_transform = self.legcom_transforms[self.s3o_legcom.find_piece("torso")]
        torso_transform.rotation.y -= glm.radians(50 * frametime)

        head_transform = self.legcom_transforms[self.s3o_legcom.find_piece("head")]
        head_transform.rotation.y -= glm.radians(50 * frametime)

        self.piece_matrices_data = bytearray()
        for transform in self.legcom_transforms.values():
            self.piece_matrices_data.extend(transform.model_space_matrix.to_bytes())

        self.piece_matrices_buffer.clear()
        self.piece_matrices_buffer.write(self.piece_matrices_data)
        self.piece_matrices_buffer.bind_to_storage_buffer(0)

        self.leg_color_texture.use()
        self.legcom_vao.render(self.prog)


if __name__ == "__main__":
    MGLWindow.run()
