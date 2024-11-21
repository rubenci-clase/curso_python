num1 = int(input("Introduce un número:"))
num2 = int(input("Introduce otro número:"))

if(num2 == 0):
    print("El segundo numero es 0")
else:
    division = num1%num2

    if(division/2 == 0):
        print("Es par")
    else:
        print("Es inpar")
