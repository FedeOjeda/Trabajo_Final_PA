"""Escribe una función recursiva para encontrar y sumar todos los números
primos desde 1 hasta un número deseado.
"""

def suma_primos(n):
    if n < 2:
        return 0
    elif n == 2:
        return 2
    elif n % 2 == 0:
        return suma_primos(n - 1)
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                return suma_primos(n - 1)
            i += 2
        return suma_primos(n - 1) + n

print(suma_primos(10))