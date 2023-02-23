class Producto:
    def __init__(self, nombre: str, cantindad: int):
        self.nombre = nombre
        self.cantidad = cantindad    



p1 = Producto("Teclado", 3)
p2 = Producto("Mouse", 5)
print(p1.nombre.__contains__("teclado"))
print(p1.nombre.__contains__("Teclado"))