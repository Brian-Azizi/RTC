from src.canvas import Canvas
from src.color import Color
from src.helpers import clamp


class PPM:
    PPM_MAGIC_NUMBER = "P3"
    MAX_COLOR_VALUE = 255
    PPM_MAX_LINE_LENGTH = 70
    canvas: Canvas

    @classmethod
    def pixel_to_ppm_str(cls, pixel: Color) -> str:
        scaled = pixel * cls.MAX_COLOR_VALUE

        def clamped(number: float) -> int:
            return int(round(clamp(number, 0, cls.MAX_COLOR_VALUE)))

        return f"{clamped(scaled.red)} {clamped(scaled.green)} {clamped(scaled.blue)}"

    def __init__(self, canvas: Canvas):
        self.canvas = canvas

    def to_string(self) -> str:
        lines = [  # ppm header
            self.PPM_MAGIC_NUMBER,
            f"{self.canvas.width} {self.canvas.height}",
            str(self.MAX_COLOR_VALUE),
        ]

        for row in self.canvas.grid:
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

    def save_to_file(self, file_name: str) -> None:
        with open(file_name, "w") as ppm_file:
            ppm_file.write(self.to_string())
