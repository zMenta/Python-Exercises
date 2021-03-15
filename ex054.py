#Contador de idade de pessoas

import datetime

quantidade = int(input("Quantas pessoas vão ter suas idades contadas?"))
atual = datetime.date.today().year
velhos = 0
#print(atual)

for c in range(1,quantidade+1):
    ano = int(input("Digite um ano de nascimento:"))
    idade = atual - ano
    if idade >= 21:
        velhos += 1
    
jovens = quantidade - velhos

print("Entre as {} pessoas, {} são maiores de idade. \n{} são Menores de idade".format(quantidade, velhos, jovens))        
