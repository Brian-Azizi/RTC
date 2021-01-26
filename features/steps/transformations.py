import math
from behave import given, then
from src.transformations import translation, scaling, rotation_x, rotation_y, rotation_z


@given("{var:w} ← translation({x:g}, {y:g}, {z:g})")
def assign_translation(context, var, x, y, z):
    context.variables[var] = translation(x, y, z)


@given("{var:w} ← scaling({x:g}, {y:g}, {z:g})")
def assign_scaling(context, var, x, y, z):
    context.variables[var] = scaling(x, y, z)


@given(u"{var:w} ← rotation_{axis:w}(π / {frac:d})")
def assign_rotation(context, var, axis, frac):
    if axis == "x":
        rotation = rotation_x
    elif axis == "y":
        rotation = rotation_y
    elif axis == "z":
        rotation = rotation_z
    else:
        raise ValueError("Invalid rotation axis")

    context.variables[var] = rotation(math.pi / frac)
