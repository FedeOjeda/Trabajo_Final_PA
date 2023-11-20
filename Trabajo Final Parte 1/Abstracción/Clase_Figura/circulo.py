from Figura import FiguraGeometrica

# Clase Círculo
class Circulo(FiguraGeometrica):
    
    pi = 3.14159

    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return self.pi * self.radio**2

    def perimetro(self):
        return 2 * self.pi * self.radio