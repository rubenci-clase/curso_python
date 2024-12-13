import math

def calculadora_raiz_cuadrada():
    try:
        numero = float(input("Introduce un número para calcular su raíz cuadrada: "))
        if numero < 0:
            raise ValueError("Error: No se puede calcular la raíz cuadrada de un número negativo.")
        raiz = math.sqrt(numero)
        print(f"La raíz cuadrada de {numero} es {raiz}")
    except ValueError as e:
        print(e)

calculadora_raiz_cuadrada()