#caixa eletrônico melhor
#Cédulas de 50 , 20 , 10 e 1

total = num = int(input("Digite o Valor a ser sacado:"))
nota = 50
cedula = 0
while True:
    
    if total >= 50:
        total -= nota
        cedula += 1
        if cedula >= 1 and total < 50:
            print(f"Total de Cédulas de $50: {cedula}")
            cedula = 0
    elif total >= 20:
        nota = 20
        total -= nota
        cedula += 1
        if cedula >= 1 and total < 20:
            print(f"Total de Cédulas de $20: {cedula}")
            cedula = 0
    elif total >= 10:
        nota = 10
        total -= nota
        cedula += 1
        if cedula >= 1 and total < 10:
            print(f"Total de Cédulas de $10: {cedula}")
            cedula = 0
    else:
        cedula = total
        total -= cedula
        print(f"Total de Cédulas de $1: {cedula}")

    if total == 0:
        break

print("FIM")
    
        
