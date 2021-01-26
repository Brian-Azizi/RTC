from __future__ import annotations
from typing import List, Tuple


RawMatrix = List[List[float]]


class Matrix:
    raw_matrix: RawMatrix
    num_rows: int
    num_cols: int

    def __init__(self, raw_matrix: RawMatrix) -> None:
        self.raw_matrix = raw_matrix
        self.num_rows = len(raw_matrix)
        self.num_cols = len(raw_matrix[0])

    def __repr__(self):
        output = f"<Matrix {self.dimensions}>\n"
        for row in self.raw_matrix:
            line = "| "
            for cell in row:
                line += str(cell) + " | "
            output += line + "\n"
        return output

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

    def __mul__(self, other: Matrix) -> Matrix:
        if isinstance(other, Matrix):
            if self.num_cols != other.num_rows:
                raise ValueError(
                    f"Cannot multiply matrices of dimensions {self.dimensions} and {other.dimensions}"
                )

            result = zeros(self.num_rows, other.num_cols)

            for i in range(self.num_rows):
                for j in range(other.num_cols):
                    value = 0.0
                    for k in range(self.num_cols):
                        value += self.at(i, k) * other.at(k, j)
                    result.set(i, j, value)

            return result

        raise TypeError(f"Multiplication is not supported for {type(other)}")

    def at(self, i: int, j: int) -> float:
        return self.raw_matrix[i][j]

    def set(self, i: int, j: int, value: float) -> None:
        self.raw_matrix[i][j] = value

    @property
    def dimensions(self) -> Tuple[int, int]:
        return (self.num_rows, self.num_cols)


def zeros(num_rows: int, num_cols: int) -> Matrix:
    raw = [[0.0 for i in range(num_cols)] for j in range(num_rows)]
    return Matrix(raw)