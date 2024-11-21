# Filas en python

"""
Filas:  típica fila de un supermercado
el primero que llega es al primero que atienden
Algoritmo FIFO

El primer elemento que se atiende es el 0
Y en ese momento:
    el del indice 1 pasa a ser el 0
    el del indice 2 pasa a ser el 1
    el del indice 3 pasa a ser el 2
Importar del módulo collections la función deque
"""
from collections import deque

lista = [1, 2, 3, 4]
fila = deque(lista)
fila.append(3)
fila.append(4)
fila.append(5)

print(fila)

# eliminar elementos de la izquierda
fila.popleft()
fila.popleft()
print(fila)

if not fila:  # Valores Falsy eran string vacios, 0, None
    print("fila vacia")
