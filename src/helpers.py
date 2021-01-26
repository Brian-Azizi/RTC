from typing import Union, Any

Num = Union[int, float]


SHORT_EPSILON = 0.00001
LONG_EPSILON = 0.00000000001


def approximately_equals(x: Num, y: Num) -> bool:
    return abs(x - y) < SHORT_EPSILON


def equals(x: Num, y: Num) -> bool:
    return abs(x - y) < LONG_EPSILON


def is_number(s: Any) -> bool:
    try:
        float(s)
        return True
    except (ValueError, TypeError):
        return False


def clamp(n: Num, smallest: Num, largest: Num) -> Num:
    return max(smallest, min(n, largest))
