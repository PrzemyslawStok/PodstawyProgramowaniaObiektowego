import numpy as np

class Person():
    def __init__(self, name="", surname=""):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Imię: {self.name} Nazwisko: {self.surname}"
