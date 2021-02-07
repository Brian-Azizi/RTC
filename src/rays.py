from __future__ import annotations
from dataclasses import dataclass
from src.tuple import Point, Vector
from src.matrix import Matrix


@dataclass(frozen=True)
class Ray:
    origin: Point
    direction: Vector


def position(ray: Ray, t: float) -> Point:
    return ray.origin + t * ray.direction


def transform(ray: Ray, matrix: Matrix) -> Ray:
    return Ray(
        matrix * ray.origin,
        matrix * ray.direction,
    )
