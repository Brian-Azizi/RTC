from abc import ABC, abstractmethod
from src.materials import Material
from src.matrix import Matrix
from src.rays import Ray
from src.tuple import Point, Vector

# from src.intersection import Intersections
from typing import Any


class Shape(ABC):
    transform: Matrix
    material: Material

    @abstractmethod
    def intersect(self, ray: Ray) -> Any:
        pass

    @abstractmethod
    def normal_at(self, world_point: Point) -> Vector:
        pass
