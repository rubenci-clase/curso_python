# Tipos de excepciones
"""
controlar los tipos de errores que devuelve python
para dar el mensaje apropiado o con la lógica apropiada

"""
try:
    n1 = int(input("Ingresa primer número: "))
    # asdfasdfas #<class 'NameError'>
except Exception as e:
    print(type(e))


try:
    n1 = int(input("Ingresa primer número: "))
    # asdfasdfas
except ValueError as e:
    print("Ingrese un valor entero")
except NameError as e:
    print("ocurrió un error")
