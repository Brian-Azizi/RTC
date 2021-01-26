from src.matrix import Matrix, identity


def translation(x: float, y: float, z: float) -> Matrix:
    result = identity(4)
    result[0, 3] = x
    result[1, 3] = y
    result[2, 3] = z
    return result