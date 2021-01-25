from behave import given, then, model


def get_raw_matrix_from_behave(table: model.Table):
    return [table.headings] + table.rows


@given("the following {n:d}x{m:d} matrix {var}")
def assign_matrix(context, var, n, m):
    raw_matrix = get_raw_matrix_from_behave(context.table)
    context.variables[var] = raw_matrix  # Matrix(raw_matrix)


@then("{var}[{i:d},{j:d}] = {value:g}")
def check_matrix_entry(context, var, i, j, value):
    matrix = context.variables[var]
    assert float(matrix[i][j]) == float(value), f"{matrix[j][i]} == {value}"
