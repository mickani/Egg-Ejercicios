class Persona:
    def __init__(self, nombre: str):
        self._nombre = nombre

    @property
    def name(self):
        return self._nombre

    @name.getter
    def name(self):
        if self._nombre == "":
            print("No tengo nombre")
        else:
            print("mi nombre es", self._nombre)

    @name.setter
    def name(self, valor: str):
        if valor.strip() == "":
            raise ValueError("nombre vacío")
        self._nombre = valor
        print("tengo nuevo nombre")

    @name.deleter
    def name(self):
        print("has borrado mi nombre")
        self._nombre = ""  

# Ejecutar de a uno para entender...
p1 = Persona("Mica")
p1.name
p1.name = "Pomelo"
p1.name
del p1.name
p1.name
p1.name = "   "