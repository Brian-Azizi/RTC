from behave import given, then
from src.test_shape import TestShape
from src.tuple import point, vector


@given(u"{var:w} ← test_shape()")
def assign_test_shape(context, var):
    context.variables[var] = TestShape()


@then(u"{shape:w}.saved_ray.origin = point({x:g}, {y:g}, {z:g})")
def check_local_ray_origin(context, shape, x, y, z):
    s = context.variables[shape]
    assert s.local_ray.origin == point(x, y, z)


@then(u"{shape:w}.saved_ray.direction = vector({x:g}, {y:g}, {z:g})")
def check_local_ray_direction(context, shape, x, y, z):
    s = context.variables[shape]
    assert s.local_ray.direction == vector(x, y, z)
