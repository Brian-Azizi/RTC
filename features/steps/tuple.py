import math
from behave import given, then, when
from typing import Union
from src.tuple import (
    Tuple,
    point,
    vector,
    magnitude,
    normalize,
    dot,
    cross,
    reflect,
)
from src.color import Color
from src.matrix import identity, Matrix
from src.helpers import is_number, equals
from src.transformations import scaling, translation


def create_structure(
    structure_type: str, x: float, y: float, z: float
) -> Union[Tuple, Color, Matrix]:
    if structure_type == "vector":
        return vector(x, y, z)
    elif structure_type == "point":
        return point(x, y, z)
    elif structure_type == "color":
        return Color(x, y, z)
    elif structure_type == "scaling":
        return scaling(x, y, z)
    elif structure_type == "translation":
        return translation(x, y, z)
    else:
        raise NotImplementedError(f"structure type '{structure_type}' not recognized")


@given("{var} ← tuple({x:g}, {y:g}, {z:g}, {w:g})")
def assign_tuple(context, var, x, y, z, w):
    context.variables[var] = Tuple(x, y, z, w)


@given("{var} ← point({x:g}, {y:g}, {z:g})")
def assign_point(context, var, x, y, z):
    context.variables[var] = point(x, y, z)


@given("{var} ← vector({x:g}, {y:g}, {z:g})")
def assign_vector(context, var, x, y, z):
    context.variables[var] = vector(x, y, z)


@given("{var} ← color({x:g}, {y:g}, {z:g})")
def assign_color(context, var, x, y, z):
    context.variables[var] = Color(x, y, z)


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
    variable_1 = float(var_1) if is_number(var_1) else context.variables[var_1]
    variable_2 = float(var_2) if is_number(var_2) else context.variables[var_2]
    expected = Tuple(x, y, z, w)
    assert variable_1 * variable_2 == expected


@then("{var} / {scalar:g} = tuple({x:g}, {y:g}, {z:g}, {w:g})")
def check_tuple_division(context, var, scalar, x, y, z, w):
    my_variable = context.variables[var]
    expected = Tuple(x, y, z, w)
    assert my_variable / scalar == expected


@then("{var_1} - {var_2} = {tuple_type}({x:g}, {y:g}, {z:g})")
def check_difference(context, var_1, var_2, tuple_type, x, y, z):
    my_variable_1 = context.variables[var_1]
    my_variable_2 = context.variables[var_2]
    expected = create_structure(tuple_type, x, y, z)
    assert expected.approximately_equals(my_variable_1 - my_variable_2)


@then("{var_1} + {var_2} = {tuple_type}({x:g}, {y:g}, {z:g})")
def check_sum(context, var_1, var_2, tuple_type, x, y, z):
    my_variable_1 = context.variables[var_1]
    my_variable_2 = context.variables[var_2]
    expected = create_structure(tuple_type, x, y, z)
    assert expected.approximately_equals(my_variable_1 + my_variable_2)


@then("{var_1} * {var_2} = {tuple_type}({x:g}, {y:g}, {z:g})")
def check_multiplication(context, var_1, var_2, tuple_type, x, y, z):
    variable_1 = float(var_1) if is_number(var_1) else context.variables[var_1]
    variable_2 = float(var_2) if is_number(var_2) else context.variables[var_2]
    expected = create_structure(tuple_type, x, y, z)
    assert expected.approximately_equals(variable_1 * variable_2)


@then("magnitude({var}) = {expected:g}")
def check_magnitude(context, var, expected):
    my_variable = context.variables[var]
    assert magnitude(my_variable) == expected


@then("magnitude({var}) = √{expected:g}")
def check_magnitude_2(context, var, expected):
    my_variable = context.variables[var]
    assert magnitude(my_variable) == math.sqrt(expected)


@then("normalize({var}) = vector({x:g}, {y:g}, {z:g})")
def check_normalize(context, var, x, y, z):
    my_variable = context.variables[var]
    assert normalize(my_variable) == vector(x, y, z)


@then("normalize({var}) = approximately vector({x:g}, {y:g}, {z:g})")
def check_approximate_normalize(context, var, x, y, z):
    my_variable = context.variables[var]
    assert normalize(my_variable).approximately_equals(vector(x, y, z))


@when("{var} ← normalize({other_var})")
def assign_normalize(context, var, other_var):
    other = context.variables[other_var]
    context.variables[var] = normalize(other)


@then("dot({var_1}, {var_2}) = {expected:g}")
def check_dot(context, var_1, var_2, expected):
    v1 = context.variables[var_1]
    v2 = context.variables[var_2]
    assert dot(v1, v2) == expected


@then("cross({var_1}, {var_2}) = vector({x:g}, {y:g}, {z:g})")
def check_cross(context, var_1, var_2, x, y, z):
    v1 = context.variables[var_1]
    v2 = context.variables[var_2]
    assert cross(v1, v2) == vector(x, y, z)


@then("{var_expression} = tuple({x:g}, {y:g}, {z:g}, {w:g})")
def check_tuple(context, var_expression, x, y, z, w):
    var_names = [v.strip() for v in var_expression.split("+")]
    my_variables = [
        -context.variables[var[1:]] if var[0] == "-" else context.variables[var]
        for var in var_names
    ]
    expected = Tuple(x, y, z, w)
    assert sum(my_variables) == expected


@then("{var:w} = {tuple_type}({x:g}, {y:g}, {z:g})")
def check_tuple_type(context, var, tuple_type, x, y, z):
    variable = float(var) if is_number(var) else context.variables[var]
    expected = create_structure(tuple_type, x, y, z)
    assert expected.approximately_equals(variable), f"{expected} ~= {variable}"


@then("{var:w}.{att:w} = {expected:w}")
@then("{var:w}.{att:w} = {expected:g}")
def check_attribute(context, var, att, expected):
    if expected == "identity_matrix":
        exp = identity(4)  # type: Union[Matrix, float]
    elif is_number(expected):
        exp = float(expected)
    elif expected == "true":
        exp = True
    elif expected == "false":
        exp = False
    else:
        exp = context.variables[expected]

    my_variable = context.variables[var]
    if att == "count":
        assert len(my_variable) == exp
    elif isinstance(exp, float) or isinstance(exp, int):
        assert equals(exp, getattr(my_variable, att))
    else:
        assert getattr(my_variable, att) == exp, f"{getattr(my_variable, att)} == {exp}"


@when("{result:w} ← reflect({vec:w}, {nor:w})")
def assign_reflection(context, result, vec, nor):
    v = context.variables[vec]
    normal = context.variables[nor]
    context.variables[result] = reflect(v, normal)
