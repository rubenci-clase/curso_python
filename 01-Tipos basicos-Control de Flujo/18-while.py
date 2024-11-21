# While en python

"""
Utilización del bucle while
"""

numero = 1
# primero evalúa la expresión del while
# Si es verdadero continúa dentro del while
while numero < 100:
    print(numero)
    numero *= 2
    # cuando llega a 128, como no cumple la condición sale del bucle


# Simular con un bucle while una linea de comandos
comando = ""
while comando.lower() != "salir":
    comando = input("$ ")
    print(comando)

# Modificar el código para que cualquier forma de escribir salir
# se pueda salir del bucle While. (Salir, SALIR, SalIr, etc.)
