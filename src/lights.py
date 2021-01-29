from src.tuple import Point
from src.color import Color
from dataclasses import dataclass


@dataclass
class PointLight:
    position: Point
    intensity: Color

    def __init__(self, position: Point, intensity: Color) -> None:
        self.position = position
        self.intensity = intensity
