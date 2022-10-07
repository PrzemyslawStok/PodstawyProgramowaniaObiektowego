class Square():
    def __init__(self, size: float):
        self.size = size

    def print(self):
        print(f"kwadrat o boku: {self.size}")

    def area(self) -> float:
        return self.size * self.size

    def __add__(self, other):
        newSize = self.size + other.size
        return Square(newSize)
