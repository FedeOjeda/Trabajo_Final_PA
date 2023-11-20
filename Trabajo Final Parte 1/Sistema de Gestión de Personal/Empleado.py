# Importo la clase Persona
from Persona import Persona

# La clase Empleado Hereda la clase Perosna
class Empleado(Persona):

    # Utilizo los atrbutos de la Clase Persona, además de atributos que agrego para esta clase.
    def __init__(self, nombre, edad, dni, cargo):
        super().__init__(nombre, edad, dni)
        self.salario = 0
        self.cargo = cargo

    # Método para calcular el salario.
    def calcular_salario(self):
        if self.cargo == "Director":
            self.salario = 1000000
            return self.salario
        elif self.cargo == "Gerente":
            self.salario = 500000
            return self.salario
        else:
            self.salario = 250000
            return self.salario
    
    # Método para consultar el salario.    
    def consultar_salario(self):
        return f'Su salario es de ${self.salario}.'