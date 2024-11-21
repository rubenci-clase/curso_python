# Format Strings en python

"""
formas diferentes de crear y formatear cadenas en Python, utilizando la concatenación de cadenas 
como la sintaxis más moderna y legible de f-strings
"""

nombre = "Beatriz"
apellido = "Sánchez"
nota = 10
nombre_completo = nombre + " " + apellido  # concatenación con +
print(nombre_completo)

nombre_completo1 = f"{nombre} {apellido} {nota}"  # operador de formateo de strings
print(nombre_completo1)

nombre_completo2 = f"{nombre[0]} {2+5}"  # operador de formateo de expresiones
print(nombre_completo2)
