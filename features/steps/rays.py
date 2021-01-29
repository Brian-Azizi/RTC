from behave import when, then, given
from src.rays import Ray, position, transform
from src.color import Color
from src.tuple import vector, point


@when("{var:w} ← ray({orig:w}, {dir:w})")
def assign_ray(context, var, orig, dir):
    origin = context.variables[orig]
    direction = context.variables[dir]
    context.variables[var] = Ray(origin, direction)


@given("{var:w} ← ray(point({px:g}, {py:g}, {pz:g}), vector({vx:g}, {vy:g}, {vz:g}))")
def assign_ray_inline(context, var, px, py, pz, vx, vy, vz):
    origin = point(px, py, pz)
    direction = vector(vx, vy, vz)
    context.variables[var] = Ray(origin, direction)


@then("position({var:w}, {t:g}) = point({x:g}, {y:g}, {z:g})")
def check_position(context, var, t, x, y, z):
    ray = context.variables[var]
    expected = point(x, y, z)
    assert position(ray, t) == expected


@when("{new_ray:w} ← transform({ray:w}, {matrix:w})")
def assign_transform(context, new_ray, ray, matrix):
    r = context.variables[ray]
    m = context.variables[matrix]
    context.variables[new_ray] = transform(r, m)


@then("{var:w}.{att:w} = {tuple_type:w}({x:g}, {y:g}, {z:g})")
def check_attribute_point(context, var, att, tuple_type, x, y, z):
    if tuple_type == "point":
        expected = point(x, y, z)
    elif tuple_type == "vector":
        expected = vector(x, y, z)
    elif tuple_type == "color":
        expected = Color(x, y, z)  # type: ignore
    else:
        raise ValueError(f"tuple type '{tuple_type}' not recognized")

    my_variable = context.variables[var]
    assert (
        getattr(my_variable, att) == expected
    ), f"{getattr(my_variable, att)} == {expected}"
