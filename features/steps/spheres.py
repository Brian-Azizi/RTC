from behave import given, then, when
from src.spheres import sphere, intersect


@given(u"{var:w} ← sphere()")
def assign_sphere(context, var):
    context.variables[var] = sphere()


@when(u"{var:w} ← intersect({sphere_var:w}, {ray_var:w})")
def assign_intersect(context, var, sphere_var, ray_var):
    s = context.variables[sphere_var]
    r = context.variables[ray_var]
    context.variables[var] = intersect(s, r)


@then(u"{var:w}[{index:d}] = {value:g}")
def check_index(context, var, index, value):
    variable = context.variables[var]
    assert variable[index] == value


@when(u"set_transform({sphere_object:w}, {transform:w})")
def set_transform(context, sphere_object, transform):
    s = context.variables[sphere_object]
    t = context.variables[transform]
    s.set_transform(t)
