from coche import Coche
from motocicleta import Motocicleta
from bicicleta import Bicicleta

# Implementación Auto  
auto = Coche('Fiat','Cronos','120 km/h', 'Manual')
print(auto.mostrar_datos())
print(auto.usar_freno_de_mano())

# Implementación Motocicleta
moto = Motocicleta('Honda','Wave','180 km/h', '4 clindros')
print(moto.mostrar_datos())
print(moto.acelerar())

# Implementación Bicicleta 
bicicleta = Bicicleta('Giant', 2012 ,'120 km/h', 'Montaña')
print(bicicleta.mostrar_datos())
print(bicicleta.levantar_rueda_delantera())