from src.tuple import Color
from typing import Callable


class Canvas:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[Color(0, 0, 0)] * width] * height

    def for_each_pixel(self, callback: Callable[[Color], None]) -> None:
        for row in self.grid:
            for pixel in row:
                callback(pixel)

    def write_pixel(self, x: int, y: int, pixel: Color) -> None:
        self.grid[y][x] = pixel

    def pixel_at(self, x: int, y: int) -> Color:
        return self.grid[y][x]