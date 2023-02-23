def intermedio(f1, f2):
    """
    Se ingresan 2 núm. float y se calcula el número intermedio.
    """
    resultado=(f1+f2)/2
    return resultado


def main():
    float1=float(input("Float 1:"))
    float2=float(input("Float 2:"))    
    resultado=intermedio(float1, float2)
    print("El núm. intermedio entre", float1, "y", float2, "es:", resultado)


main()    