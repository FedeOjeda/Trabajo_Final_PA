"""Solicita al usuario que ingrese una cadena que represente un
número. Utiliza un bloque try y except para manejar la excepción
que se produce si la cadena no se puede convertir a un número."""

ingreso = input("Ingrese una cadena que represente un número: ")

try:
    print(numero = int(ingreso))
except ValueError:
    print("Error: La cadena no se puede convertir a número.")