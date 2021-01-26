from behave import when, given, then
from src.intersection import Intersection, intersections, hit
from src.helpers import is_number


@given(u"{var:w} ← intersection({t:g}, {obj:w})")
@when(u"{var:w} ← intersection({t:g}, {obj:w})")
def assign_intersection(context, var, t, obj):
    variable = context.variables[obj]
    context.variables[var] = Intersection(t, variable)


@given(u"{var:w} ← intersections({var_list})")
@when(u"{var:w} ← intersections({var_list})")
def assign_intersections(context, var, var_list):
    var_names = [v.strip() for v in var_list.split(",")]
    variables = [context.variables[v] for v in var_names]
    context.variables[var] = intersections(*variables)


@then(u"{var:w}[{index:d}].{attribute:w} = {expected}")
def check_list_member_attribute(context, var, index, attribute, expected):
    exp = float(expected) if is_number(expected) else context.variables[expected]
    array = context.variables[var]
    assert getattr(array[index], attribute) == exp


@when(u"{var_1:w} ← hit({var_2:w})")
def assign_hit(context, var_1, var_2):
    inters = context.variables[var_2]
    context.variables[var_1] = hit(inters)


@then(u"{var:w} is nothing")
def check_none(context, var):
    variable = context.variables[var]
    assert variable is None
