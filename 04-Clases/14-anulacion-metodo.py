# Anulación de Método
"""
Method Override o Anulación de Método
tomamos un método heredado y decidimos reemplazarlo
por otro para cambiar su funcionalidad
"""


class Ave:
    # def __init__(self):
    #     self.volador = "volador"
    #     # settear volador a la instancia

    def vuela(self):
        print("Vuela ave")

# hereda de Ave


class Pato(Ave):
    # def __init__(self):
    #     super().__init__()  # llamar al constructor de Ave
    #     self.nadador = "nadador"

    def vuela(self):
        # super().vuela()
        print("Vuela pato")
        # super().vuela()


pato = Pato()
# Como hemos definido el método vuela en la clase Pato
# Anulamos el método vuela de la clase padre Ave
# y nos quedamos con el método vuela de la clase Pato
pato.vuela()

# Añadir en el método vuela de la clase Pato
# super() esto lo que hace es coger todos los metodos de la clase padre

# Y si hacemos lo mismo con el constructor??
# Crear en ave un constructor __init__ para settear volador
# Crear en Pato un constructor __init__ para settear nadador

# Por qué da error???
# print(pato.volador, pato.nadador)

# Llamar al constructor desde Pato al constructor de Ave.
