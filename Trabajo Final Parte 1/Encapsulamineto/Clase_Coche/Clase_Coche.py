class Coche:
    def __init__(self,velocidad,kilometraje):
        self._velocidad = velocidad
        self.kilometraje = kilometraje
        
    def guardar_velocidad(self):
        return self._velocidad
    
    def guardar_kilometros(self):
        return self.kilometraje
    
    def acelerar(self,nueva_velocidad):
        self._velocidad += nueva_velocidad
        return self._velocidad 
    
    def actualizar_kilometraje(self):
        if self.kilometraje > 0:
            self.kilometraje = self.kilometraje - self._velocidad
            return self.kilometraje
    
    def ver_informacion(self):
        return f'El auto va {self._velocidad}km/h y tiene {self.kilometraje}km de recorrido.'