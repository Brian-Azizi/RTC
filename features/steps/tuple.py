from behave import given, when, then
from src.tuple import Tuple


@given("{var} ← tuple({x:f}, {y:f}, {z:f}, {w:f})")
def assign_tuple(context, var, x, y, z, w):
    context.variables[var] = Tuple(x, y, z, w)


@then("{var}.{att} = {num:f}")
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
