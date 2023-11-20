# Importo la clase abstracta Figura3D
from Figura3D import Figura3D

# La clase Esfera hereda la clase Figura3D.
class Cilindro(Figura3D):
    def __init__(self,color,radio,altura):
        self.color = color
        self._radio = radio
        self._altura = altura
    
    # Encapsulo los atributos radio y altura.
    @property    
    def radio(self):
        return self._radio
    
    @property    
    def altura(self):
        return self._altura
    
    # Aplico polimorfismo al utilizar los métodos abstractos de la clase Figura3D
    def area_superficial(self):
        return 2 * 3.14159 * self._radio * (self._altura + self._radio)
    
    def volumen_superficial(self):
        return 3.14159 * self._radio ** 2 * self._altura