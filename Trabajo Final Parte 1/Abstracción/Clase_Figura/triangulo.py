from Figura import FiguraGeometrica

# Clase Triángulo  
class Triangulo(FiguraGeometrica):
    
    def __init__(self, base, altura, lado_a, lado_b):
        self.base = base
        self.altura = altura
        self.lado_a = lado_a
        self.lado_b = lado_b
    
    def area(self):
        return self.base * self.altura /2
    
    def perimetro(self):
        return self.lado_a + self.lado_b + self.base