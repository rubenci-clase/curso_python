# if-elif-else en python

"""
Utiliza una estructura de control if-elif-else
"""

# Cambia el valor de edad para revisar todas las posibilidades
edad = input("Introduce tu edad:")
edad = int(edad)

if edad > 65:
    print("Puedes ver la película con super descuento")
elif edad > 54:
    print("Puedes ver la película con descuento")
elif edad > 17:
    print("Puedes ver la película")
else:
    print("No puedes entrar")


print("Listo")

#prueba
if (True != True): print("holaaaaaaaaaaaaaaaaaaaaaaa")
else: print("paco")