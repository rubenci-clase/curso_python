
cadena = [1,4,7]

def mediaDeUnaLista(cadena):
    sumaTotal = 0
    numMin = cadena[0]
    numMax = cadena[0]

    for num in cadena:
        sumaTotal += num

        if(numMin < num): numMin = num
        if(numMax > num): numMax = num

    print("La media es: ", sumaTotal / len(cadena))
    print("El número mínimo es: ", numMin)
    print("El número maximo es: ", numMax)

mediaDeUnaLista(cadena)