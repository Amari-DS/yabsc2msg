from app.models import Linear, Point
from app.transitions.base import PointGeneratorFactory, BasePointGenerator


@PointGeneratorFactory.register(Linear)
class LinearPointGenerator(BasePointGenerator[Linear]):

    def __init__(self, start: Point, end: Point, interpolation: Linear):
        super().__init__(start, end, interpolation)

    def _generate_point(self, t: float) -> Point:
        x = self._start.x + t * (self._end.x - self._start.x)
        y = self._start.y + t * (self._end.y - self._start.y)
        z = self._start.z + t * (self._end.z - self._start.z)
        return Point(x=round(x, 5), y=round(y, 5), z=round(z, 5))
