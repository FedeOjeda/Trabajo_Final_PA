# Clase CarritoCompra
class CarritoCompra:
    def __init__(self):
        self.productos = []
    
    # Método para agregar un producto al carrito.
    def agregar_producto(self, producto):
        self.productos.append(producto)

    # Método para eliminar un producto del carrito.
    def eliminar_producto(self, producto):
        self.productos.remove(producto)

    # Método para calcular el total de la compra.
    def calcular_total(self):
        total = 0
        for producto in self.productos:
            total += producto.precio
        return total       