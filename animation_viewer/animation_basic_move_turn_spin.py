import moderngl
import moderngl_window as mgw
import moderngl_window.geometry
import moderngl_window.scene
import pyglm as glm
from moderngl_window.geometry import AttributeNames
from moderngl_window.scene import Node, Mesh, Material
from pyglet.gl import GL_FLOAT

from animation_viewer.fixed_update_window import FixedUpdateWindow
from animation_engine import anim_functions
from animation_engine.fixed_tick_runner import FixedUpdateTicker


class ColorMaterial(Material):
    def __init__(self, name: str, color: tuple[float, float, float, float]):
        """
        Initializes a color material with the given name and RGBA color.

        Args:
            name (str): The name of the material.
            color (tuple[float, float, float, float]): The RGBA color of the material.
        """
        super().__init__(name=name)
        self.color = color


class BasicAnimationsWindow(FixedUpdateWindow):
    """Base class for animation research with fixed update ticker and 3D camera support"""

    clear_color = (0.5, 0.5, 0.5, 1.0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.wnd.title = "Basic Animations"

        self.scene = mgw.scene.Scene("anim_research_scene")

        def make_cube(name, color):
            node = Node(
                name=name,
                mesh=Mesh(
                    name=f"{name} mesh",
                    vao=mgw.geometry.cube(),
                    material=ColorMaterial(f'{name} material', color),
                    attributes={
                        "POSITION": {"name": AttributeNames.POSITION, "components": 3, "type": GL_FLOAT},
                        "NORMAL": {"name": AttributeNames.NORMAL, "components": 3, "type": GL_FLOAT},
                    }
                )
            )

            self.scene.root_nodes.append(node)
            self.scene.meshes.append(node.mesh)
            return node

        self.red_cube = make_cube("red", (1, 0, 0, 1))
        self.red_cube.matrix = glm.translate(glm.vec3(-2, 0, 0))

        self.green_cube = make_cube("green", (0, 1, 0, 1))
        self.green_cube.matrix = glm.translate(glm.vec3(0, 0, 0))

        self.blue_cube = make_cube("blue", (0, 0, 1, 1))
        self.blue_cube.matrix = glm.translate(glm.vec3(2, 0, 0))

        self.scene.prepare()

        self.camera.position = glm.vec3(0, 0.5, 10)

        # -----------------#
        # ANIMATION STUFF #
        # -----------------#

        self.red_anim_translate_targets = [
            glm.vec3(-2, 2, 0),
            glm.vec3(-4, 2, 0),
            glm.vec3(-4, 0, 0),
            glm.vec3(-2, 0, 0),
        ]
        self.red_cube_pos = glm.vec3(-2, 0, 0)

        self.green_anim_rotate_targets = [
            glm.vec3(0, 90, 0),
            glm.vec3(90, 90, 10),
            glm.vec3(90, 180, 45),
            glm.vec3(-90, 90, 90),
            glm.vec3(0, 0, 0),
        ]
        self.green_anim_rotate_targets = list(map(glm.radians, self.green_anim_rotate_targets))
        self.green_cube_rotation = glm.vec3(0, 0, 0)

        self.blue_anim_spin_velocity_targets = [
            #5 rps... 300 rpm
            360 * 5,
            -360 * 5,
        ]
        self.blue_anim_spin_velocity_targets = list(map(glm.radians, self.blue_anim_spin_velocity_targets))
        self.blue_cube_roll_angle = 0
        self.blue_cube_spin_velocity = 0

    def on_render(self, time: float, frame_time: float) -> None:
        """Override this method to implement rendering logic."""
        self.ctx.clear(*self.clear_color)
        self.ctx.enable(moderngl.CULL_FACE | moderngl.DEPTH_TEST)

        self.scene.prepare()
        self.scene.draw(
            self.camera.projection.matrix,
            self.camera.matrix
        )

    def on_fixed_update(self, tick_info: FixedUpdateTicker.TickInfo) -> None:
        self.update_red_cube(tick_info)
        self.update_green_cube(tick_info)
        self.update_blue_cube(tick_info)

    def update_red_cube(self, tick_info: FixedUpdateTicker.TickInfo):
        all_done = True
        for coord_idx in (0, 1, 2):
            done, new_pos = anim_functions.move_toward_target_position(
                self.red_cube_pos[coord_idx], self.red_anim_translate_targets[0][coord_idx],
                2,
                tick_info.fixed_tick_rate
            )
            all_done = all_done and done
            self.red_cube_pos[coord_idx] = new_pos
        if all_done:
            self.red_anim_translate_targets.append(self.red_anim_translate_targets.pop(0))
        self.red_cube.matrix = glm.translate(self.red_cube_pos)

    def update_green_cube(self, tick_info: FixedUpdateTicker.TickInfo):
        all_done = True
        for coord_idx in (0, 1, 2):
            done, new_rot = anim_functions.turn_toward_target_rotation(
                self.green_cube_rotation[coord_idx], self.green_anim_rotate_targets[0][coord_idx],
                glm.radians(90),
                tick_info.fixed_tick_rate
            )
            all_done = all_done and done
            self.green_cube_rotation[coord_idx] = new_rot
        if all_done:
            self.green_anim_rotate_targets.append(self.green_anim_rotate_targets.pop(0))
        self.green_cube.matrix = (
            glm.rotate(self.green_cube_rotation.y, glm.vec3(0, 1, 0))
            @ glm.rotate(self.green_cube_rotation.x, glm.vec3(1, 0, 0))
            @ glm.rotate(self.green_cube_rotation.z, glm.vec3(0, 0, 1))
        )

    def update_blue_cube(self, tick_info: FixedUpdateTicker.TickInfo):
        done, new_angle, new_velocity = anim_functions.spin_toward_target_velocity(
            self.blue_cube_roll_angle,
            self.blue_cube_spin_velocity,
            self.blue_anim_spin_velocity_targets[0],
            glm.radians(360),
            tick_info.fixed_tick_rate,
        )

        # spinning will keep animating unless it's slowing to a stop, check if it's reached target speed manually
        done = done or (new_velocity == self.blue_anim_spin_velocity_targets[0])

        self.blue_cube_roll_angle = new_angle
        self.blue_cube_spin_velocity = new_velocity

        if done:
            self.blue_anim_spin_velocity_targets.append(self.blue_anim_spin_velocity_targets.pop(0))

        self.blue_cube.matrix = glm.translate(glm.vec3(2, 0, 0)) @ glm.rotate(self.blue_cube_roll_angle, glm.vec3(0, 0, 1))


if __name__ == "__main__":
    BasicAnimationsWindow.run()
