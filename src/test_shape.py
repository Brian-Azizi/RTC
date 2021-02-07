from src.shape import Shape, Intersections
from src.rays import Ray
from src.tuple import Point, Vector


class TestShape(Shape):
    def intersect(self, ray: Ray) -> Intersections:
        return super().intersect(ray)

    def normal_at(self, world_point: Point) -> Vector:
        return super().normal_at(world_point)
