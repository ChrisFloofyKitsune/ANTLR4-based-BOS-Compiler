from __future__ import annotations

import moderngl_window as mglw
from moderngl_window.scene import KeyboardCamera


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
