class BuscarClave(Exception):
    pass

diccionario = {"Nombre":"Federico", "Apellido":"Ojeda", "Edad":24}
try:
    print(diccionario["Altura"])
    raise BuscarClave("La clave ingresada no existe.")
except BuscarClave as error:
    print(error)