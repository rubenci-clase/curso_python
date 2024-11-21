import math

radio = float(input("introduce el radio: "))
altura = float(input("introduce el altura: "))


def areaCirculo(radio):
    return math.pi * radio*radio

def volumenCirculo(altura, radio):
    return areaCirculo(radio) * altura


print(areaCirculo(radio))
print(volumenCirculo(altura, radio))