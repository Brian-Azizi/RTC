import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Tuple:
    x: float
    y: float
    z: float
    w: float

    def __add__(self, other):
        return Tuple(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
            self.w + other.w,
        )

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __neg__(self):
        return Tuple(-self.x, -self.y, -self.z, -self.w)

    def __sub__(self, other):
        return self + -other

    def __mul__(self, other: float):
        return Tuple(
            self.x * other,
            self.y * other,
            self.z * other,
            self.w * other,
        )

    def __truediv__(self, other: float):
        return self * (1 / other)

    def approximately_equals(self, other) -> bool:
        return (
            approximately_equals(self.x, other.x)
            and approximately_equals(self.y, other.y)
            and approximately_equals(self.z, other.z)
            and approximately_equals(self.w, other.w)
        )


def Point(x: float, y: float, z: float):
    return Tuple(x, y, z, 1.0)


def Vector(x: float, y: float, z: float):
    return Tuple(x, y, z, 0.0)


def magnitude(p) -> float:
    return math.sqrt(p.x * p.x + p.y * p.y + p.z * p.z)


def normalize(p) -> Tuple:
    return p / magnitude(p)


def dot(a, b) -> float:
    return a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w


def cross(a, b):
    return Vector(
        a.y * b.z - a.z * b.y,
        a.z * b.x - a.x * b.z,
        a.x * b.y - a.y * b.x,
    )


## Helper Functions
def approximately_equals(x: float, y: float):
    EPSILON = 0.00001
    return abs(x - y) < EPSILON