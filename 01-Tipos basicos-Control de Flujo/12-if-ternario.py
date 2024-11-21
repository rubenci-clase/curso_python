# if ternario en python

"""
Utilización del operador ternario en
"""

edad = input("Introduce tu edad:")
edad = int(edad)

if edad > 17:
    mensaje = "Es mayor de edad"
else:
    mensaje = "Es menor de edad"

print(mensaje)


mensaje = "Es mayor de edad" if edad > 17 else "Es menor de edad"
print(mensaje)
