"""Dada una lista de cadenas, utiliza map y una función lambda para crear
una lista con la longitud de cada palabra.
"""

lista_cadenas = ["tiempo","programar","python"]
contar_caracteres = lambda lista: len(lista)
lista_nueva = list(map(contar_caracteres,lista_cadenas))
print(lista_nueva)