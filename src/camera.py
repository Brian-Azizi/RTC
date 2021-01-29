import math
from src.matrix import Matrix, identity


class Camera:
    hsize: float
    vsize: float
    field_of_view: float
    transform: Matrix
    pixel_size: float

    def __init__(
        self,
        hsize: float,
        vsize: float,
        field_of_view: float,
        transform: Matrix = identity(4),
    ) -> None:
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = transform

        self.pixel_size = self.calculate_pixel_size()

    def calculate_pixel_size(self) -> float:
        half_view = math.tan(self.field_of_view / 2)
        aspect = self.hsize / self.vsize

        if aspect >= 1:
            half_width = half_view
            half_height = half_view / aspect
        else:
            half_height = half_view
            half_width = half_view * aspect

        return (half_width * 2) / self.hsize