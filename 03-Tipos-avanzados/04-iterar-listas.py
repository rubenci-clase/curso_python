# Iterar Listas en python

"""
Creamos un listado de mascotas
y como los strings son iterables podemos utilizar bucle for
Función enumerate() convierte lista en tupla
"""

mascotas = ["perro", "gato", "hamster", "pájaro"]

# Desempaquetando listas
# enumerate devuelve un listado de Tuplas (lo veremos más adelante)
for mascota in enumerate(mascotas):
    print(mascota)  # Devuelve una tupla con dos elementos: indice, mascota
    # print(mascota[0])  # Acceder al indice
    # print(mascota[1])  # Acceder a las mascotas


# Acceder al índice de una lista
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)
