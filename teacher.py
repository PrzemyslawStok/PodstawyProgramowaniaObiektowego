import numpy as np

from person import Person


class Teacher(Person):
    def __init__(self, name="", surname=""):
        super().__init__(name, surname)

    def __str__(self):
        return f"Teacher<Imię: {self.name} Nazwisko: {self.surname}>"
