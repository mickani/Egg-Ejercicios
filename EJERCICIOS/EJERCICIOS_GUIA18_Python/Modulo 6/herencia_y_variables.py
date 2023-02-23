from dataclasses import dataclass
from pprint import pprint
from typing import ClassVar, Optional


@dataclass
class Pais:
    lista_paises: ClassVar[list["Pais"]] = []
    pais: str
    descripcion: Optional[str] = None

    def __post_init__(self):
        Pais.lista_paises.append(self)


@dataclass(kw_only=True)
class Capital(Pais):
    poblacion: int
    capital: Optional[str] = None

    def __post_init__(self):
        super().__post_init__()

    def ver_poblacion(self):
        print(f"{self.pais}: {self.poblacion:_}") 
      

dato1= Capital("Arg", descripcion="Un pais binoto", capital="Bs As", poblacion=100000)
dato2= Capital("Esp", poblacion=100000)
dato1.ver_poblacion()
pprint(Pais.lista_paises)

