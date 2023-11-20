# Importo las clases.
from Empleado import Empleado
from Gerente import Gerente
from Departamento import Departamento

# Instanciación de la clase Empleado.
empleado1 = Empleado("Federico",24,47899032,"Analista Junior")
# Cálculo del salario.
empleado1.calcular_salario()
# Consulto el salario.
print(empleado1.consultar_salario())

# Instanciación de la clase Departamento.
departamento1 = Departamento("Desarrollo")
# Agrego al empleado en el departamento.
departamento1.agregar_empleado(empleado1)
# Consulto la lista de empleados del departamento.
print(departamento1.consultar_empleados())

# Instanciación de la Gerente.
gerente1 = Gerente("Pablo",45,42378568,"Gerente","Desarrollo")
# Utilizo polimorfismo para calcular y consulatar el salario del gerente.
gerente1.calcular_salario()
print(gerente1.consultar_salario())

# Agrego al Gerente al departamento creado previamente.
departamento1.agregar_empleado(gerente1)
print(departamento1.consultar_empleados())