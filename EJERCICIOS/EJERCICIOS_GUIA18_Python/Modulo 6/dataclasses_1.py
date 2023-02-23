from dataclasses import dataclass
from dataclasses import field


# class Producto:
#     def __init__(self, codigo, nombre, precio, cantidad):
#         self.codigo = codigo
#         self.nombre = nombre
#         self.precio = precio
#         self.cantidad = cantidad

# @dataclass
# class Producto:
#     codigo: int
#     nombre: str
#     precio: float
#     cantidad: int   

@dataclass
class Producto:
    codigo: int = 0
    nombre: str = ""
    precio: float = field(default=0.0)
    cantidad: int = field(default=0)   



# p1 = Producto(1234, "Cofler", 150, 10)

p1 = Producto()

# ya creó el método __repr__
print(p1)

# Serialización a tuplas o diccionarios (pag24)
