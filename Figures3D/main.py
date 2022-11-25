from Figures3D.Cone import Cone
from Figures3D.Cube import Cube
from Figures3D.Cylinder import Cylinder
from Figures3D.Figure3D import Figure3D

if __name__ == "__main__":
    cylinder = Cylinder(r=1, h=1)
    cone = Cone(r=1, h=1)
    cube = Cube(a=5)

    figure3d_list: list[Figure3D] = []
    figure3d_list.append(cylinder)
    figure3d_list.append(cone)
    figure3d_list.append(cube)

    print(Figure3D.info())

    for figure3d in figure3d_list:
        print(f"Objętość {figure3d.name} wynosi: {figure3d.volume()}")
