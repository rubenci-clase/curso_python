# Ejemplo real de herencia

"""
Cuando utilizamos Bases de Datos (BBDD)
Vamos a poder:
    - Leer
    - Crear
    - Actualizar
    - Eliminar 

Ejemplo: tabla de Usuario con los usuarios pueden tener: nombre, DNI, apellidos    
"""
# Método Guardar, donde podemos crear o actualizar
# Método para Buscar algún elemento a la BBDD


class Model():
    tabla = False
    # añadir un constructor que indique si la tabla está definida en la BBDD

    def __init__(self):
        if not self.tabla:
            print("Error tienes que definir una tabla")

    def guardar(self):
        print(f"Guardando {self.tabla} en BBDD")
    # Se pasa además de self el _id, porque ya existe una función nativa en python llamada id

    @classmethod
    def buscar_por_id(self, _id):
        print(f"Buscando por {_id}")
        print(f"Buscando por {_id} en la tabla {self.tabla}")
# Definir clase Usuario que hereda de Model
# donde solo le pasamos el nombre de la tabla


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()
usuario.guardar()

# Definir un método en Usuario para buscar elementos en la BBDD
usuario.buscar_por_id(123)

# pero un usuario no debería buscar por id
# eso lo debería hacer la clase Model
# modificar con decorador @classmethod
Usuario.buscar_por_id(123)

# Debemos asegurar que va a buscar el usuario en la tabla de usuarios
