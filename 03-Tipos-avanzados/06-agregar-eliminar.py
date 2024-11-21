# Agregar y Eliminar elementos en  Listas en python

"""
Utilizar el método insert de listas
- para añadir un elemento en una posición concreta
Utilizar el método append 
- para agregar elemento al final
Utilizar el método remove
- para borrar elemento de la lista
Utilizar el método pop
- borra el último elemento de la lista
- borra el elemento del indice 
Utilizar el método Clear
- borra todos los elementos de la lista

palabra reservada del

"""

mascotas = [
    "perro",
    "hamster",
    "gato",
    "hamster",
    "pájaro"
]

print(mascotas)

# Agregar una mascota en el indice 1
mascotas.insert(1, "pez")
print(mascotas)

# Agregar una mascota al final
mascotas.append("gorila")
print(mascotas)

# Eliminar elementos, se indica el elemento a eliminar
# no el indice
# si hay varios elementos, solo elimina el primero que aparece
mascotas.remove("perro")

# eliminar el último elemento con pop()
mascotas.pop()
print(mascotas)

# si quiero eleminar un elemento de un índice en particular
mascotas.pop(0)  # elimina el
print(mascotas)

# eliminar con palabra reservada del, se pasa el índice
del mascotas[0]
print(mascotas)
# eliminar completamente la lista
mascotas.clear()
print(mascotas)
