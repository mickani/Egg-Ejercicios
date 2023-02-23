# __str__

# class Persona:
#     def __init__(self, nombre, apellido):
#         self.nombre = nombre
#         self.apellido = apellido

# class Persona:
#     def __init__(self, nombre, apellido):
#         self.nombre = nombre
#         self.apellido = apellido

#     def __str__(self):
#         return f"{self.nombre} {self.apellido}"


# persona = Persona("Michael", "Faraday")
# print(persona)

# --------------------------------------------------

# __repr__

# class Persona:
#     lista_personas: list["Persona"] = []
#     def __init__(self, nombre, apellido):
#         self.nombre = nombre
#         self.apellido = apellido
#         Persona.lista_personas.append(self)
    
#     def __str__(self) -> str:
#         return f"{self.nombre} {self.apellido}"

# class Persona:
#     lista_personas: list["Persona"] = []
#     def __init__(self, nombre, apellido):
#         self.nombre = nombre
#         self.apellido = apellido
#         Persona.lista_personas.append(self)
    
#     def __str__(self) -> str:
#         return f"{self.nombre} {self.apellido}"

#     def __repr__(self) -> str:
#         return f"{self.__class__.__name__}{self.__dict__}"    


# persona_1 = Persona("Michael", "Faraday")
# persona_2 = Persona("André", "Ampère")
# persona_3 = Persona("Alessandro", "Volta")

# print(Persona.lista_personas)

# --------------------------------------------------

# __add__

# class Producto:
#     def __init__(self, nombre: str, cantidad: int):
#         self.nombre: str = nombre
#         self.cantidad: int = cantidad

class Producto:
    def __init__(self, nombre: str, cantidad: int):
        self.nombre: str = nombre
        self.cantidad: int = cantidad

    def __add__(self, producto: "Producto"):
        suma_cantidades = self.cantidad + producto.cantidad
        return suma_cantidades

p1 = Producto("Teclado", 3)
p2 = Producto("Mouse", 4)
total_cantidad_productos = p1 + p2
print(total_cantidad_productos)
print(p1.cantidad)
print(p2.cantidad)



