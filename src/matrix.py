from __future__ import annotations
from typing import List, Tuple as TupleType, Union
from src.tuple import Tuple


RawMatrix = List[List[float]]


class Matrix:
    raw_matrix: RawMatrix

    def __init__(self, raw_matrix: RawMatrix) -> None:
        self.raw_matrix = raw_matrix

    def __repr__(self) -> str:
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

    def __mul__(self, other: Union[Matrix, Tuple]) -> Union[Matrix, Tuple]:
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

        elif isinstance(other, Tuple):
            if self.dimensions != (4, 4):
                raise NotImplementedError(
                    "Matrix X Tuple is only supported for 4x4 matrices"
                )

            return Tuple(
                sum([self.at(0, j) * other[j] for j in range(4)]),
                sum([self.at(1, j) * other[j] for j in range(4)]),
                sum([self.at(2, j) * other[j] for j in range(4)]),
                sum([self.at(3, j) * other[j] for j in range(4)]),
            )

        raise TypeError(f"Multiplication is not supported for {type(other)}")

    def at(self, i: int, j: int) -> float:
        return self.raw_matrix[i][j]

    def set(self, i: int, j: int, value: float) -> None:
        self.raw_matrix[i][j] = value

    @property
    def dimensions(self) -> TupleType[int, int]:
        return (self.num_rows, self.num_cols)

    @property
    def num_rows(self) -> int:
        return len(self.raw_matrix)

    @property
    def num_cols(self) -> int:
        return len(self.raw_matrix[0])


def zeros(num_rows: int, num_cols: int) -> Matrix:
    raw = [[0.0 for i in range(num_cols)] for j in range(num_rows)]
    return Matrix(raw)


def identity(n: int) -> Matrix:
    raw = [[1.0 if i == j else 0.0 for i in range(n)] for j in range(n)]
    return Matrix(raw)
