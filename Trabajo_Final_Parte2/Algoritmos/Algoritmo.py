"""Escribe una función que sume los dígitos de un número pares de un
número entero. Si el número es impar, restarle 3 y sumarlo. Si el número
da negativo, sumar 1"""

def digitos_de_un_numero(numero):
    
    if numero % 2 == 1:
        numero -= 3
        if numero < 0:
            numero += 1

    digitos = str(numero)
    suma = 0
    for digito in digitos:
        if int(digito) % 2 == 0:
            suma += int(digito)

    return suma

print(digitos_de_un_numero(242))