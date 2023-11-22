"""Hacer un decorador para registrar las llamadas a una función, junto con
sus argumentos y resultados.
"""
def registro(funcion):
    def wrapper(*args, **kwargs):
        print(f"Llamada a {funcion.__name__} con args {args} y kwargs {kwargs}")
        resultado = funcion(*args, **kwargs)
        print(f"Resultado de {funcion.__name__}: {resultado}")
        return resultado
    return wrapper

@registro
def suma(a, b):
    return a + b

print(suma(1, 2))