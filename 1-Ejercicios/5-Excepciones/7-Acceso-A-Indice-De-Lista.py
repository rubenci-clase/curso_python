def acceso_a_indice():
    lista = [10, 20, 30, 40, 50]

    try:
        indice = int(input(f"Introduce un índice entre 0 y {len(lista) - 1}: "))
        if indice < 0 or indice >= len(lista):
            raise IndexError("Error: El índice no existe en la lista.")
        print(f"Elemento en el índice {indice}: {lista[indice]}")
    except ValueError:
        print("Error: Por favor, ingresa un número entero válido.")
    except IndexError as e:
        print(e)

acceso_a_indice()
