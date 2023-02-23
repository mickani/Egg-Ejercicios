class Estudiante:
    # variable de clase
    nombre_escuela = "HomeSchooling"

    # método de instancia: constructor
    def __init__(self, nombre, edad):
        # variables de instancia
        self.nombre = nombre
        self.edad = edad

    # método de instancia
    def mostrar(self):
        # accede a las variables de instancia y a la variable de clase
        print("Estudiante:", self.nombre, self.edad, Estudiante.nombre_escuela)

    # método de instancia
    def cambiar_edad(self, nueva_edad):
        # modifica la variable de instancia
        self.edad = nueva_edad 

    # método clase 
    @classmethod
    def modificar_nombre_escuela(cls, nuevo_nombre):
        # modifica la variable de clase
        cls.nombre_escuela = nuevo_nombre

estudiante1 = Estudiante("Micaela", 31)
estudiante1.mostrar()
estudiante1.cambiar_edad(23)
estudiante1.modificar_nombre_escuela("Pomelandia")
estudiante1.mostrar()


      

