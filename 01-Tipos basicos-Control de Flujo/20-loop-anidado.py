# Loop Anidado en python

"""
Utilización del bucle for de forma anidada
"""

# Cuidado con estos bucles anidados, no es recomendable utilizarlos
# porque si trabajamos con millones de datos, al realizar esta operación
# tener un fin único
for j in range(3):  # outer for/ outer loop
    for k in range(2):  # inner for / inner loop
        print(f"{j}, {k}")
