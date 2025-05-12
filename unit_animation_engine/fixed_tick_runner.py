from __future__ import annotations

from collections.abc import Callable
from typing import NamedTuple

from unit_animation_engine.math import milliseconds


class FixedTickRunner:

    class TickInfo(NamedTuple):
        fixed_tick_count: int
        fixed_tick_rate: int
        fixed_delta_time_ms: milliseconds

        fixed_time_elapsed: float
        actual_time_elapsed: float

    fixed_update_function: Callable[[TickInfo], None]

    fixed_tick_count = 0
    fixed_tick_rate = 30

    actual_time_elapsed: float = 0

    def __init__(self, fixed_update_function: Callable[[TickInfo], None], fixed_tick_rate: int = 30):
        self.fixed_update_function = fixed_update_function

        self.fixed_tick_count = 0
        self.fixed_tick_rate = fixed_tick_rate

        self.actual_time_elapsed = 0

    def fixed_time_elapsed(self) -> float:
        return self.fixed_tick_count * (1 / self.fixed_tick_rate)

    def update(self, actual_delta_time: float):
        self.actual_time_elapsed += actual_delta_time

        while self.actual_time_elapsed >= self.fixed_time_elapsed():
            tick_info = FixedTickRunner.TickInfo(
                fixed_tick_count=self.fixed_tick_count,
                fixed_tick_rate=self.fixed_tick_rate,
                fixed_delta_time_ms=1000 // self.fixed_tick_rate,
                fixed_time_elapsed=self.fixed_time_elapsed(),
                actual_time_elapsed=self.actual_time_elapsed
            )

            self.fixed_tick_count += 1

            if self.fixed_update_function:
                self.fixed_update_function(tick_info)
