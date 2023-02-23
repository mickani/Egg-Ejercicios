from dataclasses import dataclass, field
from typing import Optional, ClassVar, Any


@dataclass
class Persona:
    nombre: str
    apellido: str
    edad: int

@dataclass(order=True)
class Estudiante:
    sort_index: Any = field(init=False, repr=False)
    nombre: str
    apellido: str
    edad: int
    localidad: Optional[str] = None

    def __post_init__(self):
        self.sort_index = self.edad

@dataclass(order=True)
class Profesor(Persona):
    sort_index: Any = field(init=False, repr=False)
    materia: str
    escuela: Optional[str] = None  

    def __post_init__(self):
        self.sort_index = self.materia

e1 = Estudiante("Pome", "Pomelero", 9, "San Jorge")
e2 = Estudiante("Mik", "Boss", 31, "San Jorge")
e3 = Estudiante("Facu", "Per", 30, "San Juan")
e4 = Estudiante("Piru", "Bert", 84, "San Jorge")

p1 = Profesor("Pepito", "Pirulo", 30, materia="Lengua")
p2 = Profesor("Juanpa", "Jota", 34, materia="Mate", escuela="Saraza")
p3 = Profesor("Florencia", "Per", 31, materia="Ingles")
p4 = Profesor("Ines", "Per", 32, materia="Sociales")

for e in sorted([e1, e2, e3, e4]):
    print(e)

print("-------------------------------------")

for p in sorted([p1, p2, p3, p4]):
    print(p)  