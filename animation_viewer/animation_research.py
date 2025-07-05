from animation_viewer.fixed_update_window import FixedUpdateWindow
from unit_animation_engine.fixed_tick_runner import FixedUpdateTicker


class AnimResearchWindow(FixedUpdateWindow):
    """Base class for animation research with fixed update ticker and 3D camera support"""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Animation Research"

    def on_render(self, time: float, frame_time: float) -> None:
        """Override this method to implement rendering logic."""
        self.ctx.clear()

    def on_fixed_update(self, tick_info: FixedUpdateTicker.TickInfo):
        print(tick_info)

if __name__ == "__main__":
    AnimResearchWindow.run()
