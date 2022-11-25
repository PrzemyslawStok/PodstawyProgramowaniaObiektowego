from Figures2D.circle import Circle
from Figures3D.Pyramid import Pyramid


class Cone(Pyramid):
    def __init__(self, r: float, h: float):
        self.name = "Cone"
        self.base = Circle(r)
        super().__init__(self.base, h, name=self.name)
