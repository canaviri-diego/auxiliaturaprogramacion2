class Animal:
    def __init__(self, edad, peso, especie):
        self._edad = edad
        self._peso = peso
        self._especie = especie

    def respirar(self):
        print(f"{self._especie} toma oxigeno para vivir")

    def mover(self):
        print(f"{self._especie} se desplaza de un lugar a otro")

    def mostrar(self):
        print(f"Especie: {self._especie} | Edad: {self._edad} anios | Peso: {self._peso} kg")

class Terrestre(Animal):
    def __init__(self, edad, peso, especie, patas, dieta):
        super().__init__(edad, peso, especie)
        self._patas = patas
        self._dieta = dieta

    def correr(self):
        print(f"{self._especie} corre sobre sus {self._patas} patas")

    def cavar(self):
        print(f"{self._especie} cava la tierra buscando refugio")

    def respirar(self):
        super().respirar()
        print("Respira aire con sus pulmones por la nariz")

    def mover(self):
        print(f"{self._especie} camina y corre sobre la tierra")

    def mostrar(self):
        super().mostrar()
        print(f"Tipo: Terrestre | Patas: {self._patas} | Dieta: {self._dieta}")

class Acuatico(Animal):
    def __init__(self, edad, peso, especie, tipo_agua, profundidad):
        super().__init__(edad, peso, especie)
        self._tipo_agua = tipo_agua
        self._profundidad = profundidad

    def nadar(self):
        print(f"{self._especie} nada en agua {self._tipo_agua}")

    def bucear(self):
        print(f"{self._especie} bucea hasta {self._profundidad} metros")

    def respirar(self):
        super().respirar()
        print("Respira el oxigeno disuelto en el agua con sus branquias")

    def mover(self):
        print(f"{self._especie} se desplaza nadando con sus aletas")

    def mostrar(self):
        super().mostrar()
        print(f"Tipo: Acuatico | Agua: {self._tipo_agua} | Profundidad maxima: {self._profundidad} m")

class Aereo(Animal):
    def __init__(self, edad, peso, especie, envergadura, altitud):
        super().__init__(edad, peso, especie)
        self._envergadura = envergadura
        self._altitud = altitud

    def volar(self):
        print(f"{self._especie} vuela con alas de {self._envergadura} m de envergadura")

    def aterrizar(self):
        print(f"{self._especie} desciende y aterriza suavemente")

    def respirar(self):
        super().respirar()
        print("Respira con pulmones y sacos de aire que le dan eficiencia en altura")

    def mover(self):
        print(f"{self._especie} se desplaza volando hasta {self._altitud} metros de altura")

    def mostrar(self):
        super().mostrar()
        print(f"Tipo: Aereo | Envergadura: {self._envergadura} m | Altitud maxima: {self._altitud} m")

leon = Terrestre(5, 190.5, "Leon", 4, "carnivoro")
delfin = Acuatico(8, 150.0, "Delfin", "salada", 300)
condor = Aereo(12, 11.5, "Condor", 3.0, 5500)

for a in (leon, delfin, condor):
    a.mostrar()
    a.respirar()
    a.mover()
    print()

leon.correr()
leon.cavar()
delfin.nadar()
delfin.bucear()
condor.volar()
condor.aterrizar()
