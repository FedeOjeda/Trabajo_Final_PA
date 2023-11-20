from gerente import Gerente
from trabajador import Trabajador

# Implementación Gerente
pablo = Gerente('Pablo Gonzales',1200000,'IT',30)
print(pablo.control_de_empleados())
print(pablo.mostrar_informacion())

# Implementación Trabajador
lucas = Trabajador('Lucas Rodriguez',450000,'IT','Programador Senior')
print(lucas.funcion())
print(lucas.mostrar_informacion())