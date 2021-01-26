import math
from typing import List
from src.tuple import point, Point, dot
from src.rays import Ray
from src.intersection import Intersection, intersections, Intersections, Object
from src.matrix import identity, Matrix


class Sphere(Object):
    origin: Point
    radius: float
    transform: Matrix

    def __init__(self, origin: Point, radius: float, transform: Matrix = identity(4)):
        self.origin = origin
        self.radius = radius
        self.transform = transform

    def set_transform(self, transform: Matrix) -> None:
        self.transform = transform


def sphere() -> Sphere:
    origin = point(0, 0, 0)
    radius = 1
    return Sphere(origin, radius)


def intersect(s: Sphere, ray: Ray) -> Intersections:
    sphere_to_ray = ray.origin - s.origin

    a = dot(ray.direction, ray.direction)
    b = 2 * dot(ray.direction, sphere_to_ray)
    c = dot(sphere_to_ray, sphere_to_ray) - 1

    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        return []
    return intersections(
        Intersection((-b - math.sqrt(discriminant)) / (2 * a), s),
        Intersection((-b + math.sqrt(discriminant)) / (2 * a), s),
    )
