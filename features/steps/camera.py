from behave import given, then, when
from src.camera import Camera


@given(u"{var:w} ← {value:g}")
def assign_number(context, var, value):
    context.variables[var] = value


@when(u"{var:w} ← camera({hsize_var:w}, {vsize_var:w}, {field_of_view:w})")
def assign_camera(context, var, hsize_var, vsize_var, field_of_view):
    hsize = context.variables[hsize_var]
    vsize = context.variables[vsize_var]
    fov = context.variables[field_of_view]
    context.variables[var] = Camera(hsize, vsize, fov)