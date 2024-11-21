
cadena = [1,4,7]

def mediaDeUnaLista(cadena):
    sumaTotal = 0

    for num in cadena:
        sumaTotal += num

    return sumaTotal / len(cadena)

print(mediaDeUnaLista(cadena))