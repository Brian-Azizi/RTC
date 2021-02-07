from behave import when, given, then
from src.shape import Intersection, intersections, find_hit
from src.world import PreparedComputation
from src.helpers import is_number, LONG_EPSILON


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
    context.variables[var_1] = find_hit(inters)


@then(u"{var:w} is nothing")
def check_none(context, var):
    variable = context.variables[var]
    assert variable is None


@when(u"{var:w} ← prepare_computations({intersection_var:w}, {ray_var:w})")
def assign_computations(context, var, intersection_var, ray_var):
    intersection = context.variables[intersection_var]
    ray = context.variables[ray_var]
    context.variables[var] = PreparedComputation(intersection, ray)


@then(u"{var_1:S}.{attr_1:S} = {var_2:D}.{attr_2:D}")
def check_attribute_attribute(context, var_1, attr_1, var_2, attr_2):
    variable_1 = context.variables[var_1]
    variable_2 = context.variables[var_2]
    assert getattr(variable_1, attr_1) == getattr(variable_2, attr_2)


@then(u"{var:w}.{outer:w}.{inner:w} < -EPSILON/2")
def check_epsilon(context, var, outer, inner):
    variable = context.variables[var]
    assert getattr(getattr(variable, outer), inner) < -LONG_EPSILON / 2


@then(u"{var_1:w}.{outer_1:w}.{inner_1:w} > {var_2:w}.{outer_2:w}.{inner_2:w}")
def check_nested(context, var_1, outer_1, inner_1, var_2, outer_2, inner_2):
    variable_1 = context.variables[var_1]
    variable_2 = context.variables[var_2]
    assert getattr(getattr(variable_1, outer_1), inner_1) > getattr(
        getattr(variable_2, outer_2), inner_2
    )
