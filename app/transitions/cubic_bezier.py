from app.models import CubicBezier, Point
from app.transitions.base import PointGeneratorFactory, BasePointGenerator


@PointGeneratorFactory.register(CubicBezier)
class CubicBezierPointGenerator(BasePointGenerator[CubicBezier]):

    def __init__(self, start: Point, end: Point, interpolation: CubicBezier):
        super().__init__(start, end, interpolation)
        self.__set_up(start, end, interpolation)

    def __set_up(self, start: Point, end: Point, transition: CubicBezier):
        self.p0 = start
        self.p1 = Point(
            x=start.x + transition.handle_start.x,
            y=start.y + transition.handle_start.y,
            z=start.z + transition.handle_start.z,
        )
        self.p2 = Point(
            x=end.x + transition.handle_end.x,
            y=end.y + transition.handle_end.y,
            z=end.z + transition.handle_end.z,
        )
        self.p3 = end

    def _generate_point(self, t: float) -> Point:
        u = 1.0 - t
        uu = u * u
        uuu = uu * u

        tt = t * t
        ttt = tt * t

        w0 = uuu
        w1 = 3 * uu * t
        w2 = 3 * u * tt
        w3 = ttt

        x = w0 * self.p0.x + w1 * self.p1.x + w2 * self.p2.x + w3 * self.p3.x
        y = w0 * self.p0.y + w1 * self.p1.y + w2 * self.p2.y + w3 * self.p3.y
        z = w0 * self.p0.z + w1 * self.p1.z + w2 * self.p2.z + w3 * self.p3.z

        return Point(
            x=round(x, 5),
            y=round(y, 5),
            z=round(z, 5),
        )
