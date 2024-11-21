# Strings en python

"""
Trabajar con cadenas de texto y utilizar varias operaciones y funciones de 
manipulación de cadenas (slicing)
"""

nombre_curso = "Sistemas de Gestión Empresarial"
descripcion_curso = """
Curso de Sistemas de Gestión Empresarial
Desarrollo de Aplicaciones Multiplataforma
"""

# Imprime la longitud (número de caracteres) de la cadena
print(len(nombre_curso))
print(str(nombre_curso.__len__()))

print(nombre_curso)
print(nombre_curso[0])  # Imprime la subcadena de la posición 0
print(nombre_curso[0:8])  # Imprime la subcadena desde la posición 0 hasta la 8
# Imprime la subcadena desde la posición 9 hasta la última por defecto
print(nombre_curso[9:])
# Imprime la subcadena desde la posición inicial por defecto hasta la 8
print(nombre_curso[:8])
print(nombre_curso[:])  # Imprime toda la cadena
print(nombre_curso[::-1])  # Imprime la cadena invertida
