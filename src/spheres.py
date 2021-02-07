import math
from dataclasses import dataclass
from src.tuple import point, Point, dot, normalize, Vector, vector
from src.rays import Ray, transform
from src.matrix import Matrix, inverse, transpose
from src.materials import Material
from src.shape import Shape, Intersection, intersections, Intersections


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
        return super().__init__()

    def local_intersect(self, ray: Ray) -> Intersections:
        sphere_to_ray = ray.origin - self.origin

        a = dot(ray.direction, ray.direction)
        b = 2 * dot(ray.direction, sphere_to_ray)
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
