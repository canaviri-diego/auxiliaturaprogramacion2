class Anuncio:
    def __init__(self, numero, precio):
        self.__numero = numero
        self.__precio = precio

    def getPrecio(self):
        return self.__precio

    def setPrecio(self, precio):
        self.__precio = precio


class Artista:
    def __init__(self, nombre, ci, aniosExperiencia):
        self.__nombre = nombre
        self.__ci = ci
        self.__aniosExperiencia = aniosExperiencia

    def getNombre(self):
        return self.__nombre

    def getAniosExperiencia(self):
        return self.__aniosExperiencia


class Obra:
    def __init__(self, titulo, material, nombre1, ci1, aniosExperiencia1, nombre2, ci2, aniosExperiencia2, anuncio):
        self.__titulo = titulo
        self.__material = material
        self.artista1 = Artista(nombre1, ci1, aniosExperiencia1)
        self.artista2 = Artista(nombre2, ci2, aniosExperiencia2)
        self.anuncio = anuncio

    def getA1(self):
        return self.artista1

    def getA2(self):
        return self.artista2

    def getB(self):
        return self.anuncio

    def setB(self, anuncio):
        self.anuncio = anuncio


class Pintura(Obra):
    def __init__(self, titulo, material, nombre1, ci1, aniosExperiencia1, nombre2, ci2, aniosExperiencia2, anuncio, genero):
        super().__init__(titulo, material, nombre1, ci1, aniosExperiencia1, nombre2, ci2, aniosExperiencia2, anuncio)
        self.__genero = genero


anuncio1 = Anuncio(1, 300)

p1 = Pintura("Paisaje", "Oleo", "Hernan", 1234567, 10, "Carlos", 3456784, 2, anuncio1, "Oculto")
p2 = Pintura("La Noche", "Acuarela", "Juan", 4567895, 5, "Angel", 1546347, 3, None, "Realismo")

mayor = p1.getA1()
if p1.getA2().getAniosExperiencia() > mayor.getAniosExperiencia():
    mayor = p1.getA2()
if p2.getA1().getAniosExperiencia() > mayor.getAniosExperiencia():
    mayor = p2.getA1()
if p2.getA2().getAniosExperiencia() > mayor.getAniosExperiencia():
    mayor = p2.getA2()
print("Artista con mayor experiencia:", mayor.getNombre())

anuncio2 = Anuncio(2, 700)
p2.setB(anuncio2)
total = p1.getB().getPrecio() + p2.getB().getPrecio()
print("Monto total de ventas:", total)
