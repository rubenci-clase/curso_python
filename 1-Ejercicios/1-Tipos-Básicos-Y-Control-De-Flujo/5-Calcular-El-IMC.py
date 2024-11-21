peso = float(input("Introduce tu peso:"))
altura = float(input("Introduce tu altura:"))

imc = float(peso/(altura*altura))

if(imc < 18.5):
    print("IMC bajo")
elif(imc < 25):
    print("IMC normal")
else:
    print("IMC alto")