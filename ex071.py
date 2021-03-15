#Caixa eletrônico, com cédulas de $50 $20 $10 e $1 

print("="*40)
print("CAIXA ELETRÔNICO".center(40))
print("="*40)

nota50 = nota20 = nota10 = nota1 = total = 0

num = int(input("Digite o valor que deseja sacar:"))


while True:

    if num >= 50:
        result = int(num/50)
        nota50 += result
        num -= result*50
    elif num >= 20:
        result = int(num/20)
        nota20 += result
        num -= result*20
    elif num >= 10:
        result = int(num/10)
        nota10 += result
        num -= result*10
    else:
        nota1 = num
        num -= num

    if num == 0:
        break


print("-"*40)
print(f"Total de notas de $50: {nota50}")
print(f"Total de notas de $20: {nota20}")
print(f"Total de notas de $10: {nota10}")
print(f"Total de notas de $1: {nota1}")
print("")
    