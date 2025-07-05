from animation_viewer.camera_window import CameraWindow
from unit_animation_engine.fixed_tick_runner import FixedUpdateTicker


class FixedUpdateWindow(CameraWindow):
    """Base class with built-in 3D camera support and fixed update ticker"""

    gl_version = (4, 6)
    window_size = (800, 800)
    aspect_ratio = 1.0
    clear_color = (0.2, 0.2, 0.2, 1.0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ticker = FixedUpdateTicker(self.on_fixed_update)

        wnd = kwargs.get('wnd')
        if wnd:
            wnd_render = getattr(wnd, 'render')
            if wnd_render:
                setattr(wnd, 'render', self.__decorate_wnd_render(wnd_render))

    def __decorate_wnd_render(self, wnd_render_func):
        def wrapped_render(current_time: float, delta: float):
            self.ticker.update(delta)
            wnd_render_func(current_time, delta)

        return wrapped_render

    def on_fixed_update(self, tick_info: FixedUpdateTicker.TickInfo):
        """Override this method to implement fixed update logic."""
        pass
