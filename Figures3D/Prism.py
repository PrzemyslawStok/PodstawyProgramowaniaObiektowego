from Figures2D.figure2D import Figure2D
from Figures3D.Figure3D import Figure3D


class Prism(Figure3D):
    def __init__(self, base: Figure2D, h: float, name: str):
        super().__init__(name=name)
        self.name = name
        self.base = base
        self.h = h

    def volume(self):
        return self.base.area() * self.h
