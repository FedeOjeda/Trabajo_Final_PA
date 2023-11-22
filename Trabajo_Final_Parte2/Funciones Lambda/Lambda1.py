"""Dada una lista de números, utiliza map y una función lambda para crear
una nueva lista que contenga el doble de cada número."""

numeros_original = [1,2,3,4,5]
duplicar = lambda lista: lista * 2
resultado = list(map(duplicar, numeros_original))
print(resultado)