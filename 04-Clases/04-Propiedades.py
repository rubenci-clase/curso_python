# propiedades = atributos
# asignar una propiedad a una clase
class Perro:
    patas = 4  # propiedad de la clase perro. Todos los perros tienen 4 patas

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print(f"{self.nombre} dice Guau!!!")


mi_perro = Perro("Kira", 2)
mi_perro.habla()
print(Perro.patas)

# puedo modificar la propiedad de la clase??
Perro.patas = 3  # lo cambia para todas las instancias
print(mi_perro.patas)

# puedo modificar la propiedad de la instancia
mi_perro.patas = 5
print(mi_perro.patas)
mi_perro2 = Perro("Lukas", 4)
print(mi_perro2.patas)
