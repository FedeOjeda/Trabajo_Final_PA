class DividirporCero(Exception):
    pass

def dividir(n1,n2):
    if n2 == 0:
        raise DividirporCero("No se puede dividir por 0")
    return n1/n2

try:
    print(dividir(4,0))
except DividirporCero as error:
    print(error)