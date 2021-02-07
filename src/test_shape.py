from src.shape import Shape, Intersections
from src.rays import Ray
from src.tuple import Point, Vector, vector


class TestShape(Shape):
    local_ray: Ray

    def local_intersect(self, ray: Ray) -> Intersections:
        self.local_ray = ray
        return super().local_intersect(ray)

    def local_normal_at(self, p: Point) -> Vector:
        return vector(p.x, p.y, p.z)
