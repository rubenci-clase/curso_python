# Calculadora

"""
Realiza operaciones aritméticas después de convertir las cadenas 
ingresadas por el usuario en números enteros.
Todavía no se controlan los errores (si usuario introduce letras en vez de números)
"""

n1 = input("Ingresa primer número:")
n2 = input("Ingresa segundo número:")

print(n1, n2, n1+n2)

# transformar datos de un string a un número
n1 = int(n1)
n2 = int(n2)

suma = n1+n2
resta = n1-n2
multi = n1*n2
div = n1/n2

mensaje = f"""
Para los números {n1} y {n2},
el resultado de la suma es {suma},
el resultado de la resta es {resta},
el resultado de la multiplicación es {multi},
el resultado de la división es {div}
"""

print(mensaje)
