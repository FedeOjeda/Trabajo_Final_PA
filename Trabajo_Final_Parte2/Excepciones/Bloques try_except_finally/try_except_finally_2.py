"""Crea un programa que solicite al usuario dos números y una
operación matemática (suma, resta, multiplicación, división) para
realizar. Utiliza bloques try, except y finally para manejar cualquier
excepción que pueda ocurrir durante la operación y asegurarte
de que los recursos se liberen correctamente"""

def operaciones(operador,nu1,nu2):
    if operador == '+':
        return nu1 + nu2
    elif operador == '-':
        return nu1 - nu2
    elif operador == '*':
        return nu1 * nu2
    elif operador == '/':
        return nu1 / nu2
    else:
        return "Operación no válida."
try:
    n1 = int(input("Ingrese un número"))
    n2 = int(input("Ingrese otro número"))
    operacion = input("Ingrese una operación matemática (+, -, *, /): ")
    print(operaciones(operacion,n1,n2))
except ValueError:
    print("El valor ingresado no es válido.")
except ZeroDivisionError:
    print("N0 se puede dividir por cero.")
finally:
    print("Operación finalizada.")