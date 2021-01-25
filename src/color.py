from __future__ import annotations
from dataclasses import dataclass
from typing import Union
from src.helpers import approximately_equals


@dataclass(frozen=True)
class Color:
    red: float
    green: float
    blue: float

    def __add__(self, other: Color) -> Color:
        return Color(
            self.red + other.red,
            self.green + other.green,
            self.blue + other.blue,
        )

    def __radd__(self, other: Color) -> Color:
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __neg__(self) -> Color:
        return Color(-self.red, -self.green, -self.blue)

    def __sub__(self, other: Color) -> Color:
        return self + -other

    def __mul__(self, other: Union[float, int, Color]) -> Color:
        if isinstance(other, float) or isinstance(other, int):
            return Color(
                self.red * other,
                self.green * other,
                self.blue * other,
            )
        else:
            return Color(
                self.red * other.red,
                self.green * other.green,
                self.blue * other.blue,
            )

    def __rmul__(self, other: float) -> Color:
        return self * other

    def __truediv__(self, other: float) -> Color:
        return self * (1 / other)

    def approximately_equals(self, other: Color) -> bool:
        return (
            approximately_equals(self.red, other.red)
            and approximately_equals(self.green, other.green)
            and approximately_equals(self.blue, other.blue)
        )
