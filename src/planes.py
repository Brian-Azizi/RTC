from src.shape import Shape
from src.tuple import vector


class Plane(Shape):
    """The xz plane defined by y=0"""

    def local_intersect(self, ray):
        return super().local_intersect(ray)

    def local_normal_at(self, point):
        return vector(0, 1, 0)
