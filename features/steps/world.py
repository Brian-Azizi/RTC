from behave import given, then, when
from src.world import World, default_world, intersect_world


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