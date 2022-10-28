class Line:
    def __init__(self, length: float):
        self.length = length

    def __add__(self, other):
        return Line(self.length + other.length)

    def print(self):
        print(f"Długość lini wynosi: {self.length}")
