class SerVivo:
    def __init__(self, nombre):
        self.nombre = nombre


class Animal(SerVivo):
    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.edad = edad


class Mamifero(Animal):
    def __init__(self, nombre, edad, pelo):
        super().__init__(nombre, edad)
        self.pelo = pelo


class Felino(Mamifero):
    def __init__(self, nombre, edad, pelo, garras):
        super().__init__(nombre, edad, pelo)
        self.garras = garras


class Gato(Felino):
    def __init__(self, nombre, edad, pelo, garras):
        super().__init__(nombre, edad, pelo, garras)


class Leon(Felino):
    def __init__(self, nombre, edad, pelo, garras):
        super().__init__(nombre, edad, pelo, garras)


class Roedor(Mamifero):
    def __init__(self, nombre, edad, pelo, dientes):
        super().__init__(nombre, edad, pelo)
        self.dientes = dientes


class Raton(Roedor):
    def __init__(self, nombre, edad, pelo, dientes):
        super().__init__(nombre, edad, pelo, dientes)


class Reptil(Animal):
    def __init__(self, nombre, edad, escamas):
        super().__init__(nombre, edad)
        self.escamas = escamas


class Vibora(Reptil):
    def __init__(self, nombre, edad, escamas, venenosa):
        super().__init__(nombre, edad, escamas)
        self.venenosa = venenosa


class Anfibio(Animal):
    def __init__(self, nombre, edad, piel_humeda):
        super().__init__(nombre, edad)
        self.piel_humeda = piel_humeda


class Rana(Anfibio):
    def __init__(self, nombre, edad, piel_humeda, salta):
        super().__init__(nombre, edad, piel_humeda)
        self.salta = salta


class Planta(SerVivo):
    def __init__(self, nombre, color):
        super().__init__(nombre)
        self.color = color


class Flor(Planta):
    def __init__(self, nombre, color, aroma):
        super().__init__(nombre, color)
        self.aroma = aroma


class Humano(Animal):
    def __init__(self, nombre, edad, nacionalidad):
        super().__init__(nombre, edad)
        self.nacionalidad = nacionalidad


class Nino(Humano):
    def __init__(self, nombre, edad, nacionalidad, escuela):
        super().__init__(nombre, edad, nacionalidad)
        self.escuela = escuela


class Adulto(Humano):
    def __init__(self, nombre, edad, nacionalidad, trabajo):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo = trabajo


class Anciano(Humano):
    def __init__(self, nombre, edad, nacionalidad, jubilado):
        super().__init__(nombre, edad, nacionalidad)
        self.jubilado = jubilado


gato = Gato("Michi", 3, "Suave", True)
leon = Leon("Simba", 8, "Corto", True)
raton = Raton("Jerry", 2, "Gris", True)
vibora = Vibora("Serpiente", 4, True, True)
rana = Rana("Rana", 1, True, True)
flor = Flor("Rosa", "Rojo", "Agradable")
nino = Nino("Pedro", 10, "Boliviana", "Colegio")
adulto = Adulto("Juan", 30, "Boliviana", "Ingeniero")
anciano = Anciano("Carlos", 70, "Boliviana", True)

print(gato.nombre, gato.edad, gato.pelo, gato.garras)
print(leon.nombre, leon.edad, leon.pelo, leon.garras)
print(raton.nombre, raton.edad, raton.pelo, raton.dientes)
print(vibora.nombre, vibora.edad, vibora.escamas, vibora.venenosa)
print(rana.nombre, rana.edad, rana.piel_humeda, rana.salta)
print(flor.nombre, flor.color, flor.aroma)
print(nino.nombre, nino.edad, nino.nacionalidad, nino.escuela)
print(adulto.nombre, adulto.edad, adulto.nacionalidad, adulto.trabajo)
print(anciano.nombre, anciano.edad, anciano.nacionalidad, anciano.jubilado)
