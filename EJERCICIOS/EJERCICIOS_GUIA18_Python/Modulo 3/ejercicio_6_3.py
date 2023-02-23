def relacion(e1, e2):
    """
    2 núm. enteros son comparados:\n
    -si el 1ero es mayo retorna 1\n
    -si el 1ero es menor retorna -1\n
    -y si son iguales retorna 0

    """    
    if e1 > e2:
        return 1
    elif e1 < e2:
        return -1
    else:
        return 0

def main():
    entero1=int(input("Entero 1:"))
    entero2=int(input("Entero 2:"))
    resultado=relacion(entero1, entero2)
    print("La relación es:", resultado)

main()    

