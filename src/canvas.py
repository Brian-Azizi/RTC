from src.color import Color
from typing import Callable


class Canvas:
    PPM_MAGIC_NUMBER = "P3"
    MAX_COLOR_VALUE = 255

    # @classmethod
    # def pixel_to_ppm_str(cls, pixel: Color):
    #     scaled = pixel * cls.MAX_COLOR_VALUE
    #     return f"{scaled.red} {scaled.green} {scaled.blue}"

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

    def to_ppm(self):
        lines = [
            self.PPM_MAGIC_NUMBER,
            f"{self.width} {self.height}",
            str(self.MAX_COLOR_VALUE),
        ]

        for row in self.grid:
            line = ""
            for pixel in row:
                line += str(pixel)
            lines.append(line)

        return "\n".join(lines)
