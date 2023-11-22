class BuscarArchivo(Exception):
    pass

try:
    archivo = open("archivo.txt", "r")
    raise BuscarArchivo("El archivo que se intenta abrir no existe.")
except BuscarArchivo as error:
    print(error) 
