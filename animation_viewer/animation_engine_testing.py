from pathlib import Path

import moderngl
from pyglm import glm

from animation_engine.animation_engine import AnimationEngine
from animation_engine.animator import Animator
from animation_engine.data_types import Axis
from animation_engine.fixed_tick_runner import FixedUpdateTicker
from animation_engine.transform import Transform
from animation_viewer.fixed_update_window import FixedUpdateWindow


class AnimationEngineTestingWindow(FixedUpdateWindow):

    resource_dir = Path(__file__, "../resources").resolve()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.wnd.title = "Animation Engine Testing"
        self.animation_engine = AnimationEngine()

        self.scene = self.load_scene("fox/Fox.gltf")
        self.camera.position = self.scene.bbox_max * 0.1
        self.fox_node = self.scene.find_node('fox')

        self.fox_transform = Transform()
        self.fox_animator = Animator(self.animation_engine)
        self.target_positions = [
            glm.vec3(10, 0, 0),
            glm.vec3(0, 10, 0),
            glm.vec3(-10, 0, 0),
            glm.vec3(0, -10, 0),
            glm.vec3(0, 0, 0)
        ]

    def on_render(self, time: float, frame_time: float) -> None:
        self.ctx.enable_only(moderngl.CULL_FACE | moderngl.DEPTH_TEST)

        self.scene.draw(
            self.camera.projection.matrix,
            self.camera.matrix,
            time
        )

        self.ctx.disable(moderngl.CULL_FACE | moderngl.DEPTH_TEST)

    def on_fixed_update(self, tick_info: FixedUpdateTicker.TickInfo) -> None:
        self.animation_engine.tick(tick_info.fixed_tick_rate)
        self.fox_node.matrix = self.fox_transform.model_space_matrix
        self.scene.matrix = glm.scale(glm.vec3(0.1))

        if not self.fox_animator.is_transform_in_animation(self.fox_transform):
            target = self.target_positions.pop(0)
            self.target_positions.append(target)
            self.fox_animator.move_3d(self.fox_transform, target, 10)

    def on_close(self) -> None:
        self.animation_engine.shutdown()


if __name__ == '__main__':
    AnimationEngineTestingWindow.run()
