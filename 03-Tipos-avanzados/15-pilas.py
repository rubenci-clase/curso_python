# Pilas en python
"""
Pilas:  típica pila de monedas (o meter en un saco libros)
el ultimo que llega es al primero que atienden
Algoritmo LIFO
Ejemplo: historial de páginas web, volver atrás

El primer elemento que se atiende es el 4
Y en ese momento:
    el del indice 3 pasa a ser el 2
    el del indice 2 pasa a ser el 1
    el del indice 1 pasa a ser el 0

"""

pila = []
# Agregar elementos con append
pila.append(1)
pila.append(2)
pila.append(3)
print(pila)

# acceder al último elemento con pop()
ultimo = pila.pop()
print(ultimo)

print(pila)
# acceder al último elemento de la pila
print(pila[-1])
pila.pop()
pila.pop()

# detectar la pila vacía
if not pila:
    print("pila vacia")
