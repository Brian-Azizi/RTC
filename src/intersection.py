from typing import List, Iterable
from src.spheres import Sphere


class Intersection:
    t: float
    the_object: Sphere

    def __init__(self, t: float, the_object: Sphere):
        self.t = t
        self.the_object = the_object


def intersections(*args: Intersection) -> List[Intersection]:
    return list(args)