# Herencia multiple
"""
Es posible definir una clase Galgo que herede de Perro
Y que Galgo también herede el método de comer de Animal, 
aunque Perro no derive de Animal??
"""


class Animal:
    def comer(self):
        print("comiendo")

    def pasear(self):
        print("paseando animales")


class Perro:
    def pasear(self):
        print("paseando al perro")


class Galgo(Perro, Animal):  # Herencia multiple
    def correr(self):
        print("corriendo")


galgo = Galgo()

galgo.comer()


# Cual es el problema de la Herencia Multiple??
# que método pasear se ejecutará en Galgo??
# el de la clase de Perro o el de la clase de Animal
galgo.pasear()

# Se hereda de derecha a izquierda, los va reemplazando por lo de la clase de la izquierda
# esto es un problema grave porque si cambiamos la herencia
# Galgo(Animal, Perro) hemos modificado toda la lógica

# Norma o regla: El método que se encuentre duplicado lo debemos eliminar


class Caminador:
    def caminar(self):
        print("caminando")


class Volador:
    def volar(self):
        print("volando")


class Nadador:
    def nadar(self):
        print("nadando")

# podemos crear las siguientes clases con herencia multiple
# las clases que sean lo más pequeñas posibles, con pocos metodos
# class Perro(Caminador, Nadador):
# class PezVolador(Volador, Nadador):
# class Pato(Volador, Nadador, Caminador):
