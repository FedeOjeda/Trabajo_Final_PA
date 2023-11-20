from Clase_Coche import Coche

auto = Coche(150,150000)
auto.guardar_kilometros()
auto.guardar_velocidad()
print(auto.ver_informacion())
auto.acelerar(30)
auto.actualizar_kilometraje()
print(auto.ver_informacion())