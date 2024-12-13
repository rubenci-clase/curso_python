def agrupar_por_primer_letra(lista):
    diccionario = {}
    for palabra in lista:
        letra = palabra[0].lower()
        if letra not in diccionario:
            diccionario[letra] = []
        diccionario[letra].append(palabra)
    return diccionario

palabras = ["manzana", "mango", "pera", "plátano", "uva", "sandía"]
resultado = agrupar_por_primer_letra(palabras)
print(resultado)