from Figures2D.figure2D import Figure2D
from Figures3D.Figure3D import Figure3D

class Pyramid(Figure3D):
    def __init__(self, base: Figure2D, h: float, name: str = None):
        self.name = name
        self.base = base
        self.h = h

    def volume(self):
        return 1.0 / 3.0 * self.base.area() * self.h
