from circulo import Circulo
from rectangulo import Rectangulo
from triangulo import Triangulo


# Instanciación de la Clase Círculo
radio = 10
circulo = Circulo(radio)
circulo.area()
circulo.perimetro()
print(circulo.mostrar_resultados())

# Instanciación de la Clase Rectángulo
largo = 50
ancho = 20
rectangulo = Rectangulo(largo, ancho)
rectangulo.area()
rectangulo.perimetro()
print(rectangulo.mostrar_resultados())

# Instanciación de la Clase Triángulo
base = 40
altura = 60
lado_a = 20
lado_b = 20
triangulo = Triangulo(base, altura, lado_a, lado_b)
triangulo.area()
triangulo.perimetro()
print(triangulo.mostrar_resultados())