from dataclasses import dataclass
from src.matrix import Matrix, identity


@dataclass
class Camera:
    hsize: float
    vsize: float
    field_of_view: float
    transform: Matrix = identity(4)
