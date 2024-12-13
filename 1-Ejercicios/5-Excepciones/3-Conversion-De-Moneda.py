def conversion_de_moneda():
    try:
        euros = float(input("Introduce la cantidad en euros: "))
        if euros < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        dolares = euros * 1.1  # Ejemplo de conversión (1 euro = 1.1 dólares)
        print(f"{euros} euros equivalen a {dolares} dólares.")
    except ValueError as e:
        print(f"Error: {e}")

conversion_de_moneda()