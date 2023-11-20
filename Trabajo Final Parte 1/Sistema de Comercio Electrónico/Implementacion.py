#Importo las clases
from Producto import Producto
from CarritoCompra import CarritoCompra
from Cliente import Cliente

# Instanciación de la clase Producto.
producto1 = Producto("Remera", 100, 10)
producto2 = Producto("Pantalón", 200, 5)

# Instanciación de la clase Carrito.
carrito = CarritoCompra()
carrito.agregar_producto(producto1)
carrito.agregar_producto(producto2)

# Instanciación de la clase Cliente.
cliente = Cliente("Federico", "Calle123", carrito)

# Calculo el total antes de la compra.
print(f"Total antes de la compra: ${cliente.calcular_total()}")

# Calculo el total después de la compra.
cliente.realizar_compra()
print(f"Total después de la compra: ${cliente.calcular_total()}")