from typing import Union, Any

Num = Union[int, float]


EPSILON = 0.00001


def approximately_equals(x: Num, y: Num) -> bool:
    return abs(x - y) < EPSILON


def is_number(s: Any) -> bool:
    try:
        float(s)
        return True
    except (ValueError, TypeError):
        return False


def clamp(n: Num, smallest: Num, largest: Num) -> Num:
    return max(smallest, min(n, largest))
