from square import Square
from University.student import Student


def students():
    print("Programowanie obiektowe")

    students = []

    for i in range(100):
        students.append(Student(f"Przemysław{i}", f"Stokłosa_{i}"))

    for student in students:
        student.print()

def simpleGeometry():
    kwadrat1 = Square(10.0)
    kwadrat2 = Square(5.0)

    kwadrat1.print()

    kwadrat3 = kwadrat1 + kwadrat2

    kwadrat3.print()

    print(kwadrat1)
    print(kwadrat2)
    print(kwadrat3)

if __name__ == '__main__':
   students()
