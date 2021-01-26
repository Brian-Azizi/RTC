from typing import List, Iterable


class Object:
    pass


class Intersection:
    t: float
    the_object: Object

    def __init__(self, t: float, the_object: Object):
        self.t = t
        self.the_object = the_object


Intersections = List[Intersection]


def intersections(*args: Intersection) -> Intersections:
    return list(args)
