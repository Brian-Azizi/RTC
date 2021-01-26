from behave import when, then, given
from src.rays import Ray, position
from src.tuple import vector, point


@when("{var:w} ← ray({orig:w}, {dir:w})")
def assign_ray(context, var, orig, dir):
    origin = context.variables[orig]
    direction = context.variables[dir]
    context.variables[var] = Ray(origin, direction)


@given(u"{var:w} ← ray(point({px:g}, {py:g}, {pz:g}), vector({vx:g}, {vy:g}, {vz:g}))")
def assign_ray_inline(context, var, px, py, pz, vx, vy, vz):
    origin = point(px, py, pz)
    direction = vector(vx, vy, vz)
    context.variables[var] = Ray(origin, direction)


@then("position({var:w}, {t:g}) = point({x:g}, {y:g}, {z:g})")
def check_position(context, var, t, x, y, z):
    ray = context.variables[var]
    expected = point(x, y, z)
    assert position(ray, t) == expected
