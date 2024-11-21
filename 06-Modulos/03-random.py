import random
import string

print(dir(random))
# número entre 0 y 1
print(random.random())

# número entre 1 y 10
print(random.randint(1, 10))

# listado que queremos mezclar
listado = [1, 2, 3, 4, 5, 6, 7]
random.shuffle(listado)
print(listado)

# elegir un valor dentro de una lista
print(random.choice(listado))

# elegir varios elementos dentro de una lista
print(random.choices(listado, k=3))

# también funciona con strings
print(random.choices("asgrc32.43", k=3))

# generar contraseñas de 16 digitos de forma aleatoria
# en python import strings
chars = string.ascii_letters
digitos = string.digits

seleccion = random.choices(chars+digitos, k=16)
print(seleccion)
password = "".join(seleccion)
print(password)
