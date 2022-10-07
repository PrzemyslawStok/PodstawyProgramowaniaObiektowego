from square import Square
from student import Student

def students():
    print("Programowanie obiektowe")

    students = []

    for i in range(100):
        students.append(Student(f"Przemysław{i}", f"Stokłosa_{i}"))

    for student in students:
        student.print()


if __name__ == '__main__':
    kwadrat = Square(100.0)
    kwadrat.print()

    print(f"pole powierzchni: {kwadrat.area()}")
