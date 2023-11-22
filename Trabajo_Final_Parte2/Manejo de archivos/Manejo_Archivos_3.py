"""Lee un archivo CSV que contiene registros de datos y realiza alguna
operación de procesamiento en los datos, cómo calcular promedios,
encontrar valores máximos o mínimos, o filtrar registros que cumplan
ciertas condiciones"""

import csv

with open("datos.csv", "r") as f:
    reader = csv.reader(f)
    edades = []
    for row in reader:
        edad = int(row[1])
        edades.append(edad)
    print(sum(edades) / len(edades))
    print(max(edades))
    if edad > 35:
            print(row)