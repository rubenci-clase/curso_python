# Dir en paquetes en Python
"""
si hacemos import de un módulo
utilizando la función dir nos va a mostrar métodos de ese paquete 

metodos magicos y paquetes dentro de ese módulo especifico
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', 
'acciones', 'gestion']
"""
from usuarios.acciones.utilidades import guardar
import usuarios


print(dir(usuarios))
print(usuarios.__name__)
print(usuarios.__package__)
print(usuarios.__path__)
print(usuarios.__file__)
