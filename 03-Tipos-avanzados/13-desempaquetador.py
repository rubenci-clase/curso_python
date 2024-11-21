# Desempaquetador en python

"""
Listas para desempaquetarlas
"""

lista = [1, 2, 3, 4]
print(1, 2, 3, 4)

# operador de desempaquetamiento
print(*lista)

# combinar listas con desempaquetador
lista2 = [5, 6]
combinada = (*lista, *lista2)
print(combinada)

combinada = ("Hola", *lista, "mundo", *lista2, "fin")
print(combinada)

# Desempaquetador de diccionarios utilizar **
punto1 = {"x": 19}
punto2 = {"y": 15}
nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)

# que pasaría si agregamos llave y al punto1?
punto1 = {"x": 19, "y": "hola"}
punto2 = {"y": 15}
nuevoPunto = {**punto1, **punto2}
print(nuevoPunto)

# Se pueden añadir elementos del diccionario en cualquier posición
nuevoPunto = {"r": 12, **punto1, "q": 1, **punto2, "w": 23, }
print(nuevoPunto)
