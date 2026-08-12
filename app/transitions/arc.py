import math

from app.models import Arc, Point
from app.transitions.base import PointGeneratorFactory, BasePointGenerator


@PointGeneratorFactory.register(Arc)
class ArcPointGenerator(BasePointGenerator[Arc]):

    def __init__(self, start: Point, end: Point, interpolation: Arc):
        super().__init__(start, end, interpolation)
        self.__set_up()

    def __set_up(self):
        center_point = self._interpolation.center
        self.__cx, self.__cy, self.__cz = center_point.x, center_point.y, center_point.z

        # Gemini: 1. Векторы относительно 3D центра
        v0 = [
            self._start.x - self.__cx,
            self._start.y - self.__cy,
            self._start.z - self.__cz
        ]
        v1 = [
            self._end.x - self.__cx,
            self._end.y - self.__cy,
            self._end.z - self.__cz
        ]

        # Gemini: 2. Трехмерные радиусы
        self.__r0 = math.sqrt(v0[0] ** 2 + v0[1] ** 2 + v0[2] ** 2)
        self.__r1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2 + v1[2] ** 2)

        # Gemini: 3. Единичные направления (направление дуги в 3D)
        self.__u0 = [v0[0] / self.__r0, v0[1] / self.__r0, v0[2] / self.__r0] if self.__r0 > 0 else [0, 0, 0]
        self.__u1 = [v1[0] / self.__r1, v1[1] / self.__r1, v1[2] / self.__r1] if self.__r1 > 0 else [0, 0, 0]

    def _generate_point(self, t: float) -> Point:
        # Gemini: Интерполяция 3D радиуса
        r_t = self.__r0 + t * (self.__r1 - self.__r0)

        # Gemini: Интерполяция 3D направления по сфере
        u_t = self.__slerp_3d(self.__u0, self.__u1, t)

        # Gemini: Результирующие координаты X, Y, Z
        x = self.__cx + r_t * u_t[0]
        y = self.__cy + r_t * u_t[1]
        z = self.__cz + r_t * u_t[2]

        return Point(x=round(x, 5), y=round(y, 5), z=round(z, 5))

    @staticmethod
    def __slerp_3d(u0, u1, t):
        """ Spherical linear interpolation """
        dot = u0[0] * u1[0] + u0[1] * u1[1] + u0[2] * u1[2]
        # Gemini: Защита от погрешностей float для acos
        dot = max(-1.0, min(1.0, dot))

        omega = math.acos(dot)
        sin_omega = math.sin(omega)

        # Gemini: Если векторы практически совпадают или противоположны
        if sin_omega < 1e-6:
            return [
                u0[0] + t * (u1[0] - u0[0]),
                u0[1] + t * (u1[1] - u0[1]),
                u0[2] + t * (u1[2] - u0[2])
            ]

        w0 = math.sin((1.0 - t) * omega) / sin_omega
        w1 = math.sin(t * omega) / sin_omega

        return [
            w0 * u0[0] + w1 * u1[0],
            w0 * u0[1] + w1 * u1[1],
            w0 * u0[2] + w1 * u1[2]
        ]
