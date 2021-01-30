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


@given(u"{var:w} ← camera({hsize:d}, {vsize:d}, {field_of_view:g})")
def assign_camera_2(context, var, hsize, vsize, field_of_view):
    context.variables[var] = Camera(hsize, vsize, field_of_view)


@when(u"{var:w} ← ray_for_pixel({cam_var:w}, {x:g}, {y:g})")
def assign_ray_for_pixel(context, var, cam_var, x, y):
    camera = context.variables[cam_var]
    context.variables[var] = camera.ray_for_pixel(x, y)


@when(u"{var:w} ← render({cam_var:w}, {world_var:w})")
def assign_image(context, var, cam_var, world_var):
    camera = context.variables[cam_var]
    world = context.variables[world_var]
    context.variables[var] = camera.render(world)
