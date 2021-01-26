from behave import when, given, then
from src.intersection import Intersection, intersections


@given(u"{var:w} ← intersection({t:g}, {obj:w})")
@when(u"{var:w} ← intersection({t:g}, {obj:w})")
def assign_intersection(context, var, t, obj):
    variable = context.variables[obj]
    context.variables[var] = Intersection(t, variable)


@when(u"{var:w} ← intersections({var_list})")
def assign_intersections(context, var, var_list):
    var_names = [v.strip() for v in var_list.split(",")]
    variables = [context.variables[v] for v in var_names]
    context.variables[var] = intersections(*variables)


@then(u"{var:w}[{index:d}].{attribute:w} = {value:g}")
def check_list_member_attribute(context, var, index, attribute, value):
    array = context.variables[var]
    assert getattr(array[index], attribute) == value
