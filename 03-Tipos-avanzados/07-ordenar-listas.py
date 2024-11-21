# Ordenar elementos de Listas en python

"""
Utilizar el método sort de listas
- para ordenar los elementos de una lista
- argumento reverse
- argumento key 

Función sorted
- devuelve una nueva lista ordenada

Funciones lambda o expresiones lambda o anónimas
"""

numeros = [2, 45, 6, 17, 7, 1, 1, 2, 3, 4, 8, 9]

# ordenar de menor a mayor
numeros.sort()
print(numeros)

# ordenar de mayor a menor
numeros.sort(reverse=True)
print(numeros)

numeros2 = sorted(numeros)
print(numeros2)

numeros2 = sorted(numeros, reverse=True)
print(numeros2)

# Ordenando listas más complicadas
usuarios = [
    [1, "Beatriz"],
    [3, "Mónica"],
    [4, "Mario"],
    [2, "Alejandro"],
]

usuarios.sort()
print(usuarios)

usuarios2 = [
    ["Beatriz", 1],
    ["Mónica", 3],
    ["Mario", 4],
    ["Alejandro", 2],
]

# ordena alfabeticamente por el nombre usuario
usuarios2.sort()
print(usuarios2)

# Crear una función para ordenar por el elemento de la lista


def ordena(elemento):
    return (elemento[1])


# utilizadno el parametro key de sort
usuarios2.sort(key=ordena)
print("Orden ascendente:", usuarios2)
usuarios2.sort(key=ordena, reverse=True)
print("Orden descendente:", usuarios2)

# Utilizando lambda donde solo le pasamos
# parámetro que recibe esa función
# valor de retorno
usuarios2.sort(key=lambda el: el[1])
print(usuarios2)

# la función lambda se utiliza cuando solo lo vamos a utiliar una vez
# por eso no es necesario declarar una función
