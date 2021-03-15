#Somador de Números pares

summ = 0

for c in range(0,6):
    num = int(input("Digite um número:"))
    if (num % 2) == 0:
        summ += num
print("A soma de todos os valores pares digitados é: {}".format(summ))
