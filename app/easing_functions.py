import math


def linear(t_linear: float) -> float:
    return t_linear


def ease_in(t_linear: float) -> float:
    return t_linear * t_linear


def ease_out(t_linear: float) -> float:
    return t_linear * (2.0 - t_linear)


def smooth_step(t_linear: float) -> float:
    return t_linear * t_linear * (3.0 - 2.0 * t_linear)


def smoother_step(t_linear: float) -> float:
    return t_linear ** 3 * (t_linear * (t_linear * 6 - 15) + 10)


def cos_ipol(t_linear: float) -> float:
    return (1 - math.cos(t_linear * math.pi)) / 2
