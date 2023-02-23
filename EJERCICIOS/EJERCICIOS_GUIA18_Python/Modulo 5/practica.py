class Loro:
    def __init__(self, nombre, sexo, edad):
        self.nombre = nombre
        self.sexo = sexo
        self.edad = edad

    def palabras(self):
        print(f"{self.nombre} dice 'Hola cómo va?!'")

loro1 = Loro("Pomelo", "hembra", 10)
loro2 = Loro("Lola", "hembra", 13) 

print(loro1.nombre, loro1.sexo)
print(loro2.nombre, loro2.sexo)

loro1.palabras()
loro2.palabras()
        