# map y Filter listas en python

"""
Comprensión en python con listas
- Transformar elementos de la lista (map)
- Filtrar elementos de la lista (filter)
- Transformar y filtrar elementos (map-filter)
Muchos desarrolladores utilizan map y filter en lugar
de la comprensión de listas
"""

# Tomar esta lista de usuarios
usuarios = [
    ["Beatriz", 1],
    ["Mónica", 3],
    ["Mario", 4],
    ["Alejandro", 2],
    ["Carlos", 5],
]
# transformar listas con map
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)

# realizar filtros con filter
filtrados = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(filtrados)
