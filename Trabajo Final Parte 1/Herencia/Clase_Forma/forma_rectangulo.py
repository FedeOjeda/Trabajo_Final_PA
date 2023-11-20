from forma import Forma

# Clase FormaRectángulo
class FormaRectangulo(Forma):
    
    def __init__(self,color,largo,ancho):
        super().__init__(color)
        self.largo = largo
        self.ancho = ancho
    
    def area(self):
        return f'El área del rectángulo es igual a {self.largo * self.ancho}.'
    
    def perimetro(self):
        return f'El perímetro del rectángulo es igual a {2 * self.largo + 2 * self.ancho}.'