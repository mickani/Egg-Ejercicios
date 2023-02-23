from typing import Optional


class Loro:
    '''Clase que maneja datos de loros'''

    habitat: str = "Chaco"
    edad: int

    def __init__(self, nombre: str, sexo: str, habla: Optional[str] = None) -> None:
        self.nombre: str = nombre
        self.sexo: str = sexo
        self.habla: Optional[str] = habla

    def palabras(self) -> str:
            if self.habla:
                mensaje = f"{self.nombre} dice '{self.habla}'"
            else:
                mensaje = f"{self.nombre} no habla."
            return mensaje    

if __name__ == "__main__":

    loro1 = Loro("Pome", "Hembra", "Vamo?")
    loro2 = Loro("Lola", "Hembra")
    loro3 = Loro("Facu", "Macho", "Pepón")

    loro1.edad = 9
    loro2.edad = 13
    loro3.edad = 37
    loro1.habitat = "Chaco"
    loro3.habitat = "San Juan"
    
    Loro.habitat = "Santa Fe"

    print("-----------------\nLOROS\n")
    print(loro1.palabras(),",", loro2.palabras(), "y", loro3.palabras()) 
    print(loro1.nombre, "vive en",loro1.habitat, ",",loro2.nombre,"en", loro2.habitat, "y", loro3.nombre, "en", loro3.habitat)
    print("-----------------\nVARIABLES/ATRIBUTOS DE INSTANCIA DE C/OBJETO\n")

    # Para ver qué variables de instancia tiene cada objeto
    print(loro1.__dict__)
    print(loro2.__dict__)
    print(loro3.__dict__)

    print("-----------------\nLISTA DE LOROS")
    lista_loros = []
    lista_loros.append(loro1)
    lista_loros.append(loro2)
    lista_loros.append(loro3)

    for loro in lista_loros:
        print("\n",loro.nombre,"-", loro.sexo,"-",loro.palabras(),"-",loro.habitat, "-", loro.edad, "años.")