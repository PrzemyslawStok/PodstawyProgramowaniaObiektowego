from person import Person
from student import Student
from teacher import Teacher

if __name__ == "__main__":
    student0 = Student(name="Przemysław", surname="Stokłosa")
    teacher0 = Teacher(name="Przemysław", surname="Stokłosa")

    print(student0)
    print(teacher0)

    student0.print()
    teacher0.print()

    teacher0.f0()
    #student0.f0()

    print(student0())
