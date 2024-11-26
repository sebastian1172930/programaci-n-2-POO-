#POLIMORFISMO con método
import math

class Triangulo:
    def __init__(self):
        self.l1 = float(input("Ingrese lado 1: "))
        self.l2 = float(input("Ingrese lado 2: "))
        self.l3 = float(input("Ingrese lado 3: "))

    def Peri(self):
        print("El perímetro de la figura es: ", self.l1 + self.l2 + self.l3)

    def Area(self):
        s = (self.l1 + self.l2 + self.l3) / 2
        area = (s * (s - self.l1) * (s - self.l2) * (s - self.l3)) ** 0.5
        print("El área de la figura es: ", area)

class Rectangulo:
    def __init__(self):
        self.l1 = float(input("Ingrese lado 1: "))
        self.l2 = float(input("Ingrese lado 2: "))

    def Peri(self):
        print("El perímetro de la figura es: ", 2 * (self.l1 + self.l2))

    def Area(self):
        area = self.l1 * self.l2
        print("El área de la figura es: ", area)

class Circulo:
    def __init__(self):
        self.r = float(input("Ingrese el radio: "))

    def Peri(self):
        peri = 2 * math.pi * self.r
        print("El perímetro de la figura es: ", peri)

    def Area(self):
        area = math.pi * (self.r ** 2)
        print("El área de la figura es: ", area)









            
            
