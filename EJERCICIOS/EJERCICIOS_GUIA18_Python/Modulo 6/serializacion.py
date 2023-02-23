from dataclasses import asdict, astuple, dataclass, field


# @dataclass
# class Producto:
#     codigo: int
#     nombre: str
#     precio: float
#     cantidad: int

# -------------------------------------------------
# __eq__

# class Producto:
#     def __init__(self, codigo,nombre, precio,cantidad=0):
#         self.codigo = codigo
#         self.nombre = nombre
#         self.precio = precio
#         self.cantidad = cantidad

#     def __eq__(self, otro):
#         if otro.__class__ is not self.__class__:
#             return NotImplemented
#         return (self.codigo,self.nombre, self.precio, self.cantidad) == (otro.codigo, otro.nombre, otro.precio, otro.cantidad)        

# -------------------------------------------------

# __post_init__

@dataclass
class Producto:
    codigo: int
    nombre: str
    precio: float
    cantidad: int = 0
    precio_final: float = field(init=False)

    def __post_init__(self):
        self.precio_final = round(self.precio * 1.12, 2)


p1 = Producto(1, "Pomelo", 50, 1)
print(p1)
# p2 = Producto(1, "Pomelo", 50, 1)
# print(p1 == p2)

# tupla = astuple(p1)
# print(tupla)

# diccionario = asdict(p1)
# print(diccionario)