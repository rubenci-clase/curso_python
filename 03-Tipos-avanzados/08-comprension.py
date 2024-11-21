# Comprensión listas en python

"""
Comprensión en python con listas
- Transformar elementos de la lista (map)
- Filtrar elementos de la lista (filter)
- Transformar y filtrar elementos )map-filter)
"""

# Tomar esta lista de usuarios
usuarios = [
    ["Beatriz", 1],
    ["Mónica", 3],
    ["Mario", 4],
    ["Alejandro", 2],
    ["Carlos", 5],
]

# Transformarla para obtener una lista de nombres
# Solución1: Iterar con for, y append()

nombres = []
for usuario in usuarios:
    nombres.append(usuario[0])

print(nombres)

# Transformarla para obtener una lista de nombres
# Solución 2: En una sola linea
# nombres = [expresion for item in items]

nombres = [usuario[0] for usuario in usuarios]
print(nombres)

# Filtrar los elementos con id > 2
nombres = [usuario for usuario in usuarios if usuario[1] > 2]
print(nombres)

# Filtrar y transformar los elementos con id > 2
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]
print(nombres)

# transformar a usuarios con map
nombres = list(map(lambda usuario: usuario[0], usuarios))
print(nombres)
