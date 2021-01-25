from typing import List

RawMatrix = List[List[float]]


class Matrix:
    raw_matrix: RawMatrix

    def __init__(self, raw_matrix: RawMatrix) -> None:
        self.raw_matrix = raw_matrix

    def at(self, i: int, j: int) -> float:
        return self.raw_matrix[i][j]