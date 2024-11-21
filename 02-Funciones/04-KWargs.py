# KWargs en python

"""
KWargs: Key Word 
Parametros: Cuando definimos la función las variables
Argumentos: Cuando llamamos a la función el valor que le estamos pasando
"""

# Funcion con kwargs


def get_product(**datos):
    print(datos)


get_product("IdProducto")  # porque da error?

# Hay que pasar el nombre del parámetro y el valor del argumento
get_product(id="IdProducto")

# Cuantos argumentos podemos pasar??
get_product(id="IdProducto",
            nombre="Iphone",
            desc="Esto es un iphone")

# que tipo de datos se crea al utilizar KWargs? dict
