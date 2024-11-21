# Diccionario en python

"""
Los diccionarios son una colección de datos que se encuentran 
agrupados por una llave y un valor
Muy utilizados porque por lo general las bases de datos 
nos devuelven las consultas en diccionarios:
- listado de usuarios
- listado de productos

Se definen con {}
Métodos de diccionarios
- get, para acceder al valor de una llave
- items
- values

Funciones y palabras reservadas
- del, del() para eliminar llaves y valores
"""

# Crear un diccionario
# la llave es un string, el valor puede ser cualquier tipo
punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])  # para acceder a las llaves tenemos que poner su nombre
print(punto["y"])

# podemos añadir nuevas llaves
punto["z"] = 45
print(punto)

# podemos accedera una llave que no existe??
# print(punto("r"))
# Antes debemos confirmar que esa llave existe
if "r" in punto:
    print("Encontré la llave r", punto["r"])
else:
    print("Llave no encontrada")

print(punto.get("x"))  # para acceder al valor de una llave
print(punto.get("r"))  # Si no existe esa llave, devuelve None
print(punto.get("r"), 0)  # Podemos definir valor por defecto si no existe llave

# eliminar llave y valor
del punto["x"]
del (punto["y"])

print(punto)

punto["x"] = 25

# Recorrer las llaves de un diccionario
for valor in punto:
    print(valor)

# Recorrer los valores de un diccionario
for valor in punto:
    print(valor, punto[valor])

# Recorrer las llaves y valores de un diccionario
for valor in punto.items():
    print(valor)

# Recorrer las llaves y los valores de un diccionario
for llave, valor in punto.items():
    print(llave, valor)

# Recorrer los valores de un diccionario
for valor in punto.values():
    print(valor)

# usos reales de diccionarios: usuarios con id único
usuarios = [
    {"id": 1, "nombre": "Beatriz"},
    {"id": 2, "nombre": "Javier"},
    {"id": 3, "nombre": "Mónica"},
    {"id": 4, "nombre": "Felipe"},
]

# Recorrer el diccionario para recuperar el nombre
for usuario in usuarios:
    print(usuario["nombre"])
