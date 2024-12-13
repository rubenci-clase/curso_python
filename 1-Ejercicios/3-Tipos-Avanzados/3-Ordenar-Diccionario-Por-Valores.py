diccionario = {"a": 3, "b": 2, "c": 4, "d": 4}

ordenado = sorted(diccionario.items(), key=lambda item: (item[1], item[0]))

print(ordenado)