# Funciones de números en python

"""
Importar el módulo math y utilizar algunas de las funciones 
proporcionadas por este módulo
https://docs.python.org/3/library/math.html
"""

import math

print(round(1.3))  # Redondea el número 1.3 al entero más cercano. Resultado: 1
print(round(1.7))  # Redondea el número 1.7 al entero más cercano. Resultado: 2
print(round(1.5))  # Redondea el número 1.5 al entero más cercano. Resultado: 2
print(abs(-77))  # Devuelve el valor absoluto de -77. Resultado: 77
print(abs(55))  # Devuelve el valor absoluto de 55. Resultado: 55

print(math.ceil(1.1))  # Redondea hacia arriba. Resultado: 2
print(math.floor(1.9999))  # Redondea hacia abajo. Resultado: 1
# Devuelve True si el número no es un número (NaN), de lo contrario False. En este caso, devuelve False.
print(math.isnan(23))
# print(math.isnan("23"))

print(math.pow(10, 3))  # Eleva 10 a la potencia de 3. Resultado: 1000.0
print(math.sqrt(81))  # Calcula la raíz cuadrada de 81. Resultado: 9.0

#pruebas
print(math.ceil(-1.1))
print(math.sqrt(71))
