from behave import when, given, then
from src.intersection import Intersection


@when(u"{var:w} ← intersection({t:g}, {obj:w})")
def assign_intersection(context, var, t, obj):
    variable = context.variables[obj]
    context.variables[var] = Intersection(t, variable)
