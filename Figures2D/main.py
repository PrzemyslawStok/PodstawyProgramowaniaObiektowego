from Figures2D.circle import Circle
from Figures2D.square import Square

if __name__ == "__main__":
    square = Square(a=10)
    circle = Circle()

    figures_list = []
    figures_list.append(square)
    figures_list.append(circle)

    for figure in figures_list:
        print(figure)
