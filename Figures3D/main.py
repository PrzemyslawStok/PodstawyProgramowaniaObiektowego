from Figures3D.Cone import Cone
from Figures3D.Cylinder import Cylinder

if __name__ == "__main__":
    cylinder = Cylinder(r=1, h=1)
    stozek = Cone()

    print(f"Objętość {cylinder.name} wynosi: {cylinder.volume()}")
    print(f"Objętość {stozek.name} wynosi: {stozek.volume()}")
