from behave import given, when
from src.planes import Plane
from src.tuple import point


@given(u"{var:w} ← plane()")
def assign_plane(context, var):
    context.variables[var] = Plane()


@when(u"{var:w} ← local_normal_at({plane:w}, point({x:g}, {y:g}, {z:g}))")
def assign_local_normal(context, var, plane, x, y, z):
    p = context.variables[plane]
    context.variables[var] = p.local_normal_at(point(x, y, z))
