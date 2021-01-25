from dataclasses import dataclass
from src.tuple import Point, Vector, point, vector, normalize
from src.color import Color
from src.canvas import Canvas
from src.ppm import PPM


@dataclass
class Projectile:
    position: Point
    velocity: Vector


@dataclass
class Environment:
    gravity: Vector
    wind: Vector


def tick(environment: Environment, projectile: Projectile) -> Projectile:
    position = projectile.position + projectile.velocity
    velocity = projectile.velocity + environment.gravity + environment.wind
    return Projectile(position, velocity)


def draw_projectile(canvas: Canvas, projectile: Projectile) -> None:
    projectile_color = Color(1, 0, 0)
    x = int(round(projectile.position.x))
    y = canvas.height - int(round(projectile.position.y))

    canvas.write_pixel(x, y, projectile_color)


def run() -> None:
    start = point(0, 1, 0)
    velocity = normalize(vector(1, 1, 0))
    gravity = vector(0, -0.1, 0)
    wind = vector(-0.01, 0, 0)

    projectile = Projectile(start, velocity)
    environment = Environment(gravity, wind)
    canvas = Canvas(10, 10)

    draw_projectile(canvas, projectile)
    num_ticks = 0
    while projectile.position.y >= 0:
        projectile = tick(environment, projectile)
        draw_projectile(canvas, projectile)
        num_ticks += 1

    ppm = PPM(canvas)

    print(ppm.to_string())
    print(f"Projectile flew for {num_ticks} ticks.")

    file_name = "projectile.ppm"
    ppm.save_to_file(file_name)
    print(f"Output stored to {file_name}")
