import math
from src.matrix import Matrix, identity, inverse
from src.tuple import point, normalize
from src.rays import Ray
from src.world import World, color_at
from src.canvas import Canvas


class Camera:
    """
    Camera
    Looking at a canvas in the -z direction, 1 pixel away from itself
    """

    hsize: int
    vsize: int
    field_of_view: float
    transform: Matrix
    pixel_size: float

    def __init__(
        self,
        hsize: int,
        vsize: int,
        field_of_view: float,
        transform: Matrix = identity(4),
    ) -> None:
        self.hsize = hsize
        self.vsize = vsize
        self.field_of_view = field_of_view
        self.transform = transform

        self.calculate_pixel_size()

    def calculate_pixel_size(self) -> None:
        half_view = math.tan(self.field_of_view / 2)
        aspect = self.hsize / self.vsize

        if aspect >= 1:
            half_width = half_view
            half_height = half_view / aspect
        else:
            half_height = half_view
            half_width = half_view * aspect

        self.pixel_size = (half_width * 2) / self.hsize
        self.half_width = half_width
        self.half_height = half_height

    def ray_for_pixel(self, canvas_x: float, canvas_y: float) -> Ray:
        # offset from edge of canvas to the pixel's center
        x_offset = (canvas_x + 0.5) * self.pixel_size
        y_offset = (canvas_y + 0.5) * self.pixel_size

        # pixel coordinate in camera space
        x = self.half_width - x_offset
        y = self.half_height - y_offset
        z = -1  # camera is looking at -z by default

        # transform to world coordinates
        transformer = inverse(self.transform)
        pixel = transformer * point(x, y, z)
        origin = transformer * point(0, 0, 0)
        direction = normalize(pixel - origin)

        return Ray(origin, direction)

    def render(self, world: World) -> Canvas:
        image = Canvas(self.hsize, self.vsize)

        for x in range(image.width):
            for y in range(image.height):
                ray = self.ray_for_pixel(x, y)
                color = color_at(world, ray)
                image.write_pixel(x, y, color)

        return image
