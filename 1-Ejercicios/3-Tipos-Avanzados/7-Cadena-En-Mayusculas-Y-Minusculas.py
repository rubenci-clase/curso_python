def cadena_mayusculas_sin_repeticion(texto):
    texto_mayusculas = texto.upper()

    texto_sin_repetidos = ''.join(dict.fromkeys(texto_mayusculas))

    return texto_sin_repetidos

texto = "aAbcAbcD"
resultado = cadena_mayusculas_sin_repeticion(texto)
print("Resultado:", resultado)