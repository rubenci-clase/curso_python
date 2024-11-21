# Métodos Mágicos Clases en Python
"""
Metodos mágicos: son metodos que se van a ejecutar
cuando nosotros no los estemos llamando directamente
por ejemplo el constructor, cuando creamos una instancia de Perro
sin llamar al constructor en realidad se ejecuta
Todos los metodos mágicos se comienzan por __
"""


class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # def __str__(self):
    #     return f"Clase perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Luna", 5)
# ver todos los metodos mágicos pulsando en __
# esos metodos ya están creados en otra clase principal
# y pasan a las clases por medio de la herencia
# Cuantos métodos mágicos existen?? revisamos los
# más importantes:
print(perro)
# Al realizar print de perro nos aparece:
# <__main__.Perro object at 0x0000028CCD5AE8D0>

# definir un método __str__ en la clase Perro
# delante de def habla
# podemos indicar que debe aparecer cuando hagamos print de perro

print(str(perro))

# documentación de métodos mágicos:
# https://rszalski.github.io/magicmethods/
# Representing your Classes
