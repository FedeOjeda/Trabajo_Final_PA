class ConvertirValor(Exception):
    pass

ingreso = input("Ingrese una cadena que represente un número: ")

try:
    print(numero = int(ingreso))
    raise ConvertirValor("Error: La cadena no se puede convertir a número.")
except ConvertirValor as error:
    print(error)