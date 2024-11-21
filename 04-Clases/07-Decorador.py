# Decorador Properties en Python
"""
Desde la clase Perro con la que hemos estado trabajando, dejar solo el constructor y nombre
Es posible crear instancias de perro con nombres no recomendados
La intención de los decoradores es poder controlar los atributos de la clase
Podemos exponer en la instancia de nuestro objeto
solamente el nombre de la propiedad que queremos obtener
sin necesidad de contaminar con muchos métodos que no van a ser necesarios las instancias
de nuestras clases. 
"""
"""

class Perro:
    def __init__(self, nombre):
        self.nombre = nombre


perro = Perro("Chocolate")
print(perro.nombre)
# Podemos añadir una instancia de Perro con nombre vacío
perro2 = Perro("")
print(perro2.nombre)
# Podemos añadir una instancia de Perro con nombre True
perro3 = Perro(True)
print(perro3.nombre)
"""

# Para controlar que el nombre del perro se valide
# podemos crear un método de clase set_nombre
# hacer la propiedad de nombre privado con Ctrl+Shift+P
# para retornar el nombre de la mascota crear metodo get_nombre
"""


class Perro:
    def __init__(self, nombre):
        self.set_nombre(nombre)

    def set_nombre(self, nombre):
        if nombre.strip():
            self.__nombre = nombre
        # si está vacío el nombre salimos del método sin hacer nada
        return

    def get_nombre(self):
        return self.__nombre


perro = Perro("Luna")
print(perro.get_nombre())


# Revisar las propiedades y métodos de la instancia perro
# __nombre esta no nos va a servir
# get_nombre
# set_nombre
print(perro.__nombre)  # nos deja seleccionar la propiedad privada, pero da error
"""

# Hay una solución en python para hacerlo de forma correcta
# Añadimos decoradores


class Perro:
    def __init__(self, nombre):
        # self.set_nombre(nombre)
        self.nombre = nombre  # cuando hayamos incluido los decoradores

    @property  # indicarle al método de abajo que lo transforme en una propiedad
    def nombre(self):  # def get_nombre(self):
        print("pasando por getter")
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):  # def set_nombre(self, nombre):
        print("pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return
    # Hemos dejado dos métodos nombre en Perro
    # pero han quedado completamente ocultos
    # y en realidad son diferentes porque dependen del decorador


perro = Perro("Luna")
# revisar las propiedades de perro.
# nombre y __nombre
print(perro.nombre)
