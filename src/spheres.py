import math
from src.tuple import point, Point, dot
from src.rays import Ray
from typing import List


class Sphere:
    origin: Point
    radius: float

    def __init__(self, origin: Point, radius: float):
        self.origin = origin
        self.radius = radius


def sphere() -> Sphere:
    origin = point(0, 0, 0)
    radius = 1
    return Sphere(origin, radius)


def intersect(s: Sphere, ray: Ray) -> List[float]:
    sphere_to_ray = ray.origin - s.origin

    a = dot(ray.direction, ray.direction)
    b = 2 * dot(ray.direction, sphere_to_ray)
    c = dot(sphere_to_ray, sphere_to_ray) - 1

    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        return []
    return [
        (-b - math.sqrt(discriminant)) / (2 * a),
        (-b + math.sqrt(discriminant)) / (2 * a),
    ]
