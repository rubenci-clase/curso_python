# Iterables en python

"""
Iterables en python
- rango
- string
- listas
- tuplas 
- diccionario
"""

# Rango
for i in range(5):
    print(i)

# String
mensaje = "Hola"
for letra in mensaje:
    print(letra)

# Listas
lista_numeros = [10, 20, 30, 40, 50]
for numero in lista_numeros:
    print(numero)

# Tuplas
tupla_colores = ("rojo", "verde", "azul")
for color in tupla_colores:
    print(color)

# Diccionario iteracción clave
diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Ejemplo"}
for clave in diccionario:
    print(clave, ":", diccionario[clave])

# Diccionario iteracción clave, valor
diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Ejemplo"}
for clave, valor in diccionario.items():
    print(clave, ":", valor)

# Diccionario iteracción valor
diccionario = {"nombre": "Juan", "edad": 25, "ciudad": "Ejemplo"}
for valor in diccionario.values():
    print(valor)


# Usar enumerate en lista
lista_frutas = ["manzana", "banana", "cereza"]
for indice, fruta in enumerate(lista_frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

# Usar zip con dos listas
nombres = ["Juan", "María", "Pedro"]
edades = [25, 30, 22]
for nombre, edad in zip(nombres, edades):
    print(f"Nombre: {nombre}, Edad: {edad}")
