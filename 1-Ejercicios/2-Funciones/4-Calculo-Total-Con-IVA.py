def calcularIva(cantidad, porcentaje = 21):
    print(float(cantidad + (porcentaje / 100 * cantidad)))

cantidad = int(input("Introduce un numero:"))
porcentaje = int(input("Introduce el porcentaje:"))

calcularIva(cantidad, porcentaje)
calcularIva(cantidad)