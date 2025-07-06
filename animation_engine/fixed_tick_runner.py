from __future__ import annotations

from collections.abc import Callable
from typing import NamedTuple

class FixedUpdateTicker:
    """
    A class that manages fixed-rate update ticks for animations and/or game logic.
    It ensures updates occur at a consistent rate regardless of actual elapsed time.
    """

    class TickInfo(NamedTuple):
        """A named tuple containing information about a single tick.

        Attributes
        ----------
            fixed_tick_count : int
                The number of fixed ticks that have occurred.
            fixed_tick_rate : int
                The rate at which fixed ticks occur (ticks per second).
            fixed_delta_time_ms : int
                The time duration of a single fixed tick in milliseconds. (``1000 // fixed_tick_rate``)
            fixed_time_elapsed : float
                The total fixed time elapsed in seconds.
            actual_time_elapsed : float
                The total actual time elapsed in seconds. Fixed updates are run until they catch up to this value.

                (More precisely, what it was at the start of doing fixed updates)

        Usage Note
        ----------
            | Instead of a multiplying by a fractional ``delta_time`` parameter, divide values that need to be scaled by the ``fixed_tick_rate``.
            | This cuts out an unnecessary division and may help avoid floating point errors and/or help with determinism.
            |
            | Target TPS of 30
            | ``fixed_tick_rate = 30``
            |
            | Value to be scaled into "per tick"
            | ``speed_per_second = 50``
            |
            | Typical method seen in other game engines.
            | (Has to be used in update loops with variable delta_time between updates)
            | ``delta_time = 1 / fixed_tick_rate # 0.33...``
            | ``speed_per_tick = speed_per_second * delta_time``
            | Result = 1.666...
            |
            | Suggested method
            | (able to be used in fixed update loops)
            | ``speed_per_tick = speed_per_second / fixed_tick_rate``
            | Result = 1.666...
            |
            | As this is a fixed update loop, use the suggested method.
        """
        fixed_tick_count: int
        fixed_tick_rate: int
        fixed_delta_time_ms: int

        fixed_time_elapsed: float
        actual_time_elapsed: float

        def __str__(self):
            """
            Returns a string representation of the TickInfo object.
            """
            return (
                f"TickInfo(fixed_tick_count={self.fixed_tick_count}, "
                f"fixed_tick_rate={self.fixed_tick_rate}, "
                f"fixed_delta_time_ms={self.fixed_delta_time_ms}, "
                f"fixed_time_elapsed={self.fixed_time_elapsed:.2f}, "
                f"actual_time_elapsed={self.actual_time_elapsed:.2f})"
            )

    fixed_update_function: Callable[[TickInfo], None]
    """
    A callable function that is executed on each fixed tick.
    It receives a TickInfo object as its argument.
    """

    fixed_tick_count = 0
    """
    The number of fixed ticks that have occurred.
    """

    fixed_tick_rate = 30
    """
    The rate at which fixed ticks occur (ticks per second).
    """

    actual_time_elapsed: float = 0
    """
    The total actual time elapsed in seconds.
    """

    def __init__(self, fixed_update_function: Callable[[TickInfo], None], fixed_tick_rate: int = 30):
        """
        Initializes the FixedUpdateTicker.

        Args:
            fixed_update_function (Callable[[TickInfo], None]): The function to call on each fixed tick.
            fixed_tick_rate (int, optional): The rate at which fixed ticks occur (ticks per second). Defaults to 30.
        """
        self.fixed_update_function = fixed_update_function

        self.fixed_tick_count = 0
        self.fixed_tick_rate = fixed_tick_rate

        self.actual_time_elapsed = 0

    def fixed_time_elapsed(self) -> float:
        """
        Calculates the total fixed time elapsed in seconds.

        Returns:
            float: The total fixed time elapsed.
        """
        return self.fixed_tick_count * (1 / self.fixed_tick_rate)

    def update(self, actual_delta_time: float):
        """
        Updates the ticker with the actual time elapsed since the last update.
        Executes fixed update ticks as needed based on the elapsed time.

        Args:
            actual_delta_time (float): The actual time elapsed since the last update in seconds.
        """
        self.actual_time_elapsed += actual_delta_time

        while self.actual_time_elapsed >= self.fixed_time_elapsed():
            tick_info = FixedUpdateTicker.TickInfo(
                fixed_tick_count=self.fixed_tick_count,
                fixed_tick_rate=self.fixed_tick_rate,
                fixed_delta_time_ms=1000 // self.fixed_tick_rate,
                fixed_time_elapsed=self.fixed_time_elapsed(),
                actual_time_elapsed=self.actual_time_elapsed
            )

            self.fixed_tick_count += 1

            if self.fixed_update_function:
                self.fixed_update_function(tick_info)
