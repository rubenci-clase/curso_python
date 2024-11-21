palabra = str(input("Introduce una palabra:"))

if(palabra.lower() == palabra[::-1].lower()):
    print("Es palindromo")
else:
    print("No es palindromo")


