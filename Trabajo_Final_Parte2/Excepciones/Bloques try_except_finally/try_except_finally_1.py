"""Escribe un programa que intente abrir un archivo, leer su
contenido y luego cerrarlo. Utiliza bloques try, except y finally
para asegurarte de que el archivo se cierre correctamente,
incluso si ocurre una excepción durante la lectura.
"""
def leer_archivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        return archivo.read()
    
try:
    contenido_archivo = leer_archivo("archivo")
    print(contenido_archivo)
except FileNotFoundError:
    print("El archivo no se pudo abrir.")
finally:
    if "archivo":
        archivo = open("archivo", "r")
        archivo.close()