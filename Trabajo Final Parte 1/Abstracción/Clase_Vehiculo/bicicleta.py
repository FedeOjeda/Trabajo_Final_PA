from vehiculo import Vehiculo

# Clase Bicicleta
class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, velocidad_maxima, tipo_de_bicicleta):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_de_bicicleta = tipo_de_bicicleta
        
    def mostrar_datos(self):
        info = (self.marca,self.modelo,self.velocidad_maxima,self.tipo_de_bicicleta)
        return info
    
    def levantar_rueda_delantera(self):
        return 'Estas levantado la rueda delantera.'