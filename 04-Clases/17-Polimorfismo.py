from abc import ABC, abstractmethod
# Polimorfismo
"""
Vamos a declarar el método guardar en varias clases
- Metodo Abstracto de clase Model, que hereda de Abstracto
- Metodo de clase Usuario, que hereda de Model
- Función guardar donde le pasamos una entidad (instancia de una clase)

"""


class Model(ABC):
    @abstractmethod
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print("Guardando en BBDD")


class Sesion(Model):
    def guardar(self):
        print("Guardando en archivo")


def guardar(entidad):
    entidad.guardar()


# Creamos instancia de Usuario y llamamos a función guardar
# Que sucede???
usuario = Usuario()
guardar(usuario)

# Creamos una instancia de sesión y llamamos a función guardar
# Que sucede???
sesion = Sesion()
guardar(sesion)

# ahora modificamos la función guardar, para que acepte varias entidades


def guardar2(entidades):
    for entidad in entidades:
        entidad.guardar()


guardar2([usuario, sesion])
# Estamos entregando a la función guardar2, dos objetos que cumplen
# con una interfaz necesaria para poder ser ejecutados
# por nuestra función guardar2
# eso es POLIMORFISMO se utiliza mucho en programación
# objetos con metodos similares, y luego definimos función que
# se encarga de llamar a esos métodos de objetos
