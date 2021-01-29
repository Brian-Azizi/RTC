from behave import given, then, when
from src.camera import Camera


@given(u"{var:w} ← {value:g}")
def assign_number(context, var, value):
    context.variables[var] = value


@when(u"{var:w} ← camera({hsize_var:w}, {vsize_var:w}, {field_of_view:w})")
def assign_camera_1(context, var, hsize_var, vsize_var, field_of_view):
    hsize = context.variables[hsize_var]
    vsize = context.variables[vsize_var]
    fov = context.variables[field_of_view]
    context.variables[var] = Camera(hsize, vsize, fov)


@given(u"{var:w} ← camera({hsize:g}, {vsize:g}, {field_of_view:g})")
def assign_camera_2(context, var, hsize, vsize, field_of_view):
    context.variables[var] = Camera(hsize, vsize, field_of_view)