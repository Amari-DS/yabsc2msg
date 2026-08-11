from abc import ABC, abstractmethod
from typing import Type, TypeVar, Generic

from app.models import Transition, Point

T = TypeVar("T", bound=Transition)


class BasePointGenerator(ABC, Generic[T]):

    def __init__(self, start: Point, end: Point, transition: T):
        self._start = start
        self._end = end
        self._transition = transition

    @abstractmethod
    def generate(self, t: float) -> Point:
        raise NotImplementedError()


class PointGeneratorFactory:
    _registry: dict[Type[Transition], Type[BasePointGenerator]] = {}

    @classmethod
    def register(cls, transition_cls: Type[Transition]):
        def decorator(generator_cls: Type[BasePointGenerator]):
            cls._registry[transition_cls] = generator_cls
            return generator_cls

        return decorator

    @classmethod
    def create(cls, start: Point, end: Point, transition: Transition ) -> BasePointGenerator:
        generator_cls = cls._registry.get(type(transition))
        if not generator_cls:
            raise ValueError(f'No generator for transition_type={type(transition)}')
        return generator_cls(start, end, transition)
