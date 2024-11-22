def calcularIva(cantidad, porcentaje = 21):
    print(float(cantidad + (porcentaje / 100 * cantidad)))

cantidad = int(input("Introduce un numero:"))
porcentaje = input("Introduce el porcentaje:")

if (porcentaje.isnumeric()):
    calcularIva(cantidad, porcentaje)
else:
    calcularIva(cantidad)