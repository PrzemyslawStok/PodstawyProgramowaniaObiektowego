import numpy as np


class Person():
    def __init__(self, name="", surname=""):
        self.name = name
        self.surname = surname
        self.weight = np.random.randint(70, 100)

    def __str__(self):
        return f"Imię: {self.name} Nazwisko: {self.surname}"

    def __call__(self, *args, **kwargs):
        return self.name

    def print(self):
        print(f"weight: {self.weight}")


