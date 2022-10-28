import numpy as np

from person import Person

class Student(Person):
    def __init__(self, name="", surname=""):
        super().__init__(name, surname)

        self.id = np.random.randint(0, 1000)

    def __str__(self):
        return f"Student<Imię: {self.name} Nazwisko: {self.surname}, id: {self.id}>"
