# Personalizar excepciones
"""
Vamos a crear una clase que hereda de otra para personalizar las excepciones
Exception

En vez de utilizar 
except ZeroDivisionError as e:
Utilizaremos 
except MiError as e:

Pero porque queremos realizar esto??
Razón es para poder agregar lógica o más valores que sean útiles
por ejemplo crear un costructor, que recibe un mensaje
Error 404, de las páginas web

Podemos crear el método mágico de __str__()
"""


class MiError(Exception):
    "Esta clase es para representar mi error"

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo

    def __str__(self):
        return f"{self.mensaje} - código: {self.codigo}"


def division(n=0):
    if n == 0:
        # Modificar esta línea para pasar el mensaje y el cógido de error
        raise MiError("No se puede dividir por cero:", 805)
    return 5/n


try:
    division()
# except MiError as e:
# Al definir el constructor en la clase, ahora podemos acceder a código
# e.codigo  y también a e.mensaje
except MiError as e:
    print(e.codigo, e.mensaje)
    print(e)
