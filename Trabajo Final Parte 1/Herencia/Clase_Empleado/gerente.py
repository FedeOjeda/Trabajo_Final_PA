from empleado import Empleado

# Clase Gerente
class Gerente(Empleado):
    def __init__(self,nombre,salario,departamento, cantidad_de_empleados):
        super().__init__(nombre,salario,departamento)
        self.cantidad_de_empleados = cantidad_de_empleados

    def control_de_empleados(self):
        return f'El gerente {self.nombre} tiene a su cargo {self.cantidad_de_empleados} trabajadores.'
    
    def mostrar_informacion(self):
        return f'{self.nombre} gerente del departamento de {self.departamento} tiene un salrio de ${self.salario} pesos.'