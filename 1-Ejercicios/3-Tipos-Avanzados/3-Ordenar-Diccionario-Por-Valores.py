


def ordenarDiccionario(diccionario):
    lista = []
    for v in diccionario:
        lista += str(v), diccionario[v]
    return lista


frase = {"x": 25, "y": 50, "z": 40}

lista = ordenarDiccionario(frase)

print(lista)