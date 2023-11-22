"""Toma una lista de números y utiliza map con una función lambda para
calcular la raíz cuadrada de cada número."""

numeros_original = [1,4,9,16,25]
raiz_cuadrada = lambda lista: int(lista ** 0.5)
resultado = list(map(raiz_cuadrada, numeros_original))
print(resultado)