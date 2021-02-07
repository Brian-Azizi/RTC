from src.shape import Shape, Intersections
from src.rays import Ray
from src.tuple import Point, Vector


class TestShape(Shape):
    local_ray: Ray

    def local_intersect(self, ray: Ray) -> Intersections:
        self.local_ray = ray
        return super().local_intersect(ray)

    def normal_at(self, world_point: Point) -> Vector:
        return super().normal_at(world_point)
