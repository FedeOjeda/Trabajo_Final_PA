#Importo los métodos abstractos
from abc import ABC,abstractmethod

# Clase abstracta
class Figura3D(ABC):
    
    # Método abstracto para calcular el área.
    @abstractmethod
    def area_superficial(self):
        pass
    
    # Método abstracto para calcular el volumen.
    @abstractmethod
    def volumen_superficial(self):
        pass