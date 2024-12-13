frase = input("Introduce una frase:")

def quitarEspacios(frase):
    letras = []
    for letra in frase:

        if letra != " ":
            letras += letra
    return letras

print(quitarEspacios(frase))