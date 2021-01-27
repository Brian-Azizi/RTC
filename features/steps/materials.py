from behave import given
from src.materials import Material


@given(u"{var:w} ← material()")
def assign_material(context, var):
    context.variables[var] = Material()