from unit_animation_engine import math
from unit_animation_engine.math import (
    milliseconds,
    float_per_second,
    radians,
    radians_per_second,
    radians_per_second_per_second,
)


def move_toward_target_position(
    current_position: float,
    target_position: float,
    speed: float_per_second,
    delta_time_ms: milliseconds
) -> tuple[float, bool]:
    """
    Updates move animations
    :param current_position: position to update
    :param target_position: target position
    :param speed: change in position per second
    :param delta_time_ms: time since last tick (usually a fixed rate)
    :return: new position, True if destination was reached
    """
    speed = math.abs(speed)

    tick_rate = math.milliseconds_to_tick_rate(delta_time_ms)
    speed_per_tick = speed / tick_rate

    # Calculate the distance to the target position
    delta_position = target_position - current_position

    # If the target would be overshot, snap to target
    if math.abs(delta_position) < speed_per_tick:
        return target_position, True

    # Return updated position
    return current_position + (speed_per_tick * math.sign(delta_position)), False


def turn_toward_target_position(
    current_angle: radians,
    target_angle: radians,
    speed: radians_per_second,
    delta_time_ms: milliseconds
) -> tuple[radians, bool]:
    """
    Updates turn animations
    :param current_angle: current angle
    :param target_angle: target angle
    :param speed: change in value per second
    :param delta_time_ms: time since last tick (usually a fixed rate)
    :return new rotation, True if destination was reached
    """
    current_angle = math.clamp_rad(current_angle)
    target_angle = math.clamp_rad(target_angle)
    speed = math.abs(speed)

    tick_rate = math.milliseconds_to_tick_rate(delta_time_ms)

    # Visualization:
    #   Isaac (https://math.stackexchange.com/users/72/isaac),
    #   Shortest way to achieve target angle,
    #   URL (version: 2012-02-17): https://math.stackexchange.com/q/110236
    delta = math.mod(target_angle - current_angle + math.THREE_PI, math.TWO_PI) - math.PI

    speed_per_tick = speed / tick_rate

    # If the target would be overshot, snap to target
    if math.abs(delta) < speed_per_tick:
        return target_angle, True

    # Return updated angle
    return math.clamp_rad(current_angle + (speed_per_tick * math.sign(delta))), False


def spin_towards_target_speed(
    current_angle: radians,
    target_speed: radians_per_second,
    current_speed: radians_per_second,
    accel: radians_per_second_per_second,
    delta_time_ms: milliseconds
) -> tuple[radians, radians_per_second, bool]:
    """
    Updates spin animations
    :param current_angle: current angle
    :param target_speed: the final desired speed (NOT the final angle!)
    :param current_speed: value change per second
    :param accel: change in speed per second
    :param delta_time_ms: time since last tick (usually a fixed rate)
    :return: new rotation angle, new speed, True if target speed was reached AND it was zero (animation finished)
    """
    current_angle = math.clamp_rad(current_angle)
    accel = math.abs(accel)

    tick_rate = math.milliseconds_to_tick_rate(delta_time_ms)

    target_speed_per_tick = target_speed / tick_rate
    speed_per_tick = current_speed / tick_rate
    accel_per_tick = accel / tick_rate

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
    return new_angle, new_speed, animation_finished
