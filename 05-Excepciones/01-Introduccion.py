# Excepciones en python
"""
Como podemos controlar los errores
Algunos errores los podemos corregir de forma sencilla
Y otros errores podemos controlarlos para que muestre información apropiada
en lugar de romper el código


"""

# nos va marcando en rojo los errores
# print(""

# acceder a una lista, e intentar acceder al elemento 45
# lista = [1, 2]
# lista[45]

n1 = int(input("Ingresa primer número: "))
# pasadle un string "hola mundo"
"""
 line 17, in <module>
    n1 = int(input("Ingresa primer número")) 
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
ValueError: invalid literal for int() with base 10: 'hola mundo'

Ese es el error que queremos controlar
Gestionar errores con 
    try
    except
"""
try:
    n1 = int(input("Ingresa primer número: "))
except:
    print("ocurrió un error :(")
