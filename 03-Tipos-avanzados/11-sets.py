# Set en python

"""
Set significa grupo o conjunto
- no se pueden repetir los elementos
- se trabajan igual que en las listas
- agregar un elemento con add
- eliminar un elemento con remove

se define con {}
Los sets no se encuentran ordenados

Operadores con conjuntos 
    | unión
    & intersección
    - diferencia

"""

# primer = {1, 1, 2, 2, 3, 4}
primer = {1, 2, 3, 4}
print(primer)
primer.add(5)
primer.remove(1)
print(primer)

# Podemos hacer operaciones con conjuntos
segundo = [3, 4, 5, 6]
# transformar lista a set, conjunto o grupo
segundo = set(segundo)  # set recibe un Iterable:lista o tupla
print(segundo)

# Operadores importantes
print(primer | segundo)  # unión de conjuntos
print(primer & segundo)  # intersección de  conjuntos
print(primer - segundo)  # diferencia de  conjuntos
"""
en la diferencia de conjuntos, 
se queda sólo con los elementos del primer set
"""

# diferencia simetrica: elementos que nos se encuentran en loo dos conjuntos
print(primer ^ segundo)

# no podemos acceder a los elementos para ordenarlos
# si podemos hacer comprobaciones
# segundo[0]
if 5 in segundo:
    print("El 5 está en el conjunto")
