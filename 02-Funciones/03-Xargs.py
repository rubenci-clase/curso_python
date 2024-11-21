# Xargs en python

"""
En las funciones se pueden pasar multiples parámetros sin tener definido un número en concreto
Parametros: Cuando definimos la función las variables
Argumentos: Cuando llamamos a la función el valor que le estamos pasando
"""

# Funcion de dos argumentos


def funcion_suma(a, b):
    print(a + b)

funcion_suma(3, 4)
# Y si queremos Funcion de tres argumentos
funcion_suma(3, 4, 6)

# y una función de 5 argumentos
funcion_suma(3, 4, 6, 10, 3)


# SOLUCIÓN: utilizar Xargs en la declaración de la función
# Se aconseja poner plural en la variable que se pasa como parámetro


def funcion_suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
        # print(resultado) # Ojo con la identación
    print(resultado)


funcion_suma(3, 4)
# Y si queremos Funcion de tres argumentos
funcion_suma(3, 4, 6)

# y una función de 5 argumentos
funcion_suma(3, 4, 6, 10, 3)
