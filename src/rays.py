from __future__ import annotations
from dataclasses import dataclass, asdict
from src.tuple import Point, Vector


@dataclass(frozen=True)
class Ray:
    origin: Point
    direction: Vector


def position(ray: Ray, t: float) -> Point:
    return ray.origin + t * ray.direction
