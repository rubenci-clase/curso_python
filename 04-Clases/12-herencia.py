# Herencia en clases en python
"""
Definimos varios métodos en diferentes clases
Algunos métodos son iguales para varias clases
Si hay un error en un método lo tenemos que cambiar en todas las clases
La HERENCIA puede solucionar estos problemas
Una clase padre donde definir sólo un método para todos los hijos

"""


class Perro:
    def pasear(self):
        print("paseando")

    def comer(self):
        print("comiendo")


class Gato:
    def comer(self):
        print("comiendo")

    def ronronear(self):
        print("ronroneando")


# el problema de definir metodos iguales en clases distintas
# vamos a crear herencia desde otra clase padre
class Animal:
    def comer(self):
        print("comiendo")

# la clase de Perrohijo, hereda de Animal,
# tiene disponible todos sus métodos y propiedades


class Perrohijo(Animal):
    def pasear(self):
        print("paseando")


class Gatohijo(Animal):
    def ronronear(self):
        print("ronroneando")


# Crear instancia de Perrohijo y Gatohijo
# y comprobar metodos que tienen
perro = Perrohijo()
perro.comer()
perro.pasear()

gato = Gatohijo()
gato.comer()
gato.ronronear()

# y si los gatos pueden pasear??
# definir Gatohijo con herencia de Perrohijo
# Herencia multinivel (recomendado hacerlo solo dos generaciones)
# no podemos controlar la herencia multiple de forma sencilla
