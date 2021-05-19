#Leitor de idade e sexo

p18 = m = f20 = 0

while True:
    sex = str(input("Digite o sexo da pessoa: [M/F]")).upper().strip()
    #Validar Dados
    if sex != "M" and sex != "F":
        print("Inválido, tente novamente")
    else:
        age = (input("Digite a Idade da pessoa:"))
        if age.isnumeric() == False:
            print("Tente novamente, dado inválido")
        else: 
            age = int(age)
            
            if age > 18:
                p18 += 1
            
            if sex == "M":
                m += 1

            if sex == "F" and age < 20:
                f20 += 1

            option = str(input("Você deseja continuar registrando pessoas? [Y para continuar]")).upper()
            
            if option != "Y":
                break
print("="*30)
print(f"""\nFoi registrado {p18} pessoas acima de 18 anos;

{m} Homens;

{f20} Mulheres com menos de 20 anos.""")
print("="*30)

print("\n FIM DO PROGRAMA \n")

            

            

        
