"""Escribe un programa que abra un archivo, lea su contenido y
escriba el mismo contenido en otro archivo. Utiliza bloques try,
except y finally para manejar cualquier excepción que pueda
ocurrir durante la lectura o escritura, y asegúrate de que ambos
archivos se cierren correctamente."""

def copiar_archivo(archivo_origen, archivo_destino):
    with open(archivo_origen, "r") as f_origen:
        with open(archivo_destino, "w") as f_destino:
            contenido = f_origen.read()
            f_destino.write(contenido)
            
try:
    copiar_archivo("archivo1", "archivo2")
except FileNotFoundError:
    print("El archivo no se pudo abrir.")
finally:
    print("Los archivos se han copiado correctamente.")