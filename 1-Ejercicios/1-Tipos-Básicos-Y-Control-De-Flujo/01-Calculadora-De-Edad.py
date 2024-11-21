from datetime import datetime

anioNacimiento = input("Ingresa tu año de nacimiento:")

anios = 2024 - int(anioNacimiento)

if(anios < 18):
    print("Menor")
else:
    print("Mayor")