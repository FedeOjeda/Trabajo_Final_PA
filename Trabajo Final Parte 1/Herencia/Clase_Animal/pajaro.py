from animal import Animal

# Clase Pájaro
class Pajaro(Animal):
    def __init__(self, nombre,edad):
        super().__init__(nombre,edad)
    
    def mostrar_informacion(self):
        return f'{self.nombre} tiene {self.edad} años.'    
    
    def volar(self):
       return f'{self.nombre} está volando' 