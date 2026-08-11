from enum import Enum
from typing import Callable


class EasingEnum(str, Enum):

    def __new__(cls, name: str, easing_func: Callable[[float], float]):
        obj = str.__new__(cls)
        obj._value_ = name
        obj._easing_func = easing_func
        return obj

    def __call__(self, t: float) -> float:
        return self._easing_func(t)
