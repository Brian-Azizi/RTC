import math
from dataclasses import dataclass
from typing import List
from src.tuple import point, Point, dot, normalize, Vector, vector
from src.rays import Ray, transform
from src.intersection import Intersection, intersections, Intersections
from src.matrix import identity, Matrix, inverse, transpose
from src.materials import Material
from src.shape import Shape


@dataclass
class Sphere(Shape):
    """Unit Sphere"""

    origin: Point
    radius: float
    transform: Matrix
    material: Material

    def __init__(self) -> None:
        self.origin = point(0, 0, 0)
        self.radius = 1.0
        self.transform = identity(4)
        self.material = Material()

    def set_transform(self, transform: Matrix) -> None:
        self.transform = transform

    def intersect(self, ray: Ray) -> Intersections:
        world_to_object_transform = inverse(self.transform)
        transformed_ray = transform(ray, world_to_object_transform)

        sphere_to_ray = transformed_ray.origin - self.origin

        a = dot(transformed_ray.direction, transformed_ray.direction)
        b = 2 * dot(transformed_ray.direction, sphere_to_ray)
        c = dot(sphere_to_ray, sphere_to_ray) - 1

        discriminant = b * b - 4 * a * c

        if discriminant < 0:
            return []

        return intersections(
            Intersection((-b - math.sqrt(discriminant)) / (2 * a), self),
            Intersection((-b + math.sqrt(discriminant)) / (2 * a), self),
        )

    def normal_at(self, world_point: Point) -> Vector:
        transformer = inverse(self.transform)
        object_point = transformer * world_point
        object_normal = object_point - point(0, 0, 0)
        world_normal = transpose(transformer) * object_normal
        world_normal = vector(
            world_normal.x, world_normal.y, world_normal.z
        )  # set w to 0
        return normalize(world_normal)
