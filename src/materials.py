from src.color import Color


class Material:
    color: Color
    ambient: float
    diffuse: float
    specular: float
    shininess: float

    def __init__(self) -> None:
        self.color = Color(1, 1, 1)
        self.ambient = 0.1
        self.diffuse = 0.9
        self.specular = 0.9
        self.shininess = 200.0