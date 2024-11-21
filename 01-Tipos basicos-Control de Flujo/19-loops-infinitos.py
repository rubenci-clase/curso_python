# Loop Infinito en python

"""
Utilización del bucle while de forma infinita
"""

# Cuidado con los bucles infinitos
comando = ""
while True:
    comando = input("$ ")
    print(comando)

# Se puede salir de la terminal pulsando Ctrl+C


"""
# Se puede controlar así:
while True:
    comando=input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
"""
