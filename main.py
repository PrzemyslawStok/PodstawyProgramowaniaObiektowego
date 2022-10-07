from student import Student
import numpy as np

if __name__ == '__main__':
    print("Programowanie obiektowe")

    students = []

    for i in range(100):
        students.append(Student(f"Przemysław{i}", f"Stokłosa_{i}"))

    for student in students:
        student.print()
