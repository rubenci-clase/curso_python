# Listas en python

"""
Listas en python, como hacer una lista de supermercado
pan
aceite
zanahorias
"""

# los corchetes marcan que la variable es una lista
# entre cada elemento se pone ,
# listas de números, strings, etc
numeros = [1, 2, 3]
print(numeros)
print(type(numeros))

# lista de caracteres
letras = ["a", "b", "c"]
print(letras)
print(type(letras))

# lista de strings
palabras = ["alumno", "profesor", "clase", "empresa"]
print(palabras)
print(type(palabras))

# lista de booleans
booleans = [True, False, False, True, True]
print(booleans)
print(type(booleans))

# listas de listas, se pueden crear matrices
matriz = [[0, 0], [0, 1], [1, 0], [1, 1]]
print(matriz)
print(type(matriz))

# listado de 10 ceros
# ceros = [0,0,0,0,0,0,0,0,0,0]
ceros = [0] * 10
print(ceros)

ceros_unos = [0, 1] * 10
print(ceros_unos)

# unir dos listas
alfanumerico = numeros + letras
print(alfanumerico)

# crear un listado que contenga un rango de números
# utilizar la función list
# rango = [1..10] # ??? esto no funcionaría
rango = list(range(10))
rango = list(range(1, 11))
print(rango)
print(type(rango))

# lista de strings
chars = list("hola mundo")
print(chars)
print(type(chars))
