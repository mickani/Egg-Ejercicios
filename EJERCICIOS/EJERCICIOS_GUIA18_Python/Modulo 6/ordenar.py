from dataclasses import asdict, astuple, dataclass, field
from typing import Any


@dataclass(order=True)
class Producto:
    sort_index: Any = field(init=False, repr=False)
    codigo: int
    nombre: str
    precio: float
    cantidad: int = 0
    precio_final: float = field(init=False)

    def __post_init__(self):
        self.precio_final = round(self.precio * 1.12, 2)
        # estsblece en base a qué atributo ordenar
        self.sort_index = self.codigo


p1 = Producto(1, "Pomelo", 50, 1)
p2 = Producto(2, "Manzana", 40, 4)
p3 = Producto(3, "Banana", 100, 3)
p4 = Producto(4, "Semillitas", 30, 100)
print(p4 > p3)
for producto in sorted([p1, p2, p3, p4]):
    print(producto)

# p2 = Producto(1, "Pomelo", 50, 1)
# print(p1)
# print(p1 == p2)

# tupla = astuple(p1)
# print(tupla)

# diccionario = asdict(p1)
# print(diccionario)
