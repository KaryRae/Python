class Cuadrado:

    def __init__(self, arista):
        self.arista = arista
        self.escribir()

    def perimetro(self):
        return self.arista * 4

    def area(self):
        return self.arista ** 2

    def escribir(self):
        print('Soy un cuadrado')

cuad = Cuadrado(5)