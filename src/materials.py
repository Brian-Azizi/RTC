import math
from src.color import Color
from src.tuple import Point, Vector, normalize, dot, reflect
from src.lights import PointLight
from dataclasses import dataclass


@dataclass
class Material:
    color: Color = Color(1, 1, 1)
    ambient: float = 0.1
    diffuse: float = 0.9
    specular: float = 0.9
    shininess: float = 200.0


def lighting(
    m: Material,
    light: PointLight,
    point: Point,
    eye: Vector,
    normal: Vector,
    in_shadow: bool = False,
) -> Color:
    """
    Compute color at a point on the surface using the Phong Reflection Model
    Composition made up of ambient light, diffused light and specular light
    """
    effective_color = m.color * light.intensity
    ambient = effective_color * m.ambient

    if in_shadow:
        return ambient

    black = Color(0, 0, 0)
    light_direction = normalize(light.position - point)
    light_direction_cosine = dot(light_direction, normal)
    if light_direction_cosine < 0:
        # Light source is on other side of surface => only ambient lighting
        diffuse = black
        specular = black
    else:
        diffuse = effective_color * m.diffuse * light_direction_cosine

        reflection = reflect(-light_direction, normal)
        reflection_eye_cosine = dot(reflection, eye)

        if reflection_eye_cosine <= 0:
            # Light is reflected away from the eye => no specular lighting
            specular = black
        else:
            factor = reflection_eye_cosine ** int(m.shininess)
            specular = light.intensity * m.specular * factor

    return ambient + diffuse + specular
