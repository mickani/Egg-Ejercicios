def recortar(n, li, ls):
    """
    3 argumento: "num", "límite inferior","limite superior"\n
    De acuerdo a ciertas condiciones\n
    va a devolver el "num", "límite inferior" o "limite superior"
    """
    if n < li:
        return li
    elif n > ls:
        return ls
    else:
        return n


def main():
    numero = int(input("Núm:"))
    limite_inferior = int(input("limite inferior:"))
    limite_suprior = int(input("limite superior:"))
    resultado = recortar(numero, limite_inferior, limite_suprior)
    print("\nEl resultado es", resultado)


main()
