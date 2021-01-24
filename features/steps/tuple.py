from behave import given, then
from src.tuple import Tuple, Point, Vector


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


@given("{var} ← tuple({x:g}, {y:g}, {z:g}, {w:g})")
def assign_tuple(context, var, x, y, z, w):
    context.variables[var] = Tuple(x, y, z, w)


@given("{var} ← point({x:g}, {y:g}, {z:g})")
def assign_point(context, var, x, y, z):
    context.variables[var] = Point(x, y, z)


@given("{var} ← vector({x:g}, {y:g}, {z:g})")
def assign_vector(context, var, x, y, z):
    context.variables[var] = Vector(x, y, z)


@then("{var}.{att} = {num:g}")
def check_tuple_attribute(context, var, att, num):
    my_variable = context.variables[var]
    assert getattr(my_variable, att) == num


@then("{var} is a point")
def check_point(context, var):
    my_variable = context.variables[var]
    assert my_variable.w == 1.0


@then("{var} is not a point")
def check_not_point(context, var):
    my_variable = context.variables[var]
    assert my_variable.w != 1.0


@then("{var} is a vector")
def check_vector(context, var):
    my_variable = context.variables[var]
    assert my_variable.w == 0.0


@then("{var} is not a vector")
def check_not_vector(context, var):
    my_variable = context.variables[var]
    assert my_variable.w != 0.0


@then("{var_1} * {var_2} = tuple({x:g}, {y:g}, {z:g}, {w:g})")
def check_tuple_multiplication(context, var_1, var_2, x, y, z, w):
    scalar = float(var_1) if is_number(var_1) else float(var_2)
    my_variable = (
        context.variables[var_1] if is_number(var_2) else context.variables[var_2]
    )
    expected = Tuple(x, y, z, w)
    assert my_variable * scalar == expected


@then("{var} / {scalar:g} = tuple({x:g}, {y:g}, {z:g}, {w:g})")
def check_tuple_division(context, var, scalar, x, y, z, w):
    my_variable = context.variables[var]
    expected = Tuple(x, y, z, w)
    assert my_variable / scalar == expected


@then("{var_1} - {var_2} = {tuple_type}({x:g}, {y:g}, {z:g})")
def check_difference(context, var_1, var_2, tuple_type, x, y, z):
    my_variable_1 = context.variables[var_1]
    my_variable_2 = context.variables[var_2]
    if tuple_type == "vector":
        expected = Vector(x, y, z)
    elif tuple_type == "point":
        expected = Point(x, y, z)
    else:
        raise NotImplementedError(f"tuple type '{tuple_type}' not recognised")
    assert my_variable_1 - my_variable_2 == expected


@then("{var_expression} = tuple({x:g}, {y:g}, {z:g}, {w:g})")
def check_tuple(context, var_expression, x, y, z, w):
    var_names = [v.strip() for v in var_expression.split("+")]
    my_variables = [
        -context.variables[var[1:]] if var[0] is "-" else context.variables[var]
        for var in var_names
    ]
    expected = Tuple(x, y, z, w)
    assert sum(my_variables) == expected
