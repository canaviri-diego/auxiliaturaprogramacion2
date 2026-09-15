class Auto:
    def __init__(self, marca="Toyota", gasolina=0, color="Blanco"):
        self.marca = marca
        self.gasolina = gasolina
        self.color = color

    @classmethod
    def crear(cls, marca, gasolina):
        return cls(marca, gasolina, "Blanco")

    def __pos__(self):
        self.gasolina += 5
        return self

    def __add__(self, color):
        self.color = color
        return self

    def __sub__(self, otro):
        return self.gasolina + otro.gasolina

    def mostrar(self):
        print("Marca:", self.marca)
        print("Gasolina:", self.gasolina, "litros")
        print("Color:", self.color)


auto1 = Auto("Toyota", 20, "Rojo")
auto2 = Auto.crear("Nissan", 30)

print("AUTO 1")
auto1.mostrar()

print("\nAUTO 2")
auto2.mostrar()

+auto1
+auto2

auto1 + "Azul"

total = auto1 - auto2

print("\nDESPUES DE LOS OPERADORES")

print("AUTO 1")
auto1.mostrar()

print("\nAUTO 2")
auto2.mostrar()

print("\nTotal de gasolina:", total, "litros")
