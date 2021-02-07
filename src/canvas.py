from typing import Callable, Optional
from src.color import Color


class Canvas:
    PPM_MAGIC_NUMBER = "P3"
    MAX_COLOR_VALUE = 255
    PPM_MAX_LINE_LENGTH = 70

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        black = Color(0, 0, 0)
        self.fill(black)

    def for_each_pixel(self, callback: Callable[[Color], None]) -> None:
        for row in self.grid:
            for pixel in row:
                callback(pixel)

    def write_pixel(self, x: int, y: int, pixel: Color) -> None:
        if self.is_inside(x, y):
            self.grid[y][x] = pixel

    def fill(self, pixel: Color) -> None:
        self.grid = [[pixel for i in range(self.width)] for j in range(self.height)]

    def pixel_at(self, x: int, y: int) -> Optional[Color]:
        return self.grid[y][x] if self.is_inside(x, y) else None

    def is_inside(self, x: int, y: int) -> bool:
        return 0 <= x and x < self.width and 0 <= y and y < self.height
