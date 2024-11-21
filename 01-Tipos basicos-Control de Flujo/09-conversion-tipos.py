# Conversión de tipos en python

"""
Ejemplos que ilustran cómo diferentes tipos de datos son evaluados como booleanos en Python.
En general, valores vacíos, None, y el número 0 se consideran False, 
mientras que cualquier otro valor se considera True.
"""
# un input del usuario siempre será de tipo string y la tenemos que convertir
x = input("Introduce input:")
print("El valor introducido es de tipo:", type(x))

# int()
# str()
# float()
# bool()

"""
bool intenta decirnos si la expresión es verdadera True o falso False
hay datos que siempre son True (Truthy)
hay datos que siempre son False (Falsy)

Estos siempre son datos Falsy = 
    ""      (string vacío)
    0       (cero)
    None    (objeto)

Algunos valores siempre son Truthy
    string  

"""

print("String vacía: ", bool(""))
print("String 0: ", bool("0"))
print("None: ", bool(None))
print("Espacio: ", bool(" "))
print("Numero 0: ", bool(0))
