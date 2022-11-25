from Figures2D.figure2D import Figure2D
from Figures2D.square import Square
from Figures3D.Prism import Prism


class Cube(Prism):
    def __init__(self, a: float):
        self.name = "Cube"
        self.a = a
        self.base = Square(a=self.a)
        super().__init__(base=self.base, h=a, name=self.name)
