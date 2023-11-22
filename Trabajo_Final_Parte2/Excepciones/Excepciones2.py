"""Crea una lista de números y, a continuación, intenta acceder a un
elemento en un índice especificado por el usuario. Utiliza un
bloque try y except para manejar la excepción que se produce si
el índice está fuera de rango.
"""

try:
    numeros = [1, 2, 3, 4, 5]
    
    indice = int(input("Ingrese el índice del elemento que desea acceder: "))
    elemento = numeros[indice]
    print(f"El elemento en el índice {indice} es {elemento}")
except IndexError:
    print("El índice especificado está fuera de rango")