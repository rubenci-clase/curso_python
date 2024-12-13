def diccionario_caracteres_unicos(palabra):

    diccionario = {}

    for indice, caracter in enumerate(palabra):
        if palabra.count(caracter) == 1:
            diccionario[caracter] = indice

    return diccionario

palabra = "programa"
resultado = diccionario_caracteres_unicos(palabra)
print("Diccionario de caracteres únicos:", resultado)