"""Escribe un programa que abra un archivo de texto, cuente cuántas
palabras contiene y muestre el resultado en la pantalla.
"""

def contar_palabras(archivo):
  palabras = 0
  with open(archivo, "r") as f:
    for linea in f:
      for palabra in linea.split():
        palabras += 1
  return palabras

archivo = "archivo.txt"
palabras = contar_palabras(archivo)
print(f"El archivo '{archivo}' tiene {palabras} palabras.")