# Actividad

"""
Definir una función es_palindromo que devuelva 
True si es palindromo, o False si no lo es
Definir una función no_space para eliminar espacios en blanco
Definir una función reverse para devolver la cadena al reves
(utilizando for)

Probar la función con las siguientes cadenas:
Abba, Reconocer, Hola Mundo, Amo la paloma, Dabale arroz a la zorra el abad

"""


def no_space(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return texto_al_reves


def es_palindromo(texto):
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    # print(texto, " ", texto_al_reves)
    return minusculas(texto) == minusculas(texto_al_reves)

def minusculas(texto):
    return texto.lower()

print(minusculas("LDKSJFLSKD"))
print(es_palindromo("Amo la paloma"))
print(es_palindromo("Hola Mundo"))
print(es_palindromo("Reconocer"))
print(es_palindromo("Dabale arroz a la zorra el abad"))
