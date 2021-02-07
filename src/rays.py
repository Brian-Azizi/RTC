from __future__ import annotations
from dataclasses import dataclass
from src.tuple import Point, Vector
from src.matrix import Matrix


@dataclass(frozen=True)
class Ray:
    origin: Point
    direction: Vector

    def position(self, t: float) -> Point:
        return self.origin + t * self.direction

    def transform(self, matrix: Matrix) -> Ray:
        return Ray(
            matrix * self.origin,
            matrix * self.direction,
        )
