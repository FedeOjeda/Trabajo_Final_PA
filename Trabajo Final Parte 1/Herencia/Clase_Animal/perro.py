from animal import Animal

# Clase Perro
class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        
    def mostrar_informacion(self):
        return f'{self.nombre} tiene {self.edad} años.'
    
    def sentarce(self):
        return f'{self.nombre} está sentado.'