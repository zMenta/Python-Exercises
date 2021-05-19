#Calculador de aumento de salário

saly = float(input("Digite um salário e veja seu aumento:"))



'''
if saly <= 1250:
    print("Seu novo salário é de: ${:.2f}".format(saly*1.15))
else:
    print("Seu novo salário é de: ${:.2f}".format(saly*1.10))
'''

#Cleaner method 

if saly <= 1250: 
    novo = saly*1.15
else:
    novo = saly*1.10

print("Seu novo salário é de ${:.2f}".format(novo))