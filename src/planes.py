from src.shape import Shape, Intersection, Intersections
from src.tuple import vector, Point, Vector
from src.rays import Ray
from src.helpers import LONG_EPSILON


class Plane(Shape):
    """The xz plane defined by y=0"""

    def local_intersect(self, ray: Ray) -> Intersections:
        if abs(ray.direction.y) < LONG_EPSILON:
            return []

        t = -ray.origin.y / ray.direction.y
        return [Intersection(t, self)]

    def local_normal_at(self, point: Point) -> Vector:
        return vector(0, 1, 0)
