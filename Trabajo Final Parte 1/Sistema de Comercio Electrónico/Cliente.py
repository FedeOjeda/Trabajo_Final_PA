# Clase Cliente
class Cliente:
    def __init__(self, nombre, direccion, carrito_de_compra):
        self.nombre = nombre
        self._direccion = direccion
        self.carrito_de_compra = carrito_de_compra

    # Encapsulo el atributo direccion.
    @property
    def direccion(self):
        return self._direccion
    
    # Método para realizar la compra.
    def realizar_compra(self):
        for producto in self.carrito_de_compra.productos:
            producto.cantidad_en_stock -= 1

    # Utilizo polimorfismo, ya que es método utilizado en la Clase CarritoCompra.
    def calcular_total(self):
        return self.carrito_de_compra.calcular_total()