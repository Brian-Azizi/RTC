from __future__ import annotations
from typing import List, Iterable, Optional
from src.matrix import Matrix


class Object:
    transform: Matrix


class Intersection:
    t: float
    the_object: Object

    def __init__(self, t: float, the_object: Object):
        self.t = t
        self.the_object = the_object

    def __lt__(self, other: Intersection) -> bool:
        return self.t < other.t


Intersections = List[Intersection]


def intersections(*args: Intersection) -> Intersections:
    result = list(args)
    result.sort()
    return result


def hit(xs: Intersections) -> Optional[Intersection]:
    for intersection in xs:
        if intersection.t >= 0:
            return intersection

    return None
