#Calculador de IMC
#IMC = peso/ altura**2

kg = float(input("How much do you weight(kg)?"))
height = float(input("How tall are you(cm/meters)?"))

#Converter, cm to meters.
if height > 3.50:
    height = height/100
    
imc = kg / height**2

if imc <= 18.5:
    print("Seu imc é {:.1f} ,você está abaixo do peso.".format(imc))
elif imc <= 25:
    print("Seu imc é {:.1f} , você está com peso ideal.".format(imc))
elif imc <= 30:
    print("Seu imc é {:.1f} , você está acima do peso.".format(imc))
elif imc <= 40:
    print("seu imc é {:.1f} , você está obeso.".format(imc))
else:
    print("Seu imc é {:.1f} , você é um obeso mórbido.".format(imc))