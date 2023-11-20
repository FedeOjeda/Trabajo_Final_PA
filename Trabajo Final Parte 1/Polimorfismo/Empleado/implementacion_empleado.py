from gerente import Gerente
from trabajador import Trabajador

# Implementación Gerente
pablo = Gerente('Pablo Gonzales','Desarrollo',30)
print(pablo.control_de_empleados())
pablo.calcular_salario()
print(pablo.mostrar_informacion())

# Implementación Trabajador
lucas = Trabajador('Lucas Rodriguez','Recursos Humanos','Administrativo')
print(lucas.funcion())
lucas.calcular_salario()
print(lucas.mostrar_informacion())