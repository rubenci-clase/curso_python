# Primera Clase

class Perro:
    # Convención de llamar clases en Pascal Case/Upper Camel case
    # Primera letra en Mayuscula: MiPerro
    # Agregar todas las funciones y variables de esta clase
    def habla(self):
        # todas las funciones dentro de una clase son métodos
        # dentro de los parentesis siempre incluir el parámetro self
        print("Guau!!!")


# Crear una instancia de mi clase
# Pascal case diferencia si creamos instancia de una clase o llamamos a función (underscore)
mi_perro = Perro()
print(type(mi_perro))

# <class '__main__.Perro'>
# __main__ se refiere al módulo (lo veremos más adelante)
# ver métodos de Perro además del creado por nosotros habla

mi_perro.habla()  # no hay que pasar ningún argumento al método, salvo que incluyamos otros además de self

# Verificar si este objeto es instancia de una clase en particular
print(isinstance(mi_perro, Perro))
print(isinstance(mi_perro, str))
