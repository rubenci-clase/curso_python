# Contenedores en Python
"""
Meter objetos dentro de otros objetos
Crear dos clases Producto y Categoria, y vamos a conseguir
añadir en Categoria diferentes Productos
Vamos a crear para la clase Producto
    constructor __init__ incluir nombre y precio del producto
    formateador __str__ para visualizar correctamente el producto

La clase Categoría definimos con 
    atributo o propiedad con lista de todos los productos
    constructor __init__ acepta varios productos
    agregar metodo para incluir nuevos productos
    imprimir metodo para ver todos los productos de la categoria    
    """


class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"


class Categoria:
    productos = []

    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos

    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)


# crear una categoría con dos productos
kayak = Producto("Kayak", 1000)
bicicleta = Producto("Bicicleta", 750)

# podemos pasar directamente la lista con los productos
deportes = Categoria("Deportes", [kayak, bicicleta])
deportes.imprimir()

# agregar otro producto
raqueta = Producto("Raqueta", 110)
deportes.agregar(raqueta)
deportes.imprimir()
