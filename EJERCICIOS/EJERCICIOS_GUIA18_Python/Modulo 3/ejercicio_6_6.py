def separar(nums):
    '''
    Se reciben núms. por parámetro y se muestra por pantalla
    una lista con los núms. pares y otra con los impares.
    '''
    nums.sort()
    pares = []
    impares = []

    for num in nums:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    return pares, impares


def main():
    lista_numeros = []
    cantidad_num = int(input("Cantidad de num a ingresar:"))
    cont = 0
    while cont < cantidad_num:
        num = int(input("Ingrese num:"))
        lista_numeros.append(num)
        cont += 1
    pares, impares = separar(lista_numeros)
    print(pares)
    print(impares)


main()
