"""Escribe una función recursiva para calcular el MCD de dos números
enteros.
"""

def calcular_mcd(a, b):
    if b == 0:
        return a
    else:
        return calcular_mcd(b, a % b)
    
print(calcular_mcd(18,48))