class Estudiantes():
    def __init__(self,nombre,edad,calificaciones):
        self.nombre = nombre
        self.edad = edad
        self._calificaciones = calificaciones
    
    def guardar_nombre(self):
        return self.nombre
    
    def guardar_edad(self):
        return self.edad
    
    def guardar_calificaciones(self):
        return self._calificaciones
    
    def ver_datos(self):
        return f'Nombre: {self.nombre}\nEdad: {self.edad}\nCalificaciones: {self._calificaciones}.'