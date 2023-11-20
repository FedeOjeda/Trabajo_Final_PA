from empleado import Empleado

# Clase Trabajador
class Trabajador(Empleado):
    def __init__(self,nombre,salario,departamento,rol):
        super().__init__(nombre,salario, departamento)
        self.rol = rol
    
    def funcion(self):
        return f'El trabajador {self.nombre} cumple la función de {self.rol} en el departamento de {self.departamento}.'
    
    def mostrar_informacion(self):
        return f'{self.nombre} del departamento de {self.departamento} tiene un salrio de ${self.salario} pesos.'