from unit_animation_engine import math
from unit_animation_engine.math import radians, RadiansPerFrame


def move_toward_target_position(
    current_position: float, target_position: float, speed: float,
    delta_time_ms: int
) -> tuple[float, bool]:
    """
    Updates move animations
    :param current_position: position to update
    :param target_position: target position
    :param speed: change in position per second
    :param delta_time_ms: time since last tick (usually a fixed rate)
    :return: new position, True if destination was reached
    """

    # Calculate tick rate and per-tick speed
    tick_rate = math.milliseconds_to_tick_rate(delta_time_ms)
    speed_per_tick = speed / tick_rate

    # Calculate the distance to the target position
    delta_position = target_position - current_position

    # Check if the target is within reach
    if math.abs(delta_position) < speed_per_tick:
        return target_position, True

    # Update the current position
    return current_position + (speed_per_tick * math.sign(delta_position)), False


def turn_toward_target_position(
    current_angle: radians, target_angle: radians, speed: radians,
    delta_time_ms: int
) -> tuple[radians, bool]:
    """
    Updates turn animations
    :param current_angle: current angle
    :param target_angle: target angle
    :param speed: change in value per second
    :param delta_time_ms: time since last tick (usually a fixed rate)
    :return new rotation, True if destination was reached
    """
    # Normalize angles to ensure they are within [0, 2π)
    current_angle = math.clamp_rad(current_angle)
    target_angle = math.clamp_rad(target_angle)

    # Calculate tick rate and per-tick speed
    tick_rate = math.milliseconds_to_tick_rate(delta_time_ms)
    speed_per_tick = speed / tick_rate

    # Calculate the shortest path to the target angle
    delta = math.mod(target_angle - current_angle + math.THREE_PI, math.TWO_PI) - math.PI

    # Check if the target is within reach
    if math.abs(delta) < speed_per_tick:
        return target_angle, True

    # Update the current angle and normalize it
    return math.clamp_rad(current_angle + (speed_per_tick * math.sign(delta))), False


def spin_towards_target_speed(
    current_angle: radians, target_speed: radians, current_speed: radians, accel: RadiansPerFrame,
    delta_time_ms: int
) -> tuple[radians, radians, bool]:
    """
    Updates spin animations
    :param current_angle: current angle
    :param target_speed: the final desired speed (NOT the final angle!)
    :param current_speed: value change per second
    :param accel: change in speed per second
    :param delta_time_ms: time since last tick (usually a fixed rate)
    :return: new rotation angle, new speed, True if target speed was reached AND it was zero (animation finished)
    """
    # Normalize the current angle to ensure it is within [0, 2π)
    current_angle = math.clamp_rad(current_angle)

    # Calculate tick rate and per-tick values
    tick_rate = math.milliseconds_to_tick_rate(delta_time_ms)
    target_speed_per_tick = target_speed / tick_rate
    speed_per_tick = current_speed / tick_rate
    accel_per_tick = accel / tick_rate

    # Update speed towards the target speed
    delta_speed = target_speed_per_tick - speed_per_tick
    if math.abs(delta_speed) <= accel_per_tick:
        current_speed = target_speed
        speed_per_tick = target_speed_per_tick
    else:
        current_speed += accel_per_tick * math.sign(delta_speed)
        speed_per_tick = current_speed / tick_rate

    # Update angle based on the new speed
    current_angle = math.clamp_rad(current_angle + speed_per_tick)

    # Check if the target speed is reached and is zero
    # (the animation is finished ONLY if the spinning has completely stopped)
    animation_finished = (current_speed == 0 and target_speed == 0)
    return current_angle, current_speed, animation_finished
