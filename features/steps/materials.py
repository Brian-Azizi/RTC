from behave import given, when, then
from src.materials import Material, lighting


@given(u"{var:w} ← material()")
def assign_material(context, var):
    context.variables[var] = Material()


@then(u"{var:w} = material()")
def check_material(context, var):
    variable = context.variables[var]
    assert variable == Material()


@when(u"{res:w} ← lighting({mat:w}, {light:w}, {position:w}, {eye_v:w}, {normal_v:w})")
def assign_lighting(context, res, mat, light, position, eye_v, normal_v):
    material = context.variables[mat]
    l = context.variables[light]
    p = context.variables[position]
    eye = context.variables[eye_v]
    normal = context.variables[normal_v]

    context.variables[res] = lighting(material, l, p, eye, normal)
