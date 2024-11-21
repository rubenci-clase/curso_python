# Desempaquetar Listas en python

"""
Creamos un lista de números
Acceder a cada elemento
"""

numeros = [1, 2, 3]
# Como podemos acceder a cada elemento
# primero = numeros[0]
# segundo = numeros[1]
# tercero = numeros[2]

primero, segundo, tercero = numeros
print(primero, segundo, tercero)

# imprimir el primer elemento, y una lista con los demás
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
primero, *otros = numeros
print(primero, otros)
print(type(primero))
print(type(otros))

primero, segundo, *otros = numeros
print(primero, segundo, otros)

primero, *otros, ultimo = numeros
print(primero, ultimo, otros)

primero, segundo, *otros, penult, ultimo = numeros
print(primero, segundo, otros, penult, ultimo)
