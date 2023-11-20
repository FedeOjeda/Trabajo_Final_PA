from vehiculo import Vehiculo

# Clase Motocicleta
class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_de_motor):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_de_motor = tipo_de_motor
    
    def mostrar_datos(self):
        info = (self.marca,self.modelo, self.velocidad_maxima,self.tipo_de_motor)
        return info
    
    def acelerar(self):
        return 'estas aumentando la velocidad'