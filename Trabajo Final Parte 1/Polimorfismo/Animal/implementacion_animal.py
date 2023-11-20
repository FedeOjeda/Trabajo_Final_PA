from perro import Perro
from gato import Gato
from pajaro import	Pajaro

# Implementación Perro
perro = Perro('Rocky', 7)
print(perro.mostrar_informacion())
print(perro.sentarce())
print(perro.gritar())

# Implementación Gato
gato = Gato('Lalo', 3)
print(gato.mostrar_informacion())
print(gato.saltar())
print(gato.gritar())

# Implementación Pájaro
pajaro = Pajaro('Fred', 10)
print(pajaro.mostrar_informacion())
print(pajaro.volar())
print(pajaro.gritar())