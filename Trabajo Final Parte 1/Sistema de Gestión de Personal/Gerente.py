# Importo la clase Empleado
from Empleado import Empleado

# La clase Gerente Hereda la clase Empleado
class Gerente(Empleado):
    
    # Utilizo los atrbutos de la Clase Empleado, además de atributos que agrego para esta clase.
    def __init__(self, nombre, edad, dni,cargo,departamento):
        super().__init__(nombre, edad, dni,cargo)
        self.departamento = departamento