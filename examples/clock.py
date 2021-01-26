import math
from src.tuple import point, Point
from src.transformations import rotation_z, scaling, translation
from src.canvas import Canvas
from src.color import Color
from src.matrix import inverse
from src.ppm import PPM


def run() -> None:
    STEPS = 12
    SIZE = 121
    MIDDLE = SIZE // 2

    canvas = Canvas(SIZE, SIZE)
    color = Color(1, 0, 0)
    color_increment = Color(0, 1.0 / STEPS, -1.0 / STEPS)

    position = point(0, 1, 0)

    rotate = rotation_z(-2 * math.pi / 12)
    translate = translation(MIDDLE, MIDDLE, 0)
    scale = scaling(SIZE // 3, SIZE // 3, 1)

    for i in range(STEPS):
        canvas_position = translate * scale * position
        assert isinstance(canvas_position, Point)
        canvas.write_pixel(
            int(round(canvas_position.x)),
            SIZE - int(round(canvas_position.y)),
            color,
        )
        position = rotate * position  # type: ignore
        color += color_increment

    ppm = PPM(canvas)

    file_name = "clocks.ppm"
    ppm.save_to_file(file_name)
    print(f"Output stored to {file_name}")


if __name__ == "__main__":
    run()
