# Clase Persona
class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self._dni = dni
    
    # Encapsulo el atributo dni.
    @property
    def dni(self):
        return self._dni