# Bucle For en python

"""
Iniciación al bucle for 
"""

# Bucle For con range(5): genera una secuencia de números desde 0 hasta 4 (5 excluido).
for numero in range(5):
    print(numero)

for numero in range(5):
    print(numero, numero * "Hola ")

# Bucle For con cadena de texto.
# El bucle for itera sobre cada letra en la cadena de texto
cadena = "esto es una cadena de texto"
for letra in cadena:
    print(letra)

# Control del bucle For
buscar = 3
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break  # detener el script, queremos salir del bucle for

# Control del bucle For, y si no encontramos el número??
buscar = 10
for numero in range(5):
    print(numero)
    if numero == buscar:
        print("encontrado", buscar)
        break  # detener el script, queremos salir del bucle for
else:
    print("no se encontró el número ", buscar)
