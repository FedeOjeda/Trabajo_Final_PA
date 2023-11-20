from forma import Forma

# Clase FormaCírculo
class FormaCirculo(Forma):
    
    pi = 3.14159

    def __init__(self,color,radio):
        super().__init__(color)
        self.radio = radio
    
    def area(self):
        return f'El área del círculo es igual a {self.pi * self.radio**2}.'

    def perimetro(self):
        return f'El perímetro del círculo es igual a {2 * self.pi * self.radio}.'