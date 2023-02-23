# class Empleado:
#     def __init__(self, especialidad, salario):
#         self.especialidad = especialidad
#         self.__salario = salario

# class Empleado:
#     def __init__(self, especialidad, salario):
#         self.especialidad = especialidad
#         self.__salario = salario     

#     def get_salario(self):
#         return self.__salario

class Empleado:
    def __init__(self, especialidad, salario):
        self.especialidad = especialidad
        self.__salario = salario     

    def get_salario(self):
        return self.__salario     

    def set_salario(self, valor):
        self.__salario = valor      


e1 = Empleado("constructor", 1000)

print(e1.especialidad)
# print(e1.__salario)
print(e1.get_salario())

e1.__salario = 2000
print(e1.__salario)

print(e1.__dict__)

# muestra error pero se puede ejecutar y ver el resultado
print(e1._Empleado__salario) 

e1.set_salario(3000)
print(e1.get_salario())
