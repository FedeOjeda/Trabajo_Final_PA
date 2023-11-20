# Importo la clase abstracta Figura3D
from Figura3D import Figura3D

# La clase Esfera hereda la clase Figura3D.
class Esfera(Figura3D):
    def __init__(self,color,radio):
        self.color = color
        self._radio = radio
    
    # Encapsulo el atributo radio.
    @property    
    def radio(self):
        return self._radio
    
    # Aplico polimorfismo al utilizar los métodos abstractos de la clase Figura3D
    def area_superficial(self):
        return 6 * self._radio ** 2
    
    def volumen_superficial(self):
        return (4 / 3) * 3.14159 * self._radio ** 3