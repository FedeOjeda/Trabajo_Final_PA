"""Hacer un decorador para agrega un retardo antes de que se ejecute
una función
"""
import time

def retardo(func):
    def wrapper(*args, **kwargs):
        time.sleep(5)
        return func(*args, **kwargs)
    return wrapper

@retardo
def saludar():
    print("Hola, mundo!")

saludar()