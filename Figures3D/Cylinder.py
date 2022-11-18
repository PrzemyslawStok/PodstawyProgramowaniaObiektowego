from Figures2D.circle import Circle
from Figures3D.Prism import Prism


class Cylinder(Prism):
    def __init__(self, r: float, h: float):
        self.name = "Cylinder"
        self.base = Circle(r)
        super().__init__(self.base, h)
