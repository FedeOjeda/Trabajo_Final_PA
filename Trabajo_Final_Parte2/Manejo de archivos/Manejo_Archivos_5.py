"""Lee un archivo CSV que contiene registros de datos y convertirlo en un
archivo JSON"""

import csv
import json

def convertir_archivo(archivo_csv, archivo_json):
  with open(archivo_csv, "r") as archivo_csv:
    reader = csv.reader(archivo_csv, delimiter=",")
    lista_datos_csv = []
    for dato in reader:
      almacenamiento_datos = {}
      for columna in dato:
        almacenamiento_datos[columna] = dato[columna]
      lista_datos_csv.append(almacenamiento_datos)
  with open(archivo_json, "w") as archivo_json:
    json.dump(lista_datos_csv, archivo_json)

archivo_csv = "datos.csv"
archivo_json = "datos.json"
convertir_archivo(archivo_csv, archivo_json)