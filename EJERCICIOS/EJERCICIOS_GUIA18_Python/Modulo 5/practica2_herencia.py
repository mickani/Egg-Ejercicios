class Persona:
    def __init__(self, nombres, apellidos):
        self.nombres = nombres
        self.apellidos = apellidos

    def nombre_completo(self):
        return f"{self.nombres}, {self.apellidos}"

class Cliente(Persona): 
    def __init__(self, nombres, apellidos, celu):
        super().__init__(nombres, apellidos)
        self.celu: str = celu

    def nombre_completo(self):
        return f"{self.nombres.upper()}, {self.apellidos.upper()}"

    def saludar(self):
        return f"Hola {self.nombres}"

class Usuario(Cliente):
    def __init__(self, nombres, apellidos, celu):
        super().__init__(nombres, apellidos, celu)
        self.contrasenia = self.generar_contrasenia()

    def generar_contrasenia(self):
        len_celu=len(self.celu)
        return self.nombres[0:6] + self.celu[len_celu-2:len_celu]

if __name__ == "__main__":
    perso1 = Persona(nombres="Micaela", apellidos="Bossio")
    print(perso1.nombre_completo())   

    cliente1= Cliente(nombres="Pomelo", apellidos="Pomelero", celu="12334")
    print(cliente1.nombre_completo(), "Celu:",cliente1.celu)

    usuario1 = Usuario("Facundo", "Peralta", "1234567891")
    print(usuario1.nombre_completo(),"- cel:", usuario1.celu,"- pass:", usuario1.generar_contrasenia())