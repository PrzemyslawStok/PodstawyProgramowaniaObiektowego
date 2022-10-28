from person import Person
from student import Student
from teacher import Teacher


def add_students(students_list: list, no_students: int):
    for i in range(no_students):
        students_list.append(Student("Piotr", f"Stokłosa_{i}"))


def add_teachers(teachers_list: list, no_teachers: int):
    for i in range(no_teachers):
        teachers_list.append(Teacher("Przemyslaw", f"Stokłosa_{i}"))


def printUniversity(university_name: str, students_list: list, teachers_list: list):
    print(f"Nazwa uczelni: {university_name}")
    print("Lista nauczycieli: ")

    for teacher in teachers_list:
        print(teacher)

    print("Lista studentów: ")

    for student in students_list:
        print(student)


if __name__ == "__main__":
    university_name = "WSIZ"
    no_students = 10
    no_teachers = 2

    students_list = []
    teachers_list = []

    add_students(students_list, no_students)
    add_teachers(teachers_list, no_teachers)

    printUniversity(university_name, students_list, teachers_list)
