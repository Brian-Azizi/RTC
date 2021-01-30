from behave import given, then, when
from src.canvas import Canvas
from src.color import Color
from src.ppm import PPM


@given("{var} ← canvas({width:d}, {height:d})")
def assign_canvas(context, var, width, height):
    context.variables[var] = Canvas(width, height)


@when("every pixel of {var} is set to color({r:g}, {g:g}, {b:g})")
def assign_all_pixels(context, var, r, g, b):
    canvas = context.variables[var]
    color = Color(r, g, b)
    canvas.fill(color)


@then("every pixel of {var} is color({x:g}, {y:g}, {z:g})")
def check_all_canvas_pixels(context, var, x, y, z):
    canvas = context.variables[var]
    expected = Color(x, y, z)

    def check_pixel(p: Color) -> None:
        assert p == expected
        return None

    canvas.for_each_pixel(check_pixel)


@when("write_pixel({canvas_var}, {x:d}, {y:d}, {pixel_var})")
def write_canvas_pixel(context, canvas_var, x, y, pixel_var):
    canvas = context.variables[canvas_var]
    pixel = context.variables[pixel_var]
    canvas.write_pixel(x, y, pixel)


@then("pixel_at({canvas_var}, {x:d}, {y:d}) = {pixel_var}")
def check_canvas_pixel(context, canvas_var, x, y, pixel_var):
    canvas = context.variables[canvas_var]
    pixel = context.variables[pixel_var]
    assert canvas.pixel_at(x, y) == pixel, f"{canvas.pixel_at(x, y)} == {pixel}"


@when("{ppm_var} ← canvas_to_ppm({canvas_var})")
def assign_ppm(context, ppm_var, canvas_var):
    canvas = context.variables[canvas_var]
    ppm = PPM(canvas)
    context.variables[ppm_var] = ppm.to_string()


@then("lines {start:d}-{end:d} of {ppm_var} are")
def check_ppm_lines(context, start, end, ppm_var):
    ppm = context.variables[ppm_var]
    assert context.text == "\n".join(ppm.split("\n")[start - 1 : end])


@then("{ppm_var} ends with a newline character")
def check_ppm_final_line(context, ppm_var):
    ppm = context.variables[ppm_var]
    lines = ppm.split("\n")
    assert lines[-1] == ""
