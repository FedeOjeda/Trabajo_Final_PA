from Figura import FiguraGeometrica

# Clase Rectángulo
class Rectangulo(FiguraGeometrica):
    valor_area = 0
    valor_perimetro = 0
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    
    def area(self):
        self.valor_area = self.largo * self.ancho
        return self.valor_area
    
    def perimetro(self):
        self.valor_perimetro = 2 * self.largo + 2 * self.ancho
        return self.valor_perimetro
    
    def mostrar_resultados(self):
        return f'El area del rectángulo es igual a {self.valor_area} y el perímetro es igual a {self.valor_perimetro}.'