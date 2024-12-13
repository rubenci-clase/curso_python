
def clasificarCaracteres(frase):
    diccionario = {}

    for letra in frase:
        if diccionario.__contains__(letra):
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    return diccionario

frase = input("Introduce una frase:")

diccionario = clasificarCaracteres(frase)

for v in diccionario:
    print(v, diccionario[v])