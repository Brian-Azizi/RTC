from behave import given, then
from src.transformations import translation, scaling


@given("{var:w} ← translation({x:g}, {y:g}, {z:g})")
def assign_translation(context, var, x, y, z):
    context.variables[var] = translation(x, y, z)


@given("{var:w} ← scaling({x:g}, {y:g}, {z:g})")
def assign_scaling(context, var, x, y, z):
    context.variables[var] = scaling(x, y, z)