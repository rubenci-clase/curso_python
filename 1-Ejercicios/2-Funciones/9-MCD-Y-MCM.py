

def minimoComunMultiplo(num1, num2):
    print(int )

def maximoComunDivisor():
    print("hola")

def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mcm(a, b):
    return abs(a * b) // mcd(a, b)

# Ejemplo de uso
num1 = 12
num2 = 18
print(f"El MCD de {num1} y {num2} es {mcd(num1, num2)}")
print(f"El MCM de {num1} y {num2} es {mcm(num1, num2)}")