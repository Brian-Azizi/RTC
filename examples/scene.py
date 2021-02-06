import math
from typing import List
from src.spheres import Sphere
from src.transformations import (
    scaling,
    translation,
    rotation_y,
    rotation_x,
    view_transform,
)
from src.color import Color
from src.world import World
from src.lights import PointLight
from src.tuple import point, vector
from src.camera import Camera
from src.ppm import PPM


def run() -> None:
    room = create_room()
    objects = create_objects()
    world = World()
    world.light = PointLight(point(-10, 10, -10), Color(1, 1, 1))
    world.objects.extend(room)
    world.objects.extend(objects)
    camera = Camera(400, 200, math.pi / 3)
    camera.transform = view_transform(
        point(0, 1.5, -5), point(0, 1, 0), vector(0, 1, 0)
    )
    canvas = camera.render(world)
    PPM(canvas).save_to_file("scene.ppm")


def create_room() -> List[Sphere]:
    floor = Sphere()
    floor.transform = scaling(10, 0.01, 10)
    floor.material.color = Color(1, 0.9, 0.9)
    floor.material.specular = 0

    left_wall = Sphere()
    left_wall.transform = (
        translation(0, 0, 5)
        * rotation_y(-math.pi / 4)
        * rotation_x(math.pi / 2)
        * scaling(10, 0.01, 10)
    )
    left_wall.material = floor.material

    right_wall = Sphere()
    right_wall.transform = (
        translation(0, 0, 5)
        * rotation_y(math.pi / 4)
        * rotation_x(math.pi / 2)
        * scaling(10, 0.01, 10)
    )
    right_wall.material = floor.material

    return [floor, left_wall, right_wall]


def create_objects() -> List[Sphere]:
    middle = Sphere()
    middle.transform = translation(-0.5, 1, 0.5)
    middle.material.color = Color(0.1, 1, 0.5)
    middle.material.diffuse = 0.7
    middle.material.specular = 0.3

    right = Sphere()
    right.transform = translation(1.5, 0.5, -0.5) * scaling(0.5, 0.5, 0.5)
    right.material.color = Color(0.5, 1, 0.1)
    right.material.diffuse = 0.7
    right.material.specular = 0.3

    left = Sphere()
    left.transform = translation(-1.5, 0.33, -0.75) * scaling(0.33, 0.33, 0.33)
    left.material.color = Color(1, 0.8, 0.1)
    left.material.diffuse = 0.7
    left.material.specular = 0.3

    return [middle, right, left]


if __name__ == "__main__":
    run()
