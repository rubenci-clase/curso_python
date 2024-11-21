from abc import ABC, abstractmethod
# Clases Abstractas

"""
Que pasaría si empezamos a generar instancias de Model()
en lugar de instancias de Usuario()

No es lo que queremos, tendríamos que definir una clase a la que indicarle
que una propiedad o un método son obligatorios definirlos cuando heredemos de ella
si en la clase Usuario no definimos tabla y lo sustituimos por pass
debería arrojarnos un error, porque necesariamente tenemos que definir la tabla

Importar módulo
from abc import ABC, abstractmethod
abc = abstract class
ABC = Clase de la que tenemos que heredar

"""


# class Model():
#     tabla = False

#     def __init__(self):
#         if not self.tabla:
#             print("Error tienes que definir una tabla")

#     def guardar(self):
#         print(f"Guardando {self.tabla} en BBDD")

#     @classmethod
#     def buscar_por_id(self, _id):
#         print(f"Buscando por {_id} en la tabla {self.tabla}")
# # Definir clase Usuario que hereda de Model
# # donde solo le pasamos el nombre de la tabla


# class Usuario(Model):
#     # tabla = "Usuario"
#     pass


# model = Model()
# Model.buscar_por_id(123)

"""
Modificar el código para que la Clase Model sea abstracta
y no podamos crear instancias sin definir la tabla
1º Model debe heredar de la clase ABC
2º cual de los valores es necesario definirlo en la clase Usuario
    - eliminar tabla = True de clase Model
    - añadir un método
        def tabla(self):
            pass
3º agregar dos decoradores: para obligar que sea necesario definir tabla
    @property
    @abstractmethod
"""


class Model(ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod  # y si hacemos guardar abstracto?? tenemos que implementar en Usuario el método de guardar
    def guardar(self):
        # print(f"Guardando {self.tabla} en BBDD")
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"  # type: ignore
    # da error porque ya no necesitamos el constructor de Model1

    def guardar(self):
        print("Guardando Usuario")


# model = Model1()  # dará error
# Model1.buscar_por_id(123)

# la solución es instanciarla desde Usuario1
usuario = Usuario()
Usuario.buscar_por_id(234)
