import math
from behave import given, then
from src.transformations import translation, scaling, rotation_x


@given("{var:w} ← translation({x:g}, {y:g}, {z:g})")
def assign_translation(context, var, x, y, z):
    context.variables[var] = translation(x, y, z)


@given("{var:w} ← scaling({x:g}, {y:g}, {z:g})")
def assign_scaling(context, var, x, y, z):
    context.variables[var] = scaling(x, y, z)


@given(u"{var:w} ← rotation_x(π / {frac:d})")
def assign_rotation_x(context, var, frac):
    context.variables[var] = rotation_x(math.pi / frac)
