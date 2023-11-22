"""Hacer un administrador de contexto para notificar eventos al entrar y al
salir de un bloque de código"""

class AdministradorContextoAuto:
    def __enter__(self):
        print("Entrando al auto")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saliendo del auto")

with AdministradorContextoAuto() as auto:
    print("Estoy manejando el auto")