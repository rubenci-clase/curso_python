class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def agregar_stock(self, cantidad):
        self.cantidad += cantidad

    def reducir_stock(self, cantidad):
        if self.cantidad >= cantidad:
            self.cantidad -= cantidad
        else:
            print(f"No hay suficiente stock de {self.nombre}. Solo quedan {self.cantidad} unidades.")


class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_inventario(self):
        for producto in self.productos:
            print(f"{producto.nombre} - ${producto.precio} - Stock: {producto.cantidad}")

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre == nombre:
                return producto
        return None


class Proveedor:
    def __init__(self, nombre):
        self.nombre = nombre

    def realizar_pedido(self, producto, cantidad):
        print(f"Realizando pedido a {self.nombre} para {cantidad} unidades de {producto.nombre}")
        producto.agregar_stock(cantidad)


inventario = Inventario()

producto1 = Producto("Camiseta", 15, 20)
producto2 = Producto("Pantalón", 30, 10)

inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)

proveedor = Proveedor("Proveedor A")

inventario.mostrar_inventario()

producto1.reducir_stock(5)

proveedor.realizar_pedido(producto2, 20)

inventario.mostrar_inventario()
