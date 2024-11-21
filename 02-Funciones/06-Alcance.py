# Alcance en funciones en python

"""
Alcance de las variables en las funciones pueden devolver el resultado
Parametros: Cuando definimos la función las variables
Argumentos: Cuando llamamos a la función el valor que le estamos pasando

variables globales
variables locales de función
"""

# """
saludo = ""

def funcion_saludar():
    saludo = "Hola Mundo"
    print(saludo)


def funcion_saludarBea():
    saludo = "Hola Beatriz"
    print(saludo)


# podemos llamar a la variable saludo?
# que valor tendría?
print(saludo)

# """

"""
def funcion_saludar():
    saludo = "Hola Mundo"
    print(saludo)


def funcion_saludarBea():
    saludo = "Hola Beatriz"
    print(saludo)


# saludo de funcion_saludar es diferente de saludo de funcion SaludarBea
funcion_saludar()
funcion_saludarBea()
funcion_saludar()
"""


"""
# declaramos una variables global
saludo = "Hola Global"


def funcion_saludar():
    # print(saludo)  # porque da error??
    saludo = "Hola Mundo"
    print(saludo)


def funcion_saludarBea():
    global saludo  # Ojo!!! No es aconsejable utilizar variables globales
    # Utiliza variables dentro del contexto
    saludo = "Hola Beatriz"
    print(saludo)


# saludo de funcion_saludar es diferente de saludo de funcion SaludarBea
funcion_saludar()
print(saludo)
funcion_saludarBea()
print(saludo)
"""
