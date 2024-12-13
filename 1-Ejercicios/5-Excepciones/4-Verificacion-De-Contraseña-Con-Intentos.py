def verificar_contraseña():
    contraseña_correcta = "secreta123"
    intentos = 3

    while intentos > 0:
        contraseña = input("Introduce la contraseña: ")
        if contraseña == contraseña_correcta:
            print("Contraseña correcta. Acceso permitido.")
            return
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")

    raise Exception("Error: Has agotado los intentos permitidos.")

try:
    verificar_contraseña()
except Exception as e:
    print(e)