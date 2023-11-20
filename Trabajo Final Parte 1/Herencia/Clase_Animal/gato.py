from animal import Animal

# Clase Gato
class Gato(Animal):
    def __init__(self,nombre,edad):
        super().__init__(nombre,edad)
    
    def mostrar_informacion(self):
        return f'{self.nombre} tiene {self.edad} años.'
     
    def saltar(self):
        return f'{self.nombre} está saltando.'