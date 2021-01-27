from behave import when
from src.lights import PointLight


@when(u"{var:w} ← point_light({position:w}, {intensity:w})")
def assign_light(context, var, position, intensity):
    p = context.variables[position]
    i = context.variables[intensity]
    context.variables[var] = PointLight(p, i)
