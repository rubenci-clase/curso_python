# Extender tipos nativos
"""
Podemos extender tipos nativos creando nuevas clases

"""
lista = list([1, 2, 3])
lista.append(4)

# Agregar un elemento al comienzo de la lista???
# Ese método no existe, pero podríamos realizarlo así
lista.insert(0, 0)  # insertar en el indice 0 el elemento 0

# Como podemos agregar métodos??? Creando una clase Lista


class Lista(list):
    def prepend(self, item):  # lo contrario de append, crear elementos al comienzo
        self.insert(0, item)


lista2 = Lista([5, 6, 7, 8])
lista2.append(9)  # añade al final de la lista
lista2.prepend(4)  # añade al principio de la lista
print(lista2)
