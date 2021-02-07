from typing import List, Optional
from src.intersection import (
    Shape,
    Intersections,
    intersections,
    PreparedComputation,
    find_hit,
)
from src.rays import Ray
from src.lights import PointLight
from src.spheres import Sphere, intersect
from src.transformations import scaling
from src.tuple import point, Point, magnitude, normalize
from src.color import Color
from src.materials import Material, lighting


class World:
    objects: List[Shape]
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


def shade_hit(world: World, comps: PreparedComputation) -> Color:
    if world.light is None:
        raise ValueError("No light source present")
    else:
        shadowed = is_shadowed(world, comps.over_point)
        return lighting(
            comps.shape.material,
            world.light,
            comps.point,
            comps.eye_vector,
            comps.normal_vector,
            shadowed,
        )


def color_at(world: World, ray: Ray) -> Color:
    xs = intersect_world(world, ray)
    hit = find_hit(xs)
    if hit is None:
        return Color(0, 0, 0)

    comps = PreparedComputation(hit, ray)
    return shade_hit(world, comps)


def is_shadowed(world: World, point: Point) -> bool:
    if world.light is None:
        return False
    else:
        light_direction = world.light.position - point
        distance = magnitude(light_direction)
        ray = Ray(point, normalize(light_direction))
        intersections = intersect_world(world, ray)
        hit = find_hit(intersections)

        if hit is None or hit.t > distance:
            return False

        return True
