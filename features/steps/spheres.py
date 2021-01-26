from behave import given, then, when
from src.spheres import sphere, intersect
from src.transformations import scaling, translation


@given("{var:w} ← sphere()")
def assign_sphere(context, var):
    context.variables[var] = sphere()


@when("{var:w} ← intersect({sphere_var:w}, {ray_var:w})")
def assign_intersect(context, var, sphere_var, ray_var):
    s = context.variables[sphere_var]
    r = context.variables[ray_var]
    context.variables[var] = intersect(s, r)


@then("{var:w}[{index:d}] = {value:g}")
def check_index(context, var, index, value):
    variable = context.variables[var]
    assert variable[index] == value


@when("set_transform({sphere_object:w}, {transform:w})")
def set_transform_1(context, sphere_object, transform):
    s = context.variables[sphere_object]
    t = context.variables[transform]
    s.set_transform(t)


@when("set_transform({sphere_object:w}, {transform:w}({args}))")
def set_transform_2(context, sphere_object, transform, args):
    s = context.variables[sphere_object]
    if transform == "scaling":
        transformation = scaling
    elif transform == "translation":
        transformation = translation
    else:
        raise ValueError(f"Transformation function {transform} not recognized")

    arguments = [float(x) for x in args.split(",")]
    t = transformation(*arguments)
    s.set_transform(t)
