# class Empleado:
#     @staticmethod
#     def ejemplo(x, y):
#         print("Dentro de un método estático", x, "y", y)


# Empleado.ejemplo(10,"a")

class Prueba:
    @staticmethod
    def metodo_estatico_1():
        print("metodo_estatico_1")

    @staticmethod
    def metodo_estatico_2():
            Prueba.metodo_estatico_1()

    @classmethod
    def metodo_clase(cls):
        cls.metodo_estatico_2()


Prueba.metodo_clase()

