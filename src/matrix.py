from __future__ import annotations
from typing import List


RawMatrix = List[List[float]]


class Matrix:
    raw_matrix: RawMatrix
    num_rows: int
    num_cols: int

    def __init__(self, raw_matrix: RawMatrix) -> None:
        self.raw_matrix = raw_matrix
        self.num_rows = len(raw_matrix)
        self.num_cols = len(raw_matrix[0])

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Matrix):
            if self.num_rows != other.num_rows:
                return False
            if self.num_cols != other.num_cols:
                return False

            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    if self.at(i, j) != other.at(i, j):
                        return False
            return True

        return False

    def at(self, i: int, j: int) -> float:
        return self.raw_matrix[i][j]