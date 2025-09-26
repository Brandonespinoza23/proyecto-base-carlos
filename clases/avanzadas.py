import math

class Avanzadas:
    def __init__(self):
        self.num1 = 0
        self.num2 = 0

    def leerNumeros(self):
        self.num1 = int(input("Número base: "))
        self.num2 = int(input("Exponente: "))

    def elevarPotencia(self):
        return math.pow(self.num1, self.num2)
