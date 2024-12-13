def numeros_pares_hasta(n):
    return [i for i in range(n+1) if i % 2 == 0]

numero = int(input("Introduce un número: "))
resultado = numeros_pares_hasta(numero)
print("Números pares hasta", numero, ":", resultado)