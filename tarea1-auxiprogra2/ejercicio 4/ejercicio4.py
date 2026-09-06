class Bus:
    def __init__(self, capacidad_total, pasajeros=0):
        self.capacidad_total = capacidad_total
        self.pasajeros = pasajeros
        self.recaudacion = 0.0

    def subir_pasajeros(self, x):
        disponibles = self.asientos_disponibles()
        if x <= disponibles:
            self.pasajeros += x
        else:
            print(f"No se pueden subir {x} pasajeros, solo quedan {disponibles} asientos.")
            self.pasajeros += disponibles

    def cobrar_pasaje(self, cantidad_pasajeros):
        costo = 1.50
        self.recaudacion += cantidad_pasajeros * costo

    def asientos_disponibles(self):
        return self.capacidad_total - self.pasajeros

    def mostrar_disponibles(self):
        print(f"Asientos disponibles: {self.asientos_disponibles()}")

mi_bus = Bus(capacidad_total=40)
mi_bus.subir_pasajeros(10)
mi_bus.cobrar_pasaje(10)
mi_bus.mostrar_disponibles()
