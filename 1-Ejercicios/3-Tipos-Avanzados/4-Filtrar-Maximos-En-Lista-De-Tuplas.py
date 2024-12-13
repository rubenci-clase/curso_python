lista_tuplas = [("a", 3), ("b", 2), ("c", 4), ("d", 4)]

valor_maximo = max(lista_tuplas, key=lambda x: x[1])[1]

filtradas = [tupla for tupla in lista_tuplas if tupla[1] == valor_maximo]

print(filtradas)