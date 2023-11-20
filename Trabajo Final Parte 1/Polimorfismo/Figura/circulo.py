from Figura import FiguraGeometrica

# Clase Círculo
class Circulo(FiguraGeometrica):
    valor_area = 0
    valor_perimetro = 0
    pi = 3.14159
    
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        self.valor_area = self.pi * self.radio**2
        return self.valor_area

    def perimetro(self):
        self.valor_perimetro = 2 * self.pi * self.radio
        return self.valor_perimetro
    
    def mostrar_resultados(self):
        return f'El area del círculo es igual a {self.valor_area} y el perímetro es igual a {self.valor_perimetro}.'