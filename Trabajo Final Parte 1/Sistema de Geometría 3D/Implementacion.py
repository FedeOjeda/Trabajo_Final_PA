# Importo la clases Cubo,Esfera y Cilindro.
from Cubo import Cubo
from Esfera import Esfera
from Cilindro import Cilindro

# Instancio la clase Cubo
cubo = Cubo('Azul',10)
print(f'\nEl cubo {cubo.color} tiene un area igual a {cubo.area_superficial()} y un volumen igual a {cubo.volumen_superficial()}.\n')

# Instancio la clase Esfera
esfera = Esfera('Verde',20)
print(f'El Esfera {esfera.color} tiene un area igual a {esfera.area_superficial()} y un volumen igual a {esfera.volumen_superficial()}.\n')

# Instancio la clase Cilindro
cilindro = Cilindro('Amarillo',20,40)
print(f'El cilindro {cilindro.color} tiene un area igual a {cilindro.area_superficial()} y un volumen igual a {cilindro.volumen_superficial()}.')