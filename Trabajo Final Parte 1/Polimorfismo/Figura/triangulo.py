from Figura import FiguraGeometrica

# Clase Triángulo  
class Triangulo(FiguraGeometrica):
    valor_area = 0
    valor_perimetro = 0
    def __init__(self, base, altura, lado_a, lado_b):
        self.base = base
        self.altura = altura
        self.lado_a = lado_a
        self.lado_b = lado_b
    
    def area(self):
        self.valor_area = self.base * self.altura /2
        return self.valor_area
    
    def perimetro(self):
        self.valor_perimetro = self.lado_a + self.lado_b + self.base
        return self.valor_perimetro
    
    def mostrar_resultados(self):
        return f'El area del triángulo es igual a {self.valor_area} y el perímetro es igual a {self.valor_perimetro}.'