# Tuplas en python

"""
Tuplas en python
- es igual que las listas, pero no se puede modificar en absoluto
- no se le pueden agregar elementos
- no se le pueden eliminar elementos
- no se le pueden modificar elementos
tendríamos que crear una nueva tupla para poder hacer
estas operaciones

se define con ()
Se utilizan cuando no queremos modificar los elementos
que se almacenan en ellas

"""


numeros = (1, 2, 3)
print(numeros)

# concatenar tuplas
numeros = (1, 2, 3)+(4, 5, 6)
print(numeros)

# transformar esta lista en una tupla
punto = [1, 2]
print(type(punto))

punto = tuple(punto)
# punto = tuple([1,2])
print(punto)
print(type(punto))

# Acceder a elementos de la tupla
menosnum = numeros[:2]
print(menosnum)

# Desempaquetar tuplas
# Ojo!!! devuelve una lista
primero, segundo, *otros = numeros
print(primero, segundo, otros)

# Recorrer todos los elementos de la tupla
for n in numeros:
    print(n)

# Intentamos modificar el valor de un elemento
# numeros[0] = 5
