from behave import given, then, when
from src.world import World, default_world, intersect_world, shade_hit, color_at


@given(u"{var:w} ← world()")
def assign_world(context, var):
    context.variables[var] = World()


@then(u"{var:w} contains no objects")
def check_empty_world_1(context, var):
    world = context.variables[var]
    assert len(world.objects) == 0


@then(u"{var:w} has no light source")
def check_empty_world_2(context, var):
    world = context.variables[var]
    assert world.light is None


@when(u"{var:w} ← default_world()")
@given(u"{var:w} ← default_world()")
def assign_default_world(context, var):
    context.variables[var] = default_world()


@then(u"{world:w} contains {an_object:w}")
def check_world(context, world, an_object):
    w = context.variables[world]
    obj = context.variables[an_object]
    assert obj in w.objects


@when(u"{var:w} ← intersect_world({world_var:w}, {ray_var:w})")
def assign_intersect_world(context, var, world_var, ray_var):
    world = context.variables[world_var]
    ray = context.variables[ray_var]
    context.variables[var] = intersect_world(world, ray)


@given(u"{var:w} ← object {num:d} in {world_var:w}")
def assign_shape(context, var, num, world_var):
    world = context.variables[world_var]
    context.variables[var] = world.objects[num - 1]


@when(u"{color_var:w} ← shade_hit({world_var:w}, {comps_var:w})")
def assign_shade_hit(context, color_var, world_var, comps_var):
    world = context.variables[world_var]
    comps = context.variables[comps_var]
    context.variables[color_var] = shade_hit(world, comps)


@when(u"{color_var:w} ← color_at({world_var:w}, {ray_var:w})")
def assign_color(context, color_var, world_var, ray_var):
    world = context.variables[world_var]
    ray = context.variables[ray_var]
    context.variables[color_var] = color_at(world, ray)


@given(u"{var:w}.{outer:w}.{inner:w} ← {val:g}")
def set_inner_attribute(context, var, outer, inner, val):
    variable = context.variables[var]
    setattr(getattr(variable, outer), inner, val)


@then(u"{exp:w} = {var:w}.{outer:w}.{inner:w}")
def check_inner_attribute(context, exp, var, outer, inner):
    variable = context.variables[var]
    expected = context.variables[exp]
    assert expected == getattr(getattr(variable, outer), inner)
