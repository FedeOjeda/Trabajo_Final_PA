from empleado import Empleado

# Clase Trabajador
class Trabajador(Empleado):
    def __init__(self,nombre,departamento,rol):
        super().__init__(nombre,departamento)
        self.rol = rol
        self.salario = 0
    
    def funcion(self):
        return f'El trabajador {self.nombre} cumple la función de {self.rol} en el departamento de {self.departamento}.'
    
    def calcular_salario(self):
        if self.departamento == 'Desarrollo':
            self.salario = 450000
            return self.salario
        elif self.departamento == 'Recursos Humanos':
            self.salario = 250000
            return self.salario
        else:
            self.salario == 150000
            return self.salario
    
    def mostrar_informacion(self):
        return f'{self.nombre} del departamento de {self.departamento} tiene un salario de ${self.salario} pesos.'