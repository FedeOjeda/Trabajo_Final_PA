from vehiculo import Vehiculo

# Clase Auto        
class Coche(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, caja_de_cambio):
        super().__init__(marca, modelo, velocidad_maxima)
        self.caja_de_cambio = caja_de_cambio
    
    def mostrar_datos(self):
        info = (self.marca, self.modelo,self.velocidad_maxima,self.caja_de_cambio)
        return info
    
    def usar_freno_de_mano(self):
        return 'Paraste con el freno de mano.'