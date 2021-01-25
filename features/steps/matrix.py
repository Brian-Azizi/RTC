from behave import given, then, model
from src.matrix import Matrix, RawMatrix


def get_raw_matrix_from_behave_table(table: model.Table) -> RawMatrix:
    m = [
        [float(h) for h in table.headings],
    ] + [[float(c) for c in r.cells] for r in table.rows]
    return m


@given("the following {n:d}x{m:d} matrix {var}")
def assign_matrix(context, var, n, m):
    raw_matrix = get_raw_matrix_from_behave_table(context.table)
    context.variables[var] = Matrix(raw_matrix)


@then("{var}[{i:d},{j:d}] = {value:g}")
def check_matrix_entry(context, var, i, j, value):
    matrix = context.variables[var]
    assert matrix.at(i, j) == value
