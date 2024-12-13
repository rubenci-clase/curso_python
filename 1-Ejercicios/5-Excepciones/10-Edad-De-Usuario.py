from datetime import datetime


def calcular_edad():
    try:
        año_actual = datetime.now().year
        año_nacimiento = int(input("Introduce tu año de nacimiento: "))

        if año_nacimiento > año_actual:
            raise ValueError("Error: El año de nacimiento no puede ser mayor al año actual.")

        edad = año_actual - año_nacimiento
        print(f"Tu edad es: {edad} años.")
    except ValueError as e:
        print(e)

calcular_edad()
