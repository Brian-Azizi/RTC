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

    def __mul__(self, other):
        return Tuple(
            self.x * other,
            self.y * other,
            self.z * other,
            self.w * other,
        )

    def __truediv__(self, other):
        return self * (1 / other)

    def approximately_equals(self, other):
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


def magnitude(p: Tuple):
    return math.sqrt(p.x * p.x + p.y * p.y + p.z * p.z)


def normalize(p: Tuple):
    return p / magnitude(p)


## Helper Functions
def approximately_equals(x, y):
    EPSILON = 0.00001
    return abs(x - y) < EPSILON