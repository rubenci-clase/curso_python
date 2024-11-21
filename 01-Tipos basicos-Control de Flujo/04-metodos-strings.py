# Métodos de Strings en python

"""
diversas operaciones que puedes realizar con cadenas en Python, 
desde cambios en la capitalización hasta la búsqueda y reemplazo de subcadenas
https://docs.python.org/3/library/stdtypes.html#string-methods
"""

# poner espacios en blanco al inicio y al final
animal = "   rinoceronte blanco   "
persona = "shiva"
print(animal.upper())  # Convierte la cadena a mayúsculas.
print(animal.lower())  # Convierte la cadena a minúsculas.
# Capitaliza la primera letra de la cadena y convierte las demás a minúsculas.
print(animal.capitalize())
# Elimina los espacios en blanco al principio y al final de la cadena
print(animal.strip())
# Combina varios métodos para eliminar espacios en blanco y capitalizar la primera letra.
print(animal.strip().capitalize())
# Convierte la cadena para que cada palabra comience con mayúscula.
print(animal.title())
# Elimina espacios en blanco solo del lado izquierdo de la cadena.
print(animal.lstrip())
# Elimina espacios en blanco solo del lado derecho de la cadena.
print(animal.rstrip())
# Devuelve la posición en la que se encuentra la subcadena "bl" dentro de animal.
# Si no encuentra la subcadena, devuelve -1.
print(animal.find("bl"))
# Devuelve True si la subcadena "bl" está presente en animal, de lo contrario, devuelve False.
print("bl" in animal)
# Devuelve True si la subcadena "bl" NO está presente en animal, de lo contrario, devuelve False.
print("bl" not in animal)

# Reemplaza la subcadena "Rin" con "Oca" en la cadena animal.
print(animal.replace("Rin", "Oca"))

#pruebas
print("shiva" not in animal)
print("shiva"  in animal)
print(persona.capitalize())
print(persona.replace("va", "vasssssssssssssss"))