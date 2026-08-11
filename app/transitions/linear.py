from app.models import LinearTransition, Point
from app.transitions.common import PointGeneratorFactory, BasePointGenerator


@PointGeneratorFactory.register(LinearTransition)
class LinearPointGenerator(BasePointGenerator[LinearTransition]):

    def __init__(self, start: Point, end: Point, transition: LinearTransition = None):
        super().__init__(start, end, transition)

    def generate(self, t: float) -> Point:
        x = self._start.x + t * (self._end.x - self._start.x)
        y = self._start.y + t * (self._end.y - self._start.y)
        z = self._start.z + t * (self._end.z - self._start.z)
        return Point(x=round(x, 5), y=round(y, 5), z=round(z, 5))
