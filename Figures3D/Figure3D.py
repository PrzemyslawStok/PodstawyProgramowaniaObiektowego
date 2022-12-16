from Figures2D.figure2D import Figure2D


class Figure3D:
    no = 0
    figuresList = []

    def __init__(self, name: str):
        self.name = name
        Figure3D.no = Figure3D.no + 1
        self.private_no = Figure3D.no

    def volume(self):
        pass

    @staticmethod
    def info():
        return f"info: figure3d, liczba figur wynosi: {Figure3D.no}"

    @staticmethod
    def getFiguresList():
        pass
