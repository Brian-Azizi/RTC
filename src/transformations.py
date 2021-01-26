import math
from src.matrix import Matrix, identity


def translation(x: float, y: float, z: float) -> Matrix:
    result = identity(4)
    result[0, 3] = x
    result[1, 3] = y
    result[2, 3] = z
    return result


def scaling(x: float, y: float, z: float) -> Matrix:
    result = identity(4)
    result[0, 0] = x
    result[1, 1] = y
    result[2, 2] = z
    return result


def rotation_x(angle: float) -> Matrix:
    result = identity(4)
    result[1, 1] = math.cos(angle)
    result[1, 2] = -math.sin(angle)
    result[2, 1] = math.sin(angle)
    result[2, 2] = math.cos(angle)
    return result


def rotation_y(angle: float) -> Matrix:
    result = identity(4)
    result[0, 0] = math.cos(angle)
    result[0, 2] = math.sin(angle)
    result[2, 0] = -math.sin(angle)
    result[2, 2] = math.cos(angle)
    return result


def rotation_z(angle: float) -> Matrix:
    result = identity(4)
    result[0, 0] = math.cos(angle)
    result[0, 1] = -math.sin(angle)
    result[1, 0] = math.sin(angle)
    result[1, 1] = math.cos(angle)
    return result


def shearing(
    x_y: float, x_z: float, y_x: float, y_z: float, z_x: float, z_y: float
) -> Matrix:
    result = identity(4)
    result[0, 1] = x_y
    result[0, 2] = x_z
    result[1, 0] = y_x
    result[1, 2] = y_z
    result[2, 0] = z_x
    result[2, 1] = z_y
    return result
