# Duck Tiping
"""
Nosotros podemos llamar a la función Guardar, pasando una lista
y lo va a intentar ejecutar hasta que se de cuenta de si lo que le pasamos
tiene método guardar o no

Python tiene tipado dinámico, no va a revisar si está extendido de clase Model
Si camina como Pato y suena como Pato, es un Pato
Es un MODELO
"""


class Usuario():
    def guardar(self):
        print("Guardando en BBDD")


class Sesion():
    def guardar(self):
        print("Guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


# Creamos instancia de Usuario y llamamos a función guardar
# Que sucede???
usuario = Usuario()
guardar(usuario)

# Creamos una instancia de sesión y llamamos a función guardar
# Que sucede???
sesion = Sesion()
guardar(sesion)


def guardar2(entidades):
    for entidad in entidades:
        entidad.guardar()


guardar2([usuario, sesion])
