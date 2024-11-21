# Invocar excepciones
"""
Vamos a definir una función para dividir números
por defecto vamos a dividir por 0
dará un error al ejecutarla
Dentro de la función vamos a controlar la excepción
https://docs.python.org/3/library/exceptions.html
Exception hierarchy

Conocer la estructura jerárquica de las excepciones
Intentar evitar el uso de excepciones generales: Exception o BaseException
- no debemos lanzar demasiadas excepciones, porque ralentizan el rendimiento 
- podemos crear excepciones personalizadas

"""


def division(n=0):
    if n == 0:
        # raise Exception("No se puede dividir por cero")
        # raise ZeroDivisionError("No se puede dividir por cero")
        raise ZeroDivisionError("No se puede dividir por cero:", f"{n}")
    return 5/n


# division()

# Envolver la division() con Try
try:
    division()
# ahora ya recogemos todas las excepciones, dentro de la función cambiar {n}
except ZeroDivisionError as e:
    print(e)  # comprobar que devuelve una tupla
