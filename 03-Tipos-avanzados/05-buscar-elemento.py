# Buscar elementos en  Listas en python

"""
Utilizar el método index de listas
para poder realizar búsquedas
Utilizar el método count 
para contar cuantas veces aparece un elemento en una lista
"""

mascotas = ["perro", "hamster", "gato", "hamster", "pájaro"]

# si encuentra el elemento devuelve el índice donde se encuentra
print(mascotas.index("gato"))
# print(mascotas.index("pulga"))  # si no encuentra el elemento devuelve error

if "pulga" in mascotas:
    print(mascotas.index("pulga"))

print(mascotas.count("pulga"))
print(mascotas.count("perro"))
print(mascotas.count("hamster"))
