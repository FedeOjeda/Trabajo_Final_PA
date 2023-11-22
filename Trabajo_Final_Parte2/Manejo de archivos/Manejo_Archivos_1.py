"""Escribe un programa que abra un archivo de entrada, lea su contenido y
luego escriba ese contenido en un nuevo archivo de salida. Asegúrate
de cerrar ambos archivos al final."""

def copiar_archivo(archivo_entrada, archivo_salida):
  
  with open(archivo_entrada, "r") as f_entrada:
    with open(archivo_salida, "w") as f_salida:
      contenido = f_entrada.read()
      f_salida.write(contenido)
  f_entrada.close()
  f_salida.close()

copiar_archivo("ArchivoUno.txt", "ArchivoDos.txt")
  
  