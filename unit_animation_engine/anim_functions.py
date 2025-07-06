from typing import NamedTuple, Protocol

from unit_animation_engine import math
from unit_animation_engine.math import (
    float_velocity,
    radians,
    radians_velocity,
    radians_accel, ticks_per_second,
)


class AnimResult(Protocol):
    """Protocol for animation results.

    Attributes:
        done (bool): True if the animation is complete, False if the animation needs to continue being updated.
    """
    done: bool


class MoveTowardResult(NamedTuple):
    """
    Result of moving toward a target position.

    Attributes:
        done (bool): True if the target position was reached.
        new_position (float): The updated position after the move.
    """
    done: bool
    new_position: float


def move_toward_target_position(
    current_position: float,
    target_position: float,
    speed: float_velocity,
    tick_rate: ticks_per_second
) -> MoveTowardResult:
    """
    Updates move animations
    :param current_position: position to update
    :param target_position: target position
    :param speed: change in position per second
    :param tick_rate: number of ticks per second
    :return MoveTowardResult: new position and whether the target was reached
    """
    speed = math.abs(speed)

    speed_per_tick = speed / tick_rate

    # Calculate the distance to the target position
    delta_position = target_position - current_position

    # If target would be overshot, snap to target
    if math.abs(delta_position) < speed_per_tick:
        return MoveTowardResult(True, target_position)

    # Return updated position
    return MoveTowardResult(False, current_position + (speed_per_tick * math.sign(delta_position)))


class TurnTowardResult(NamedTuple):
    """Result of turning toward a target angle.

    Attributes:
        done (bool): True if the target angle was reached.
        new_angle (radians): The updated angle after the turn.
    """
    done: bool
    new_angle: radians


def turn_toward_target_rotation(
    current_angle: radians,
    target_angle: radians,
    speed: radians_velocity,
    tick_rate: ticks_per_second
) -> TurnTowardResult:
    """
    Updates turn animations
    :param current_angle: current angle
    :param target_angle: target angle
    :param speed: change in value per second
    :param tick_rate: number of ticks per second
    :return TurnTowardResult: True if the animation is finished, new angle
    """
    current_angle = math.clamp_rad(current_angle)
    target_angle = math.clamp_rad(target_angle)
    speed = math.abs(speed)

    # Visualization:
    #   Isaac (https://math.stackexchange.com/users/72/isaac),
    #   Shortest way to achieve target angle,
    #   URL (version: 2012-02-17): https://math.stackexchange.com/q/110236
    delta = math.mod(target_angle - current_angle + math.THREE_PI, math.TWO_PI) - math.PI

    speed_per_tick = speed / tick_rate

    # If target would be overshot, snap to target
    if math.abs(delta) < speed_per_tick:
        return TurnTowardResult(True, target_angle)

    # Return updated angle
    return TurnTowardResult(False, math.clamp_rad(current_angle + (speed_per_tick * math.sign(delta))))


class SpinTowardResult(NamedTuple):
    """Result of spinning toward a target speed.

    Attributes:
        done (bool): True if the animation is finished (target speed 0, and it was reached).
        new_angle (radians): The updated angle after the spin.
        new_speed (radians_velocity): The updated speed after the spin.
    """
    done: bool
    new_angle: radians
    new_speed: radians_velocity


def spin_toward_target_velocity(
    current_angle: radians,
    current_speed: radians_velocity,
    target_speed: radians_velocity,
    accel: radians_accel,
    tick_rate: ticks_per_second
) -> SpinTowardResult:
    """
    Updates spin animations
    :param current_angle: current angle
    :param current_speed: value change per second
    :param target_speed: the final desired speed (NOT the final angle!)
    :param accel: change in speed per second
    :param tick_rate: number of ticks per second
    :return SpinTowardResult: True if the animation is finished, new angle, new speed
    """
    current_angle = math.clamp_rad(current_angle)
    accel = math.abs(accel)

    accel_per_tick = accel / tick_rate
    speed_per_tick = current_speed / tick_rate
    target_speed_per_tick = target_speed / tick_rate

    delta_speed_per_tick = target_speed_per_tick - speed_per_tick

    # If target would be overshot, snap to target
    if math.abs(delta_speed_per_tick) <= accel_per_tick:
        new_speed = target_speed
    else:
        new_speed = current_speed + (accel_per_tick * math.sign(delta_speed_per_tick))

    # recalculate speed_per_tick after update
    new_speed_per_tick = new_speed / tick_rate

    # Update angle based on the new speed
    new_angle = math.clamp_rad(current_angle + new_speed_per_tick)

    # Check if the target speed is reached and is zero
    # (the animation is finished ONLY if the spinning has completely stopped)
    animation_finished = (new_speed == 0 and target_speed == 0)
    return SpinTowardResult(animation_finished, new_angle, new_speed)
