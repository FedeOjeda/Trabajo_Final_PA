# Importo la clase abstracta Figura3D
from Figura3D import Figura3D


# La clase Cubo hereda la clase Figura3D.
class Cubo(Figura3D):
    def __init__(self,color,lado):
        self.color = color
        self._lado = lado
    
    # Encapsulo el atributo lado.
    @property    
    def lado(self):
        return self._lado
    
    # Aplico polimorfismo al utilizar los métodos abstractos de la clase Figura3D
    def area_superficial(self):
        return 6 * self._lado ** 2
    
    def volumen_superficial(self):
        return self._lado ** 3