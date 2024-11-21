# Metodos de las Clases
class Perro:
    patas = 4  # propiedad de clase

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Como hacer que habla() sea Método de Clase
    # cambiar self por cls (clase), convención para referirnos a la clase misma
    @classmethod  # esto es un decorador
    def habla(cls):
        print(" Guau!!!")

    # Métodos de clase, pueden servir para crear instancias de clase
    # con valores por defecto
    # factory method =  fábrica de clases
    @classmethod
    def factory(cls):
        return cls("Luna", 3)
        """
        Sería como hacer el retorno de la propia clase
        return Perro("Luna", 3)
        """


Perro.habla()  # no es una instancia de Perro, es la propia clase
perro1 = Perro("Kira", 2)
perro2 = Perro("Lukas", 1)

# Crear una instancia con factory
perro3 = Perro.factory()
print(perro3.edad, perro3.nombre)
