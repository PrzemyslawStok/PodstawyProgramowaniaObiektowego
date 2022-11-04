from Figures2D.circle import Circle
from Figures2D.figure2D import Figure2D
from Figures2D.square import Square

if __name__ == "__main__":
    square = Square(a=10)
    circle = Circle(r=5)

    figures_list: list[Figure2D] = []

    figures_list.append(square)
    figures_list.append(circle)
    figures_list.append(Square(1))

    for figure in figures_list:
        print(figure)
