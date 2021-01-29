from typing import List, Optional
from src.intersection import Object, Intersections, intersections
from src.rays import Ray
from src.lights import PointLight
from src.spheres import Sphere, intersect
from src.transformations import scaling
from src.tuple import point
from src.color import Color
from src.materials import Material


class World:
    objects: List[Object]
    light: Optional[PointLight]

    def __init__(self) -> None:
        self.objects = []
        self.light = None


def default_world() -> World:
    """A default world with 2 spheres and a light"""
    sphere_1 = Sphere()
    sphere_1.material = Material()
    sphere_1.material.color = Color(0.8, 1.0, 0.6)
    sphere_1.material.diffuse = 0.7
    sphere_1.material.specular = 0.2
    sphere_2 = Sphere()
    sphere_2.transform = scaling(0.5, 0.5, 0.5)

    world = World()
    world.light = PointLight(point(-10, 10, -10), Color(1, 1, 1))
    world.objects.append(sphere_1)
    world.objects.append(sphere_2)

    return world


def intersect_world(world: World, ray: Ray) -> Intersections:
    xs = []
    for s in world.objects:
        xs.extend(intersect(s, ray))

    return intersections(*xs)
