def lista_de_enteros():
    try:
        lista = input("Introduce una lista de números separados por espacio: ").split()
        lista_enteros = [int(num) for num in lista]
        print(f"La lista de enteros es: {lista_enteros}")
    except ValueError:
        print("Error: Por favor, ingresa solo valores numéricos.")

lista_de_enteros()