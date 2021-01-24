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


def Point(x: float, y: float, z: float):
    return Tuple(x, y, z, 1.0)


def Vector(x: float, y: float, z: float):
    return Tuple(x, y, z, 0.0)
