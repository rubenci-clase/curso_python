# Return en funciones en python

"""
Las funciones pueden devolver el resultado
Parametros: Cuando definimos la función las variables
Argumentos: Cuando llamamos a la función el valor que le estamos pasando
"""


def funcion_suma(a, b):
    resultado = a + b
    return resultado


c = funcion_suma(23, 9)
d = funcion_suma(c, 2)

print(d)
