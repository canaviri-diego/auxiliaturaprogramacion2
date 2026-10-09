from abc import ABC, abstractmethod
from math import pi, sqrt

class Figura(ABC):
    def __init__(self, color):
        self._color = color

    @abstractmethod
    def obtenerArea(self):
        pass

    def getColor(self):
        return self._color

class Cuadrado(Figura):
    def __init__(self, color, lado):
        super().__init__(color)
        self.__lado = lado

    def obtenerArea(self):
        return self.__lado ** 2

    def __str__(self):
        return f"Cuadrado | color: {self._color} | lado: {self.__lado} | area: {self.obtenerArea():.2f}"

class Triangulo(Figura):
    def __init__(self, color, lado1, lado2, lado3):
        super().__init__(color)
        self.__lado1 = lado1
        self.__lado2 = lado2
        self.__lado3 = lado3

    def obtenerArea(self):
        s = (self.__lado1 + self.__lado2 + self.__lado3) / 2
        return sqrt(s * (s - self.__lado1) * (s - self.__lado2) * (s - self.__lado3))

    def __str__(self):
        return f"Triangulo | color: {self._color} | lados: {self.__lado1}, {self.__lado2}, {self.__lado3} | area: {self.obtenerArea():.2f}"

class Redondo(Figura):
    def __init__(self, color, radio):
        super().__init__(color)
        self.__radio = radio

    def obtenerArea(self):
        return pi * self.__radio ** 2

    def __str__(self):
        return f"Redondo | color: {self._color} | radio: {self.__radio} | area: {self.obtenerArea():.2f}"

def colorMayorArea(cuad, tri):
    if cuad.obtenerArea() > tri.obtenerArea():
        print(f"La figura con mayor area es el Cuadrado, color: {cuad.getColor()}")
    elif tri.obtenerArea() > cuad.obtenerArea():
        print(f"La figura con mayor area es el Triangulo, color: {tri.getColor()}")
    else:
        print("Ambas figuras tienen la misma area")

c1 = Cuadrado("rojo", 4)
c2 = Cuadrado("azul", 5)
t1 = Triangulo("verde", 3, 4, 5)
t2 = Triangulo("amarillo", 6, 7, 8)
r1 = Redondo("negro", 2)
r2 = Redondo("blanco", 3)

for f in (c1, c2, t1, t2, r1, r2):
    print(f)

print()
colorMayorArea(c1, t1)
colorMayorArea(c2, t2)
