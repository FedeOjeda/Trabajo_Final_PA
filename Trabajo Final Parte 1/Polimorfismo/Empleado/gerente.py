from empleado import Empleado

# Clase Gerente
class Gerente(Empleado):
    def __init__(self,nombre,departamento, cantidad_de_empleados):
        super().__init__(nombre,departamento)
        self.cantidad_de_empleados = cantidad_de_empleados
        self.salario = 0

    def control_de_empleados(self):
        return f'El gerente {self.nombre} tiene a su cargo {self.cantidad_de_empleados} trabajadores.'
    
    def calcular_salario(self):
        if self.departamento == 'Desarrollo':
            self.salario = 4500000
            return self.salario
        elif self.departamento == 'Recursos Humanos':
            self.salario = 2500000
            return self.salario
        else:
            self.salario == 1500000
            return self.salario
       
    
    
    def mostrar_informacion(self):
        return f'{self.nombre} gerente del departamento de {self.departamento} tiene un salario de ${self.salario} pesos.'