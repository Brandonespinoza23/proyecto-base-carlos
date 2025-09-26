import math

class Avanzadas:
    def __init__(self):
        self.base = 0
        self.exponente = 0
        
    def leerNumeros(self):
        self.base = float(input("Ingresa la base: "))
        self.exponente = float(input("Ingresa el exponente: "))

    def elevarPotencia(self):
        return math.pow(self.base, self.exponente)
    
    def raizCuadrada(self):
        if self.base < 0:
            return "Error: No se puede calcular la raíz cuadrada de un número negativo."
        return math.sqrt(self.base)