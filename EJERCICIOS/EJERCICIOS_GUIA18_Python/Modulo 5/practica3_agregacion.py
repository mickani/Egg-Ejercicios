from typing import Iterable

class Ruedas:
    def __init__(self, cantidad: int):
        self.cantidad: int = cantidad

class Autos:
    stock = 0

    def __init__(self, nombre:str, ruedas: Ruedas):
        self.nombre: str = nombre
        self.ruedas: Ruedas = ruedas
        Autos.stock+=1
        print(f"{self.nombre} tiene {self.ruedas.cantidad} ruedas")
        print(f"Cantidad de autos creados: {Autos.stock}")

    

def fabrica_autos(marcas: Iterable):
    ruedas = Ruedas(cantidad=4)
    for marca in marcas:
        nuevo_auto = Autos(marca, ruedas)

marcas = ["Fiat", "Toyota", "Ford"]
fabrica_autos(marcas)            
    