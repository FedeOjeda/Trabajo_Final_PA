"""Hacer un decorador para verificar que los argumentos de una función
sean del tipo correcto.
"""
def verificar_tipo(func):
    def wrapper(*args, **kwargs):
        if not all(isinstance(arg, int) for arg in args):
            return'Todos los argumentos deben ser números'
        return func(*args, **kwargs)
    return wrapper

@verificar_tipo
def suma(a, b):
    return a + b

print(suma(1, 2)) 
print(suma(1, 'a')) 