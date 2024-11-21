# Parametros y Argumentos en python

"""
En las funciones
Parametros: Cuando definimos la función las variables
Argumentos: Cuando llamamos a la función el valor que le estamos pasando
"""

# Añadimos un parametro a la función


def funcion_hola(nombre):
    print("Hola Mundo")
    print("Curso {nombre}")


# Como tenemos que llamar ahora a nuestra función
funcion_hola()  # porque aquí da error?
funcion_hola("SGE")  # pasar Argumento

# Porque da error en apellido?


def funcion_hola(nombre, apellido):
    print("Hola Mundo")
    print(f"Bienvenido {nombre}")


funcion_hola("Beatriz", "Sanchez")


# Parámetros opcionales
def funcion_hola(nombre, apellido=""):
    print("Hola Mundo")
    print(f"Bienvenido {nombre} {apellido}")


funcion_hola("Beatriz", "Sanchez")
funcion_hola("Beatriz")

# Argumentos nombrados
# Se tienen que nombrar todos los argumentos
funcion_hola(apellido="Sanchez", "Beatriz")