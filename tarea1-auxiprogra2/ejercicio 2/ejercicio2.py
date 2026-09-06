class Computadora:
    def __init__(self, marca, procesador, ram, almacenamiento):
        self.marca = marca
        self.procesador = procesador
        self.ram = ram
        self.almacenamiento = almacenamiento

    def verificar_ram(self, x):
        return self.ram == x

    def mostrar_datos(self):
        print(f"Marca: {self.marca}, Procesador: {self.procesador}, RAM: {self.ram}GB, Almacenamiento: {self.almacenamiento}GB")

comp1 = Computadora("Asus", "Intel i7", 16, 512)
comp2 = Computadora(marca="HP", procesador="Ryzen 5", ram=8, almacenamiento=1024)
print(f"¿RAM de comp1 es igual a 16?: {comp1.verificar_ram(16)}")
if comp1.almacenamiento > comp2.almacenamiento:
    comp1.mostrar_datos()
else:
    comp2.mostrar_datos()
