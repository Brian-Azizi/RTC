from __future__ import annotations
from abc import ABC, abstractmethod
from src.materials import Material
from src.matrix import Matrix, identity
from src.rays import Ray
from src.tuple import Point, Vector
from typing import List, Optional
from typing import List, Optional
from src.rays import Ray
from src.tuple import Point, Vector, vector, normalize
from src.matrix import inverse, transpose


class Shape(ABC):
    transform: Matrix
    material: Material

    def __init__(self) -> None:
        self.transform = identity(4)
        self.material = Material()

    def set_transform(self, transform: Matrix) -> None:
        self.transform = transform

    def intersect(self, ray: Ray) -> Intersections:
        world_to_object_transform = inverse(self.transform)
        local_ray = ray.transform(world_to_object_transform)
        return self.local_intersect(local_ray)

    def normal_at(self, world_point: Point) -> Vector:
        transformer = inverse(self.transform)
        local_point = transformer * world_point
        local_normal = self.local_normal_at(local_point)
        world_normal = transpose(transformer) * local_normal
        world_normal = vector(
            world_normal.x, world_normal.y, world_normal.z
        )  # set w to 0
        return normalize(world_normal)

    @abstractmethod
    def local_intersect(self, ray: Ray) -> Intersections:
        pass

    @abstractmethod
    def local_normal_at(self, point: Point) -> Vector:
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
