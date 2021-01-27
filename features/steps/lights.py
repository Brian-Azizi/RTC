from behave import when, given
from src.lights import PointLight
from src.tuple import point
from src.color import Color


@when(u"{var:w} ← point_light({position:w}, {intensity:w})")
def assign_light(context, var, position, intensity):
    p = context.variables[position]
    i = context.variables[intensity]
    context.variables[var] = PointLight(p, i)


@given(u"{var:w} ← point_light(point({x:g}, {y:g}, {z:g}), color({r:g}, {g:g}, {b:g}))")
def assign_light_inline(context, var, x, y, z, r, g, b):
    context.variables[var] = PointLight(point(x, y, z), Color(r, g, b))
