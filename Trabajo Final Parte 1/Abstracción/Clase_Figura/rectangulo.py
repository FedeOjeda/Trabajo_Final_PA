from Figura import FiguraGeometrica

# Clase Rectángulo
class Rectangulo(FiguraGeometrica):
    
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def area(self):
        return self.largo * self.ancho
    
    def perimetro(self):
        return 2 * self.largo + 2 * self.ancho