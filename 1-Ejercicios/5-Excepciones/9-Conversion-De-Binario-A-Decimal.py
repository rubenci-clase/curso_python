def conversion_binario_a_decimal():
    try:
        binario = input("Introduce un número binario: ")
        if not all(bit in '01' for bit in binario):
            raise ValueError("Error: El formato no es binario. Solo se permiten 0s y 1s.")
        decimal = int(binario, 2)
        print(f"El número binario {binario} en decimal es {decimal}")
    except ValueError as e:
        print(e)

conversion_binario_a_decimal()