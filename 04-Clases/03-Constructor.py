# Constructor Clase
"""
Constructor en clases, es una función que nosotros definimos
en las clases, y este se va a ejecutar siempre que creamos
una nueva instancia de la clase
"""


class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # en el constructor podemos definir propiedades a las clases
        # self se utiliza para referenciar cada una de las instancias de las clases
        self.edad = edad

    # Acceder a las propiedades del constructor
    def habla(self):
        print(f"{self.nombre} dice Guau!!!")

    @api.depends("self.edad")
    def _value_pc(self):
        self.prioridad = float(self.edad) + 100


mi_perro = Perro("Kyra", 1)
mi_perro2 = Perro("Lukas", 4)
print(mi_perro2._value_pc)
# Revisar ahora los métodos o propiedas de nuestra clase
print(mi_perro.nombre)
print(mi_perro2.nombre)
mi_perro.habla()
