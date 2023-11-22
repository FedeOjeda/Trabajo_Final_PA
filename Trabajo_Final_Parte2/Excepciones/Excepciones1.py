"""Escribe un programa que solicite al usuario dos números y realice
la división de uno por el otro. Utiliza un bloque try y except para
manejar la excepción que ocurre si el segundo número es cero."""

def dividir(n1,n2):
    return n1/n2

try:
    print(dividir(4,0))
except ZeroDivisionError:
    print("No se puede dividir entre 0")