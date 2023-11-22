class IndiceFueraDeRango(Exception):
    pass
        
numeros = [1, 2, 3, 4, 5]

try:
    indice = int(input("Ingrese el índice del elemento que desea acceder: "))
    elemento = numeros[indice]
    print(f"El elemento en el índice {indice} es {elemento}")
    raise IndiceFueraDeRango("El índice especificado está fuera de rango")
except IndiceFueraDeRango as error:
    print(error)