from __future__ import annotations
from dataclasses import dataclass
from typing import List, Iterable, Optional
from src.matrix import Matrix
from src.rays import Ray, position
from src.tuple import Point, Vector, dot
from src.helpers import LONG_EPSILON
from src.shape import Shape


class Intersection:
    t: float
    shape: Shape

    def __init__(self, t: float, shape: Shape):
        self.t = t
        self.shape = shape

    def __lt__(self, other: Intersection) -> bool:
        return self.t < other.t


Intersections = List[Intersection]


def intersections(*args: Intersection) -> Intersections:
    result = list(args)
    result.sort()
    return result


def find_hit(xs: Intersections) -> Optional[Intersection]:
    for intersection in xs:
        if intersection.t >= 0:
            return intersection

    return None


@dataclass
class PreparedComputation:
    t: float
    shape: Shape
    point: Point
    eye_vector: Vector
    normal_vector: Vector
    inside: bool
    over_point: Point

    def __init__(self, intersection: Intersection, ray: Ray):
        self.t = intersection.t
        self.shape = intersection.shape
        self.point = position(ray, self.t)
        self.eye_vector = -ray.direction
        self.normal_vector = self.shape.normal_at(self.point)

        if dot(self.normal_vector, self.eye_vector) < 0:
            self.inside = True
            self.normal_vector = -self.normal_vector
        else:
            self.inside = False

        self.over_point = self.point + self.normal_vector * LONG_EPSILON
