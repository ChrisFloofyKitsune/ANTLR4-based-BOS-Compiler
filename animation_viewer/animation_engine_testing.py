import moderngl

from animation_viewer.fixed_update_window import FixedUpdateWindow
from animation_engine.fixed_tick_runner import FixedUpdateTicker
from animation_engine.animation_engine import AnimationEngine


class AnimationEngineTestingWindow(FixedUpdateWindow):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.wnd.title = "Animation Engine Testing"
        self.animation_engine = AnimationEngine()

    def on_render(self, time: float, frame_time: float) -> None:
        self.ctx.enable_only(moderngl.CULL_FACE | moderngl.DEPTH_TEST)



        self.ctx.disable(moderngl.CULL_FACE | moderngl.DEPTH_TEST)

    def on_fixed_update(self, tick_info: FixedUpdateTicker.TickInfo) -> None:
        self.animation_engine.tick(tick_info.fixed_tick_rate)

    def on_close(self) -> None:
        self.animation_engine.shutdown()


if __name__ == '__main__':
    AnimationEngineTestingWindow.run()
