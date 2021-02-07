from behave import given
from src.test_shape import TestShape


@given(u"{var:w} ← test_shape()")
def assign_test_shape(context, var):
    context.variables[var] = TestShape()
