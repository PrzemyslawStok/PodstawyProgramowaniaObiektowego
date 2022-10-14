class Square():
    def __init__(self, size: float):
        self.a = size

    def print(self):
        print(f"kwadrat o boku: {self.a}, powierzchnia: {self.area()}")

    def area(self) -> float:
        return self.a * self.a

    def __add__(self, other):
        newSize = self.a + other.a
        return Square(newSize)
