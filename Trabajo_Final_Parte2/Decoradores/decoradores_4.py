"""Hacer un decorador para verificar las precondiciones antes de ejecutar
una función.
"""
def pre_condicion(x, y):
    return x > 0 and y > 0

def decorador(func):
    def func_wrapper(x, y):
        if pre_condicion(x, y):
            return func(x, y)
        else:
            return "Los valores de x e y deben ser mayores que 0"
    return func_wrapper

@decorador
def funcion_original(x, y):
    return x + y

print(funcion_original(3, 4)) 
print(funcion_original(-3, 4)) 