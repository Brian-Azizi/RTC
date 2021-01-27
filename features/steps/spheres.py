from behave import given, then, when
from typing import Callable, List
from src.spheres import Sphere, intersect, normal_at
from src.transformations import scaling, translation, rotation_z
from src.tuple import normalize, point
from src.matrix import Matrix


@given("{var:w} ← sphere()")
def assign_sphere(context, var):
    context.variables[var] = Sphere()


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
@given("set_transform({sphere_object:w}, {transform:w})")
def set_transform_1(context, sphere_object, transform):
    s = context.variables[sphere_object]
    t = context.variables[transform]
    s.set_transform(t)


def parse_transform(transform_string: str, args_string: str) -> Matrix:
    if transform_string == "scaling":
        transformation = scaling  # type: Callable[..., Matrix]
    elif transform_string == "translation":
        transformation = translation
    elif transform_string == "rotation_z":
        transformation = rotation_z
    else:
        raise ValueError(f"Transformation function {transform_string} not recognized")

    arguments = [float(x) for x in args_string.split(",")]
    return transformation(*arguments)


@when("set_transform({sphere_object:w}, {transform:w}({args}))")
@given("set_transform({sphere_object:w}, {transform:w}({args}))")
def set_transform_2(context, sphere_object, transform, args):
    s = context.variables[sphere_object]
    t = parse_transform(transform, args)

    s.set_transform(t)


@given("{var:w} ← {transform_1:w}({args_1}) * {transform_2:w}({args_2})")
def assign_transformation(context, var, transform_1, args_1, transform_2, args_2):
    t_1 = parse_transform(transform_1, args_1)
    t_2 = parse_transform(transform_2, args_2)
    context.variables[var] = t_1 * t_2


@when("{var:w} ← normal_at({obj_var:w}, point({x:g}, {y:g}, {z:g}))")
def assign_normal(context, var, obj_var, x, y, z):
    the_object = context.variables[obj_var]
    context.variables[var] = normal_at(the_object, point(x, y, z))


@then("{var_1:w} = normalize({var_2:w})")
def check_normal(context, var_1, var_2):
    variable_1 = context.variables[var_1]
    variable_2 = context.variables[var_2]
    assert variable_1 == normalize(variable_2)
