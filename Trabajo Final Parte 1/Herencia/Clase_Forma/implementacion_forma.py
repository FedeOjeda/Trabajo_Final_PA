from forma_circulo import FormaCirculo
from forma_rectangulo import FormaRectangulo

# Implementación FormaCírculo
circulo = FormaCirculo('Azul',48)
print(f'El círculo es de color {circulo.color}.')
print(circulo.area())
print(circulo.perimetro())

# Implementación FormaRectángulo
rectangulo = FormaRectangulo('Rojo',80,40)
print(f'El rectángulo es de color {rectangulo.color}.')
print(rectangulo.area())
print(rectangulo.perimetro())