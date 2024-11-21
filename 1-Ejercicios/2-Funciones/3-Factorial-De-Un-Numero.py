def factorial (num):
    if (num == 1):
        return 1
    else:
        return num * int(factorial(num - 1))

print(factorial(int(input("Introduce un numero:"))))