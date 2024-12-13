from collections import Counter

mensaje = "ABCDabcdABCDabcd"

contador = Counter(mensaje)

max_frecuencia = max(contador.values())

caracteres_frecuentes = [caracter for caracter, frecuencia in contador.items() if frecuencia == max_frecuencia]

print(f"Los caracteres que más se repiten con {max_frecuencia} repeticiones son:")
for caracter in caracteres_frecuentes:
    print(f"- {caracter} ({caracter.upper() if caracter.islower() else caracter})")