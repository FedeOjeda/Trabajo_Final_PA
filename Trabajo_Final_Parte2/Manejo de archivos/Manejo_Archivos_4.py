"""Escribe un programa que tome varios archivos de texto y los concatena
en un solo archivo de salida. Asegúrate de cerrar todos los archivos
correctamente"""

def concatenate_files(archivos_entrada, archivo_salida):
    with open(archivo_salida, 'w') as salida:
        for entrada in archivos_entrada:
            with open(entrada, 'r') as archivo:
                for linea in archivo:
                    salida.write(linea)
                    
archivos_entrada = ['archivo1.txt', 'archivo2.txt', 'archivo3.txt']
archivo_salida = 'archivo_salida.txt'
concatenate_files(archivos_entrada, archivo_salida)