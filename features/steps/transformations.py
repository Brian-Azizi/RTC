import math
from behave import given, then, when
from src.transformations import (
    translation,
    scaling,
    rotation_x,
    rotation_y,
    rotation_z,
    shearing,
)


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


@given(u"{var:w} ← shearing({x_y:g}, {x_z:g}, {y_x:g}, {y_z:g}, {z_x:g}, {z_y:g})")
def assign_shearing(context, var, x_y, x_z, y_x, y_z, z_x, z_y):
    context.variables[var] = shearing(x_y, x_z, y_x, y_z, z_x, z_y)


@when(u"{var:w} ← {var_c:w} * {var_b:w} * {var_a:w}")
def chain_multiplication(context, var, var_c, var_b, var_a):
    C = context.variables[var_c]
    B = context.variables[var_b]
    A = context.variables[var_a]
    context.variables[var] = C * B * A
