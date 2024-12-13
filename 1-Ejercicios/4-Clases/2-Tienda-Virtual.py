class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Carrito:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto, cantidad):
        self.productos.append({'producto': producto, 'cantidad': cantidad})

    def calcular_total(self):
        total = 0
        for item in self.productos:
            total += item['producto'].precio * item['cantidad']
        return total

    def mostrar_carrito(self):
        for item in self.productos:
            print(
                f"{item['producto'].nombre} - {item['cantidad']} x ${item['producto'].precio} = ${item['producto'].precio * item['cantidad']}")


class Cliente:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.carrito = Carrito()

    def agregar_producto_al_carrito(self, producto, cantidad):
        self.carrito.agregar_producto(producto, cantidad)

    def ver_total_compra(self):
        return self.carrito.calcular_total()

    def mostrar_carrito(self):
        self.carrito.mostrar_carrito()


producto1 = Producto("Camiseta", 20)
producto2 = Producto("Pantalón", 40)
producto3 = Producto("Zapatos", 60)

cliente = Cliente("Juan Pérez", "Calle Ficticia 123")
cliente.agregar_producto_al_carrito(producto1, 2)
cliente.agregar_producto_al_carrito(producto2, 1)
cliente.agregar_producto_al_carrito(producto3, 1)

print(f"Carrito de {cliente.nombre}:")
cliente.mostrar_carrito()
print(f"Total de la compra: ${cliente.ver_total_compra()}")
