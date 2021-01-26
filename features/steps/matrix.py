from behave import given, then, model
from src.matrix import Matrix, RawMatrix


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
    assert matrix.at(i, j) == value


@then("{var_1:w} = {var_2:w}")
def check_equality(context, var_1, var_2):
    matrix_1 = context.variables[var_1]
    matrix_2 = context.variables[var_2]
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
