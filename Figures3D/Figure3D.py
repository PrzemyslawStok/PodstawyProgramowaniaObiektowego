from Figures2D.figure2D import Figure2D

class Figure3D:
    def __init__(self, base: Figure2D, h: float, name: str = None):
        self.name = name
        self.base = base
        self.h = h

    def volume(self):
        return self.base.area() * self.h
