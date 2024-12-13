
def limite_de_gastos(limite):
    total_gasto = 0
    while True:
        try:
            gasto = float(input("Introduce el gasto diario: "))
            if gasto < 0:
                raise ValueError("El gasto no puede ser negativo.")
            total_gasto += gasto
            if total_gasto > limite:
                raise Exception(f"¡Error! El gasto total ha superado el límite de {limite}. Total gastado: {total_gasto}")
            print(f"Total gastado hasta ahora: {total_gasto}")
        except ValueError as e:
            print(e)
        except Exception as e:
            print(e)
            break

limite_de_gastos(100)