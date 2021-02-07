from src.canvas import Canvas
from src.rays import Ray, position
from src.color import Color
from src.intersection import find_hit
from src.spheres import Sphere
from src.tuple import point, Point, normalize
from src.ppm import PPM
from src.materials import lighting
from src.lights import PointLight


# Canvas size
CANVAS_SIZE = 400

# Wall is normal to z-axis
WALL_Z = -10

# Wall Size
WALL_SIZE = 7


def canvas_to_world(canvas_coordinate: Point) -> Point:
    pixel_size = WALL_SIZE / CANVAS_SIZE

    x = pixel_size * canvas_coordinate.x - WALL_SIZE / 2
    y = -(pixel_size * canvas_coordinate.y - WALL_SIZE / 2)
    z = WALL_Z
    return point(x, y, z)


def run() -> None:
    # Eye is at (0,0, 5)
    origin = point(0, 0, 5)

    shape = Sphere()
    # shape.set_transform(scaling(0.5, 1, 1))
    shape.material.color = Color(0.9, 0.2, 1)

    light = PointLight(point(-10, 10, 10), Color(1, 1, 1))
    canvas = Canvas(CANVAS_SIZE, CANVAS_SIZE)

    for i in range(CANVAS_SIZE):
        for j in range(CANVAS_SIZE):
            target = canvas_to_world(point(i, j, 0))
            ray = Ray(origin, normalize(target - origin))
            hit = find_hit(shape.intersect(ray))
            if hit is not None:
                hit_point = position(ray, hit.t)
                normal = hit.shape.normal_at(hit_point)
                pixel_color = lighting(
                    hit.shape.material, light, hit_point, -ray.direction, normal
                )
                canvas.write_pixel(i, j, pixel_color)

    PPM(canvas).save_to_file("sphere.ppm")


if __name__ == "__main__":
    run()
