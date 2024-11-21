# Destructor de clases __del__
"""
También es un método mágico, y sirve para destruir la instancia de una clase

"""


class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __del__(self):
        print(f"Adiós perrito :-( {self.nombre}")

    def __str__(self):
        return f"Clase perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Luna", 5)
print(perro)
perro.__del__()

del perro
