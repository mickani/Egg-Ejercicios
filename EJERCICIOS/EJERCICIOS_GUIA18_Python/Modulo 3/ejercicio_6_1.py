def area_rectangulo(base, altura):
    """
    Calcula área de rectángulo
    """
    return base * altura


def main():
    num1=int(input("Num1:"))
    num2=int(input("Num2:"))
    resultado=area_rectangulo(num1, num2)
    print("Área del rectángulo:", resultado)


main()
