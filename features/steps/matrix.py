from behave import given, then, model, when
from src.matrix import (
    Matrix,
    RawMatrix,
    identity,
    transpose,
    determinant,
    submatrix,
    minor,
    cofactor,
    is_invertible,
    inverse,
)


def get_raw_matrix_from_behave_table(table: model.Table) -> RawMatrix:
    m = [
        [float(h) for h in table.headings],
    ] + [[float(c) for c in r.cells] for r in table.rows]
    return m


@given("the following {n:d}x{m:d} matrix {var}")
def assign_matrix_1(context, var, n, m):
    raw_matrix = get_raw_matrix_from_behave_table(context.table)
    context.variables[var] = Matrix(raw_matrix)


@given("the following matrix {var}")
def assign_matrix_2(context, var):
    raw_matrix = get_raw_matrix_from_behave_table(context.table)
    context.variables[var] = Matrix(raw_matrix)


@then("{var}[{i:d},{j:d}] = {value:g}")
def check_matrix_entry(context, var, i, j, value):
    matrix = context.variables[var]
    assert matrix[i, j] == value


@then("{var_1:w} = {var_2:w}")
def check_equality(context, var_1, var_2):
    matrix_1 = context.variables[var_1]
    matrix_2 = identity(4) if var_2 == "identity_matrix" else context.variables[var_2]
    assert matrix_1 == matrix_2


@then("{var_1:w} != {var_2:w}")
def check_inequality(context, var_1, var_2):
    matrix_1 = context.variables[var_1]
    matrix_2 = context.variables[var_2]
    assert matrix_1 != matrix_2


@then("{var_1:w} * {var_2:w} is the following 4x4 matrix")
def matrix_multiplication(context, var_1, var_2):
    matrix_1 = context.variables[var_1]
    matrix_2 = context.variables[var_2]
    expected = Matrix(get_raw_matrix_from_behave_table(context.table))
    assert matrix_1 * matrix_2 == expected, f"{matrix_1 * matrix_2} == {expected}"


@then("{var_1:w} * {var_2:w} is invalid")
def invalid_matrix_multiplication(context, var_1, var_2):
    matrix_1 = context.variables[var_1]
    matrix_2 = context.variables[var_2]
    try:
        matrix_1 * matrix_2
    except ValueError as e:
        assert "Cannot multiply matrices" in str(e)


@then("{var:w} * identity_matrix = {var:w}")
def identity_post(context, var):
    matrix = context.variables[var]
    identity_matrix = identity(matrix.num_rows)
    assert matrix * identity_matrix == matrix


@then("identity_matrix * {var:w} = {var:w}")
def identity_pre(context, var):
    matrix = context.variables[var]
    identity_matrix = identity(matrix.num_rows)
    assert identity_matrix * matrix == matrix


@then("{var_1:w} * {var_2:w} = {var_3:w}")
def check_multiplication(context, var_1, var_2, var_3):
    matrix_1 = context.variables[var_1]
    matrix_2 = context.variables[var_2]
    matrix_3 = context.variables[var_3]
    assert matrix_1 * matrix_2 == matrix_3


@then("transpose({var:w}) is the following matrix")
def check_transpose(context, var):
    matrix = context.variables[var]
    expected = Matrix(get_raw_matrix_from_behave_table(context.table))
    assert transpose(matrix) == expected


@given("{var:w} ← transpose(identity_matrix)")
def assign_identity_transpose(context, var):
    identity_matrix = identity(4)
    context.variables[var] = transpose(identity_matrix)
    context.variables["identity_matrix"] = identity_matrix


@then("determinant({var:w}) = {value:g}")
def check_determinant(context, var, value):
    matrix = context.variables[var]
    assert determinant(matrix) == value


@then("submatrix({var:w}, {i:d}, {j:d}) is the following {p:d}x{q:d} matrix")
def check_submatrix(context, var, i, j, p, q):
    matrix = context.variables[var]
    expected = Matrix(get_raw_matrix_from_behave_table(context.table))
    assert submatrix(matrix, i, j) == expected


@given("{new_var:w} ← submatrix({old_var:w}, {i:d}, {j:d})")
def assign_submatrix(context, new_var, old_var, i, j):
    old = context.variables[old_var]
    context.variables[new_var] = submatrix(old, i, j)


@then("minor({var:w}, {i:d}, {j:d}) = {value:g}")
def check_minor(context, var, i, j, value):
    matrix = context.variables[var]
    assert minor(matrix, i, j) == value


@then("cofactor({var:w}, {i:d}, {j:d}) = {value:g}")
def check_cofactor(context, var, i, j, value):
    matrix = context.variables[var]
    assert cofactor(matrix, i, j) == value


@then("{var:w} is invertible")
def check_invertible(context, var):
    matrix = context.variables[var]
    assert is_invertible(matrix)


@then("{var:w} is not invertible")
def check_not_invertible(context, var):
    matrix = context.variables[var]
    assert is_invertible(matrix) is False


@given("{var_b:w} ← inverse({var_a:w})")
def assign_inverse(context, var_a, var_b):
    matrix_a = context.variables[var_a]
    context.variables[var_b] = inverse(matrix_a)


@then("{var:w}[{i:d},{j:d}] = {numerator:g}/{denominator:g}")
def check_cell(context, var, i, j, numerator, denominator):
    matrix = context.variables[var]
    assert matrix[i, j] == numerator / denominator


@then("{var:w} is the following 4x4 matrix")
def check_matrix(context, var):
    matrix = context.variables[var]
    expected = Matrix(get_raw_matrix_from_behave_table(context.table))
    assert matrix.approximately_equals(expected)


@then("inverse({var:w}) is the following 4x4 matrix")
def check_inverse_matrix(context, var):
    matrix = context.variables[var]
    expected = Matrix(get_raw_matrix_from_behave_table(context.table))
    assert inverse(matrix).approximately_equals(expected)


@given("{var_c:w} ← {var_a:w} * {var_b:w}")
@when("{var_c:w} ← {var_a:w} * {var_b:w}")
def assign_multiplication(context, var_a, var_b, var_c):
    matrix_a = context.variables[var_a]
    matrix_b = context.variables[var_b]
    context.variables[var_c] = matrix_a * matrix_b


@then("{var_c:w} * inverse({var_b:w}) = {var_a:w}")
def check_inverse_multiplication(context, var_a, var_b, var_c):
    matrix_a = context.variables[var_a]
    matrix_b = context.variables[var_b]
    matrix_c = context.variables[var_c]

    print(matrix_a)
    print(matrix_c * inverse(matrix_b))
    assert matrix_c * inverse(matrix_b) == matrix_a
