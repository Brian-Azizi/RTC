from __future__ import annotations
from abc import ABC, abstractmethod
from src.materials import Material
from src.matrix import Matrix
from src.rays import Ray
from src.tuple import Point, Vector
from typing import List, Optional
from typing import List, Optional
from src.rays import Ray
from src.tuple import Point, Vector


class Shape(ABC):
    transform: Matrix
    material: Material

    @abstractmethod
    def intersect(self, ray: Ray) -> Intersections:
        pass

    @abstractmethod
    def normal_at(self, world_point: Point) -> Vector:
        pass


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
