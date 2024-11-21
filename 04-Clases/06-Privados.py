# Con el código del fichero anterior
# Atributos Privados, cuando no quiero cambiar el valor de propiedades
# Una vez que le pongo nombre a la mascota, ya no queremos que se pueda modificar
# Queremos transformar nombre para que sea una propiedad privada
class Perro:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.edad = edad

    # pulsando sobre nombre Shift+Ctrl+P Rename Symbol
    # de este modo Visual Code nos renombra ese atributo
    # en toda la clase donde aparece
    def habla(self):
        print(f"{self.__nombre} dice: Guau!!!")

    def get_nombre(self):  # obtener el nombre del perro
        return self.__nombre

    def set_nombre(self, nombre):  # cambiar el nombre del perro
        self.__nombre = nombre

    @classmethod
    def factory(cls):
        return cls("Luna", 3)


perro1 = Perro.factory()
perro1.habla()

# Se puede imprimir el atributo __nombre??
# print(perro1.__nombre)

# Como acceder al nombre del perro??
# Crear un método que me devuelva el nombre del perro
# pero no poder cambiar su valor
# def get_nombre
print(perro1.get_nombre())

# Crear un método para cambiar el nombre del perro
# Validar el nombre del perro, que se adopta y le cambian de nombre
# Depende de lo que se necesite en cada negocio
# def set_nombre

# se pueden hacer también métodos privados
# Con __dict__ podemos ver todas propiedades
# _Perro__nombre propiedad es privada
# edad propiedad publica

print(perro1.__dict__)
# Acceder a la propiedad privada de los objetos
# print(perro1._Perro__nombre)
