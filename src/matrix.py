from __future__ import annotations
from typing import List, Tuple as TupleType, Union
from src.tuple import Tuple
from src.helpers import approximately_equals, equals

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
                    if not equals(self[i, j], other[i, j]):
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
                        value += self[i, k] * other[k, j]
                    result[i, j] = value

            return result

        elif isinstance(other, Tuple):
            if self.dimensions != (4, 4):
                raise NotImplementedError(
                    "Matrix X Tuple is only supported for 4x4 matrices"
                )

            return Tuple(
                sum([self[0, j] * other[j] for j in range(4)]),
                sum([self[1, j] * other[j] for j in range(4)]),
                sum([self[2, j] * other[j] for j in range(4)]),
                sum([self[3, j] * other[j] for j in range(4)]),
            )

        raise TypeError(f"Multiplication is not supported for {type(other)}")

    def __getitem__(self, key: TupleType[int, int]) -> float:
        if isinstance(key, tuple):
            return self.raw_matrix[key[0]][key[1]]

        raise ValueError("Matrix is only subscriptable by a tuple key")

    def __setitem__(self, key: TupleType[int, int], newvalue: float) -> None:
        if isinstance(key, tuple):
            self.raw_matrix[key[0]][key[1]] = newvalue
        else:
            raise ValueError("Matrix is only subscriptable by a tuple key")

    @property
    def dimensions(self) -> TupleType[int, int]:
        return (self.num_rows, self.num_cols)

    @property
    def num_rows(self) -> int:
        return len(self.raw_matrix)

    @property
    def num_cols(self) -> int:
        return len(self.raw_matrix[0])

    def approximately_equals(self, other: Matrix) -> bool:
        if isinstance(other, Matrix):
            if self.num_rows != other.num_rows:
                return False
            if self.num_cols != other.num_cols:
                return False

            for i in range(self.num_rows):
                for j in range(self.num_cols):
                    if not approximately_equals(self[i, j], other[i, j]):
                        return False
            return True

        return False


def zeros(num_rows: int, num_cols: int) -> Matrix:
    raw = [[0.0 for i in range(num_cols)] for j in range(num_rows)]
    return Matrix(raw)


def identity(n: int) -> Matrix:
    raw = [[1.0 if i == j else 0.0 for i in range(n)] for j in range(n)]
    return Matrix(raw)


def transpose(m: Matrix) -> Matrix:
    result = zeros(m.num_cols, m.num_rows)

    for i in range(m.num_rows):
        for j in range(m.num_cols):
            result[j, i] = m[i, j]

    return result


def determinant(m: Matrix) -> float:
    if m.num_cols != m.num_rows:
        raise ValueError("Determinant only supported for square matrices")

    if m.dimensions == (2, 2):
        return m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0]

    result = 0.0
    for i in range(m.num_cols):
        result += m[0, i] * cofactor(m, 0, i)

    return result


def submatrix(m: Matrix, row_to_delete: int, col_to_delete: int) -> Matrix:
    result = zeros(m.num_rows - 1, m.num_cols - 1)
    for i in range(result.num_rows):
        old_i = i + 1 if i >= row_to_delete else i
        for j in range(result.num_cols):
            old_j = j + 1 if j >= col_to_delete else j
            result[i, j] = m[old_i, old_j]

    return result


def minor(m: Matrix, i: int, j: int) -> float:
    sub = submatrix(m, i, j)
    return determinant(sub)


def cofactor(m: Matrix, i: int, j: int) -> float:
    m_minor = minor(m, i, j)
    return m_minor if (i + j) % 2 == 0 else -m_minor


def is_invertible(m: Matrix) -> bool:
    det = determinant(m)
    return not equals(det, 0)


def inverse(m: Matrix) -> Matrix:
    det = determinant(m)
    if equals(det, 0):
        raise ValueError("Matrix is not invertible")

    result = zeros(m.num_rows, m.num_cols)

    for i in range(m.num_rows):
        for j in range(m.num_cols):
            c = cofactor(m, i, j)
            result[j, i] = c / det

    return result
