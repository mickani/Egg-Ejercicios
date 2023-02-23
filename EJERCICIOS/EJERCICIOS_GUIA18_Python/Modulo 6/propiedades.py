# class Circulo:
#     def __init__(self, radio: float):
#         self.radio = radio

#     def diametro(self):
#         return self.radio * 2

# class Circulo:
#     def __init__(self, radio: float):
#         self.radio = radio

#     @property
#     def diametro(self):
#         return self.radio * 2


class Circulo:
    def __init__(self, radio: float):
        self.radio = radio

    @property
    def diametro(self):
        return self.radio * 2

    @diametro.setter
    def diametro(self, valor: float):
        if valor <= 0:
            raise ValueError
        self.radio = valor / 2    



c1 = Circulo(10)
# print(c1.diametro())
c1.diametro = 40
print(c1.diametro)   
c1.diametro = -20 
