#Remake do caixa eletrônico

total = int(input("Digite o valor que deseja sacar:"))
nota = 50
cedula = 0

while True:

    if total >= nota:
        total -= nota
        cedula += 1
    else: 
        if cedula > 0:
            print(f"{cedula} de ${nota:.2f}")

        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        else:
            nota = 1
        
        cedula = 0

        if total == 0:
            break

print("FIM")
        
