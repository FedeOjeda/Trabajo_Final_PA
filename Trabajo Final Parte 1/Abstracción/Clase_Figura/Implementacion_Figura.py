from circulo import Circulo
from rectangulo import Rectangulo
from triangulo import Triangulo


# Instanciación de la Clase Círculo
radio = 10
circulo = Circulo(radio)
print(circulo.area())
print(circulo.perimetro())

# Instanciación de la Clase Rectángulo
largo = 50
ancho = 20
rectangulo = Rectangulo(largo, ancho)
print(rectangulo.area())
print(rectangulo.perimetro())

# Instanciación de la Clase Triángulo
base = 40
altura = 60
lado_a = 20
lado_b = 20
triangulo = Triangulo(base, altura, lado_a, lado_b)
print(triangulo.area())
print(triangulo.perimetro())