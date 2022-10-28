from University.student import Student


class University:
    def __init__(self, university_name, no_teachers, no_students):
        self.university_name = university_name
        self.no_students = no_students
        self.no_teachers = no_teachers

        self.students_list = []
        self.teachers_list = []

        self.add_students()
        self.add_teachers()

    def add_students(self):
        for i in range(self.no_students):
            self.students_list.append(Student("Piotr", f"Stokłosa_{i}"))

    def add_teachers(self):
        pass

    def print(self):
        print(f"Nazwa uczelni: {self.university_name}")
        print("Lista nauczycieli: ")
