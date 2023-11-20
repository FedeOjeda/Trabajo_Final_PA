#Clase Departamento
class Departamento:
    
    def __init__(self,nombre_departamento):
        self.nombre_departamento = nombre_departamento
        self.lista_empleados = []
    
    # Método para agregar el empleado
    def agregar_empleado(self,empleado):
        self.lista_empleados.append(empleado)

    # Método para eliminar el empleado
    def eliminar_empleado(self,empleado):
        self.lista_empleados.remove(empleado)

    # Método para consultar la lista de empleados.
    def consultar_empleados(self):
        return self.lista_empleados