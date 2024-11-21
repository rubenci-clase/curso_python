presupuestoMensual = float(input("Introduce el presupuesto mensual:"))

gastoDiarioDeUnaSemana = 0

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]

for dia in enumerate(dias):
    print("Presupuesto del ", dia)
    gastoDiarioDeUnaSemana += float(input("Introduce el gasto:"))

print("Promedio diario: ", gastoDiarioDeUnaSemana/7)
print("El gasto total de la semana es: ", gastoDiarioDeUnaSemana )

if(presupuestoMensual/4 - gastoDiarioDeUnaSemana < 0):
    print("Gastas demasiado")
else:
    print("Te sobra presupuesto")

