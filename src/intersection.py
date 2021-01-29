from __future__ import annotations
from dataclasses import dataclass
from typing import List, Iterable, Optional
from src.matrix import Matrix
from src.rays import Ray, position
from src.materials import Material
from src.tuple import Point, Vector, dot


class Object:
    transform: Matrix
    material: Material


class Intersection:
    t: float
    the_object: Object

    def __init__(self, t: float, the_object: Object):
        self.t = t
        self.the_object = the_object

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
    the_object: Object
    point: Point
    eye_vector: Vector
    normal_vector: Vector
    inside: bool

    def __init__(self, intersection: Intersection, ray: Ray):
        from src.spheres import normal_at

        self.t = intersection.t
        self.the_object = intersection.the_object
        self.point = position(ray, self.t)
        self.eye_vector = -ray.direction
        self.normal_vector = normal_at(self.the_object, self.point)

        if dot(self.normal_vector, self.eye_vector) < 0:
            self.inside = True
            self.normal_vector = -self.normal_vector
        else:
            self.inside = False
