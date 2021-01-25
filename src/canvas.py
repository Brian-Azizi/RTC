from typing import Callable
from src.color import Color
from src.helpers import clamp


class Canvas:
    PPM_MAGIC_NUMBER = "P3"
    MAX_COLOR_VALUE = 255
    PPM_MAX_LINE_LENGTH = 70

    @classmethod
    def pixel_to_ppm_str(cls, pixel: Color) -> str:
        scaled = pixel * cls.MAX_COLOR_VALUE

        def clamped(number: float) -> int:
            return int(round(clamp(number, 0, cls.MAX_COLOR_VALUE)))

        return f"{clamped(scaled.red)} {clamped(scaled.green)} {clamped(scaled.blue)}"

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
        self.grid[y][x] = pixel

    def fill(self, pixel: Color) -> None:
        self.grid = [[pixel for i in range(self.width)] for j in range(self.height)]

    def pixel_at(self, x: int, y: int) -> Color:
        return self.grid[y][x]

    def to_ppm(self) -> str:
        lines = [
            self.PPM_MAGIC_NUMBER,
            f"{self.width} {self.height}",
            str(self.MAX_COLOR_VALUE),
        ]

        for row in self.grid:
            line = ""
            for pixel in row:
                line += self.pixel_to_ppm_str(pixel) + " "

            while len(line) > self.PPM_MAX_LINE_LENGTH:
                index = line.rfind(" ", 0, self.PPM_MAX_LINE_LENGTH)
                lines.append(line[:index])
                line = line[index:]
            lines.append(line.strip())

        lines.append("")

        return "\n".join(lines)
