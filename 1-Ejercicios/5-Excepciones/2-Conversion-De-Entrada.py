def conversion_de_entrada():
    try:
        numero = int(input("Introduce un número entero: "))
        print(f"El número ingresado es: {numero}")
    except ValueError:
        print("Error: Por favor, ingresa un valor numérico entero válido.")

conversion_de_entrada()
