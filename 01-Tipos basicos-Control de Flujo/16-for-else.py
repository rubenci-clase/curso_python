# Bucle For-Else en python

"""
Ejemplo de cómo utilizar el bucle for junto con declaraciones de control (break y else) 
para manejar diferentes situaciones dentro de un bucle.
"""

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
