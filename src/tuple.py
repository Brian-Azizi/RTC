from dataclasses import dataclass


@dataclass(frozen=True)
class Tuple:
    x: float
    y: float
    z: float
    w: float


def Point(x: float, y: float, z: float):
    return Tuple(x, y, z, 1.0)


def Vector(x: float, y: float, z: float):
    return Tuple(x, y, z, 0.0)
