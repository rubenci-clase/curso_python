# Depuración en python

"""
Alcance de las variables en las funciones pueden devolver el resultado
Parametros: Cuando definimos la función las variables
Argumentos: Cuando llamamos a la función el valor que le estamos pasando

variables globales
variables locales de función
"""


def largo(texto):
    resultado = 0
    for char in texto:
        # for _ in texto:
        resultado += 1
    return resultado


# Cual sería el resultado esperado del largo de la cadena??
l = largo("hola Mundo")
print(l)

# Para controlar esto, vamos a depurar el programa
# Icono izquierda del play y bichito (Run and Debug Ctr+Shift+D)
# Create a launch.json file
# Seleccionar el depurador: Python File
# Se crea un nuevo fichero en la carpeta llamado launch.json y settings.json
# Añadir un breakPoint en la linea 22
