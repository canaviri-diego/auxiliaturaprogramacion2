class Documento:
    def __init__(self, titulo, autores, editorial, anio):
        self.titulo = titulo
        self.autores = list(autores)
        self.editorial = editorial
        self.anio = anio

    def copiar(self):
        return Documento(self.titulo, self.autores, self.editorial, self.anio)

    def __str__(self):
        return f"{self.titulo} | {', '.join(self.autores)} | {self.editorial} | {self.anio}"

class Libro(Documento):
    def copiar(self):
        return Libro(self.titulo, self.autores, self.editorial, self.anio)

    def __str__(self):
        return "Libro: " + super().__str__()

class Revista(Documento):
    def __init__(self, titulo, autores, editorial, anio, volumen, numero, mes):
        super().__init__(titulo, autores, editorial, anio)
        self.volumen = volumen
        self.numero = numero
        self.mes = mes

    def copiar(self):
        return Revista(self.titulo, self.autores, self.editorial, self.anio, self.volumen, self.numero, self.mes)

    def __str__(self):
        return f"Revista: {super().__str__()} | vol. {self.volumen} | num. {self.numero} | {self.mes}"

class DocumentoCD(Documento):
    def __init__(self, titulo, autores, editorial, anio, formato, licencia):
        super().__init__(titulo, autores, editorial, anio)
        self.formato = formato
        self.licencia = licencia

    def copiar(self):
        return DocumentoCD(self.titulo, self.autores, self.editorial, self.anio, self.formato, self.licencia)

    def __str__(self):
        return f"CD: {super().__str__()} | formato: {self.formato} | licencia: {self.licencia}"

class RevistaInvestigacion(Revista):
    def __init__(self, titulo, autores, editorial, anio, volumen, numero, mes, campo):
        super().__init__(titulo, autores, editorial, anio, volumen, numero, mes)
        self.campo = campo

    def copiar(self):
        return RevistaInvestigacion(self.titulo, self.autores, self.editorial, self.anio, self.volumen, self.numero, self.mes, self.campo)

    def __str__(self):
        return f"{super().__str__()} | campo: {self.campo}"

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.docs = []

    def agregar(self, doc):
        self.docs.append(doc)

    def cantRevistas(self):
        return sum(1 for d in self.docs if isinstance(d, Revista))

    def cantDocs(self):
        return len(self.docs)

    def copiar(self):
        c = Biblioteca(self.nombre)
        c.docs = [d.copiar() for d in self.docs]
        return c

    def mostrar(self):
        print(f"Biblioteca {self.nombre} ({self.cantDocs()} documentos, {self.cantRevistas()} revistas)")
        for d in self.docs:
            print("  " + str(d))

def quienTieneMas(a, b):
    if a.cantRevistas() > b.cantRevistas():
        print(f"Mas revistas: {a.nombre} ({a.cantRevistas()})")
    elif b.cantRevistas() > a.cantRevistas():
        print(f"Mas revistas: {b.nombre} ({b.cantRevistas()})")
    else:
        print(f"Ambas tienen la misma cantidad de revistas ({a.cantRevistas()})")
    if a.cantDocs() > b.cantDocs():
        print(f"Mas documentos: {a.nombre} ({a.cantDocs()})")
    elif b.cantDocs() > a.cantDocs():
        print(f"Mas documentos: {b.nombre} ({b.cantDocs()})")
    else:
        print(f"Ambas tienen la misma cantidad de documentos ({a.cantDocs()})")

def trasladar(a, b):
    for origen in (a, b):
        for d in origen.docs[:]:
            if isinstance(d, Revista) and origen is not a:
                origen.docs.remove(d)
                a.docs.append(d)
            elif isinstance(d, Libro) and origen is not b:
                origen.docs.remove(d)
                b.docs.append(d)

b1 = Biblioteca("Central")
b2 = Biblioteca("Informatica")

b1.agregar(Libro("Programacion en Python", ["Mark Lutz"], "OReilly", 2013))
b1.agregar(Revista("Computer World", ["Equipo Editorial"], "IDG", 2024, 12, 3, "Marzo"))
b1.agregar(DocumentoCD("Linux Total", ["Varios"], "Tecno", 2010, "CD-ROM", "GPL"))
b1.agregar(Libro("Estructuras de Datos", ["Weiss"], "Pearson", 2012))

b2.agregar(Libro("Algoritmos", ["Cormen", "Leiserson"], "MIT Press", 2009))
b2.agregar(RevistaInvestigacion("Revista de IA", ["Lopez"], "UMSA", 2025, 4, 1, "Junio", "Inteligencia Artificial"))
b2.agregar(Revista("PC Magazine", ["Redaccion"], "Ziff", 2023, 40, 7, "Julio"))
b2.agregar(DocumentoCD("Office Suite", ["Microsoft"], "MS", 2007, "DVD", "Comercial"))
b2.agregar(Libro("Bases de Datos", ["Date"], "Addison", 2004))
b2.agregar(Libro("Redes", ["Tanenbaum"], "Pearson", 2011))

print("INICIAL")
b1.mostrar()
b2.mostrar()
print()
quienTieneMas(b1, b2)

trasladar(b1, b2)
print()
print("DESPUES DE TRASLADAR")
b1.mostrar()
b2.mostrar()
print()
quienTieneMas(b1, b2)

copia1 = b1.copiar()
copia2 = b2.copiar()
print()
print("COPIAS DE SEGURIDAD")
copia1.mostrar()
copia2.mostrar()
print()
print("Copias independientes:", all(x is not y for x, y in zip(b1.docs, copia1.docs)) and all(x is not y for x, y in zip(b2.docs, copia2.docs)))
