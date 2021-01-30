import math
from typing import List
from src.spheres import Sphere
from src.transformations import scaling, translation, rotation_y, rotation_x
from src.color import Color
from src.world import World
from src.lights import PointLight
from src.tuple import point
from src.camera import Camera
from src.ppm import PPM


def run() -> None:
    room = create_room()
    # objects = create_objects()
    world = World()
    world.light = PointLight(point(-10, 10, -10), Color(1, 1, 1))
    world.objects.extend(room)
    camera = Camera(100, 50, math.pi / 3)
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


if __name__ == "__main__":
    run()
