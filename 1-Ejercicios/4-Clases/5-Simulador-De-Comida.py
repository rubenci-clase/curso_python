class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.platos = []

    def agregar_plato(self, plato, cantidad):
        self.platos.append({'plato': plato, 'cantidad': cantidad})

    def calcular_total(self):
        total = 0
        for item in self.platos:
            total += item['plato'].precio * item['cantidad']
        return total

    def mostrar_pedido(self):
        print(f"Pedido de {self.cliente.nombre}:")
        for item in self.platos:
            print(
                f"{item['plato'].nombre} - {item['cantidad']} x ${item['plato'].precio} = ${item['plato'].precio * item['cantidad']}")
        print(f"Total: ${self.calcular_total()}")


class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pedidos = []

    def realizar_pedido(self):
        pedido = Pedido(self)
        self.pedidos.append(pedido)
        return pedido


class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.menu = []

    def agregar_plato_al_menu(self, plato):
        self.menu.append(plato)

    def mostrar_menu(self):
        print(f"Menú de {self.nombre}:")
        for plato in self.menu:
            print(f"{plato.nombre} - ${plato.precio}")


restaurante = Restaurante("El Buen Sabor")
plato1 = Plato("Pizza", 12)
plato2 = Plato("Hamburguesa", 8)
plato3 = Plato("Ensalada", 5)

restaurante.agregar_plato_al_menu(plato1)
restaurante.agregar_plato_al_menu(plato2)
restaurante.agregar_plato_al_menu(plato3)

cliente = Cliente("Juan")
cliente.realizar_pedido()
pedido = cliente.pedidos[0]

pedido.agregar_plato(plato1, 2)
pedido.agregar_plato(plato3, 1)

restaurante.mostrar_menu()
pedido.mostrar_pedido()
