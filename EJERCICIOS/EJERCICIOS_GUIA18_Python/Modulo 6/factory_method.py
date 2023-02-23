from datetime import date


class Estudiante:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def clacular_edad(cls, nombre, año_nacimiento):
        '''Calcula la edad y la configura como un ojeto nuevo'''
        edad_calculada = date.today().year - año_nacimiento
        return cls(nombre=nombre, edad=edad_calculada)

    def mostrar(self):
        print(self.nombre + " tiene " + str(self.edad) + " años.") 

e1 = Estudiante("Bartolomeo", 30)
e1.mostrar()

# crea un nuevo objeto usando el patrón Factory Method
e2 = Estudiante.clacular_edad("Micaela",2000)
e2.mostrar()