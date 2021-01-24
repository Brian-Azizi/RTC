def approximately_equals(x: float, y: float) -> bool:
    EPSILON = 0.00001
    return abs(x - y) < EPSILON


def is_number(s):
    try:
        float(s)
        return True
    except (ValueError, TypeError):
        return False


def clamp(n, smallest, largest):
    return max(smallest, min(n, largest))
