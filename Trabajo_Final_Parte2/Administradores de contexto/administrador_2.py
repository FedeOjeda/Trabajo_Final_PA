"""Crea un administrador de contexto que permita cambiar el directorio de
trabajo al entrar en un bloque y volver al directorio original al salir.
"""
import os

class AdminContexto:
    def __init__(self):
        self.directorios = []

    def __enter__(self):
        self.directorios.append(os.getcwd())
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.directorios.pop())

    def cd(self, dir):
        os.chdir(dir)

with AdminContexto() as directorio:
    print("Directorio actual:", os.getcwd())
    directorio.cd("ruta/al/directorio")
    print("Directorio actual:", os.getcwd())