"""Toma una lista de cadenas y utiliza map con una función lambda para
convertir todas las cadenas en mayúsculas.
"""

lista_minuscula = ["tiempo","programar","python"]
cadena_mayuscula = lambda lista: lista.upper()
lista_mayuscula = list(map(cadena_mayuscula,lista_minuscula))
print(lista_mayuscula)