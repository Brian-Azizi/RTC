from dataclasses import dataclass


@dataclass(frozen=True)
class Tuple:
    x: float
    y: float
    z: float
    w: float
