# Else y Finally con las excepciones de python
"""
Revisar todos bloques de try
para controlar los errores como deseemos

"""
try:
    n1 = int(input("Ingresa primer número: "))
except Exception as e:
    print("Ocurrió un error")
else:  # Este bloque solo se ejecuta cuando no existen errores
    print("No ocurrió ningún error")
finally:  # Este bloque se ejecuta siempre
    print("Se ejecuta siempre")
