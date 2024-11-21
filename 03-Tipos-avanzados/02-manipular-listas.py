# Manipular Listas en python

"""
Creamos un listado de mascotas
"""

mascotas = ["perro", "gato", "hamster", "pájaro"]
# Acceder al elemento con indice
print(mascotas)
print(mascotas[0])
# en las listas se pueden modificar los elementos
mascotas[0] = "elefante"
print(mascotas)

# podemos hacer filtros dentro de la lista
print(mascotas[:3])
print(mascotas[2:])
print(mascotas[-1])  # elemento antes de indice 0, devuelve última posición
print(mascotas[:-1])  # devuelve todos menos el último
print(mascotas[::-1])  # devuelve elementos al reves

print(mascotas[::2])  # toma los elementos saltanto de 2 en 2
print(mascotas[1::2])  # toma los elementos desde el 1 saltando de 2 en 2

# Como hacer una lista de los 40 números
# Print para mostrar solo los números pares
# Print para mostrar solo los números impares
cuarenta = list(range(41))
print(cuarenta[::2])
print(cuarenta[1::2])
