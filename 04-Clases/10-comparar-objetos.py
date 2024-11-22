# Comparar dos instancias de un objeto en Python
"""
Vamos a crear dos instancias de una clase Coordenadas
lat es latitud
lon es longitud
Y realizar comparaciones con ellas, para ver el comportamiento en python
Métodos mágicos:
    __eq__  equal       ==
    __ne__  no equal    !=
    __lt__  less than   <
    __le__  less equal  <=
    __gt__  great than  >
    __ge__  great equal >=

"""


from codecs import latin_1_decode


class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro):
        return self.lat == otro.lat and self.lon == otro.lon

    # def __ne__(self, otro):
    #     return self.lat != otro.lat or self.lon != otro.lon

    def __lt__(self, otro):
        return self.lat + self.lon < otro.lat + otro.lon

    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon


# generamos dos coordenadas
coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

# Son iguales coords=coords2
print(coords == coords2)

# Por qué no son iguales, veamos lo que hay en cada instancia
print(coords, "\n", coords2)
# nos devuelve el espacio en memoria donde están guardadas
# las instancias de la clase, no los valores que acogen
# implementar un método mágico __eq__, y volver a ejecutar el código

# implementar el método mágico __ne__
# Son distintos coords=coords2
print(coords != coords2)
# funcionaría sin el método __ne__??, comentalo en la clase
# python ya es capaz de invertir el método __eq__ aun sin definir el __ne_-

# crear método para comparar si una instacia es <
# podemos comparar si una coordenada es menor que la otra??
# dará error si no tenemos definido el método __lt__
print(coords < coords2)

# es capaz de resolver si es > que ??
# sin necesidad de crear método __gt__
print(coords > coords2)

print(coords <= coords2)
print(coords >= coords2)

