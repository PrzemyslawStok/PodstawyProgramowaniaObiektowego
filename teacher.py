import numpy as np


class Teacher():
    def __init__(self, name="", surname=""):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Teacher<Imię: {self.name} Nazwisko: {self.surname}>"
