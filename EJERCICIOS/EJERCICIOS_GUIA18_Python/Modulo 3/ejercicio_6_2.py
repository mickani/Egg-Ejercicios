import math

def area_circulo(radio):
    """
    Calcula y retorna area círculo
    """
    area=(radio**2)* math.pi
    return area

def main():
    radio=int(input("Radio:"))
    resultado=area_circulo(radio)
    print("Área círculo:", resultado)

main()
