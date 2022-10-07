import numpy as np


class Student():
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.id = np.random.randint(0, 1000)

    def print(self):
        print(f"Imię: {self.name} Nazwisko: {self.surname}, id: {self.id}")
