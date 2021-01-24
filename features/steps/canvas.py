from behave import given, then, when
from src.canvas import Canvas
from src.tuple import Color


@given("{var} ← canvas({width:d}, {height:d})")
def assign_canvas(context, var, width, height):
    context.variables[var] = Canvas(width, height)


@then(u"every pixel of {var} is color({x:g}, {y:g}, {z:g})")
def check_all_canvas_pixels(context, var, x, y, z):
    canvas = context.variables[var]
    expected = Color(x, y, z)

    def check_pixel(p: Color):
        assert p == expected

    canvas.for_each_pixel(check_pixel)


@when(u"write_pixel({canvas_var}, {x:d}, {y:d}, {pixel_var})")
def write_canvas_pixel(context, canvas_var, x, y, pixel_var):
    canvas = context.variables[canvas_var]
    pixel = context.variables[pixel_var]
    canvas.write_pixel(x, y, pixel)


@then(u"pixel_at({canvas_var}, {x:d}, {y:d}) = {pixel_var}")
def check_canvas_pixel(context, canvas_var, x, y, pixel_var):
    canvas = context.variables[canvas_var]
    pixel = context.variables[pixel_var]
    assert canvas.pixel_at(x, y) == pixel
