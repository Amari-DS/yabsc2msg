from abc import ABC, abstractmethod
from typing import Type, TypeVar, Generic

from app.models import Point, BaseInterpolation

T = TypeVar('T', bound=BaseInterpolation)


class BasePointGenerator(ABC, Generic[T]):

    def __init__(self, start: Point, end: Point, interpolation: T):
        self._start = start
        self._end = end
        self._interpolation = interpolation

    def generate(self, t_linear: float) -> Point:
        t = self._interpolation.smooth(t_linear)
        return self._generate_point(t)

    @abstractmethod
    def _generate_point(self, t: float) -> Point:
        raise NotImplementedError()


class PointGeneratorFactory:
    _registry: dict[Type[BaseInterpolation], Type[BasePointGenerator]] = {}

    @classmethod
    def register(cls, interpolation_cls: Type[BaseInterpolation]):
        def decorator(generator_cls: Type[BasePointGenerator]):
            cls._registry[interpolation_cls] = generator_cls
            return generator_cls

        return decorator

    @classmethod
    def create(cls, start: Point, end: Point, interpolation: BaseInterpolation) -> BasePointGenerator:
        generator_cls = cls._registry.get(type(interpolation))
        if not generator_cls:
            raise ValueError(f'No generator for interpolation_type={type(interpolation)}')
        return generator_cls(start, end, interpolation)
