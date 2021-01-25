from dataclasses import dataclass
from src.tuple import Point, Vector, point, vector, normalize


@dataclass
class Projectile:
    position: Point
    velocity: Vector


@dataclass
class Environment:
    gravity: Vector
    wind: Vector


def tick(environment, projectile):
    position = projectile.position + projectile.velocity
    velocity = projectile.velocity + environment.gravity + environment.wind
    return Projectile(position, velocity)


def run():
    projectile = Projectile(
        point(0, 1, 0),
        normalize(vector(1, 1, 0)),
    )


run()
