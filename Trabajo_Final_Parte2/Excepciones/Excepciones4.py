"""Escribe un programa que intente abrir un archivo que no existe y
utilice un bloque try y except para manejar la excepción de
"FileNotFoundError"."""

try:
    archivo = open("archivo.txt", "r")
except FileNotFoundError:
    print("El archivo que se intenta abrir no existe.") 
