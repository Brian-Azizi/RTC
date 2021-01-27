import math
from src.canvas import Canvas
from src.rays import Ray
from src.color import Color
from src.intersection import hit
from src.spheres import sphere, intersect
from src.tuple import point, Point, normalize
from src.ppm import PPM
from src.transformations import translation, shearing, scaling, rotation_z


# Canvas size
CANVAS_SIZE = 100

# Wall is normal to z-axis
WALL_Z = -10

# Wall Size
WALL_SIZE = 10


def canvas_to_world(canvas_coordinate: Point) -> Point:
    pixel_size = WALL_SIZE / CANVAS_SIZE

    x = pixel_size * canvas_coordinate.x - WALL_SIZE / 2
    y = -(pixel_size * canvas_coordinate.y - WALL_SIZE / 2)
    z = WALL_Z
    return point(x, y, z)


def run() -> None:
    # Eye is at (0,0, 5)
    origin = point(0, 0, 5)
    shadow = Color(1, 0, 0)

    the_object = sphere()
    the_object.set_transform(shearing(1, 0, 0, 0, 0, 0) * scaling(0.5, 1, 1))
    canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE)

    for i in range(CANVAS_SIZE):
        for j in range(CANVAS_SIZE):
            target = canvas_to_world(point(i, j, 0))
            ray = Ray(origin, normalize(target - origin))
            if hit(intersect(the_object, ray)) is not None:
                canvas.write_pixel(i, j, shadow)

    PPM(canvas).save_to_file("silhouette.ppm")


if __name__ == "__main__":
    run()
