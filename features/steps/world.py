from behave import given, then, when
from src.world import World, default_world


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
def assign_default_world(context, var):
    context.variables[var] = default_world()


@then(u"{world:w} contains {an_object:w}")
def check_world(context, world, an_object):
    w = context.variables[world]
    obj = context.variables[an_object]
    assert obj in w.objects
