class Auto:
    def __init__(self, marca, modelo, anio, kilometraje, color="Blanco"):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.kilometraje = kilometraje
        self.color = color

    def mostrar_kilometraje(self):
        metros = self.kilometraje * 1000
        print(f"Kilometraje: {self.kilometraje} km ({metros} m)")

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color

auto1 = Auto("Toyota", "Corolla", 2020, 15000)
auto2 = Auto("Hyundai", "Accent", 2019, 25000, "Negro")
auto1.cambiar_color("Rojo")
auto2.cambiar_color("Azul")
auto1.mostrar_kilometraje()
auto2.mostrar_kilometraje()
