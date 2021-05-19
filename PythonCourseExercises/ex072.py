#Leitor de número inteiro que diz o número digitado em cursivo.

NUMBERS = ("zero", "um" , "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove" , "dez")

while True:

    # verificador de dados digitados
    while True:
        choice = " "
        num = int(input("Digite um número entre 0-10:"))
        if num >= 0 and num <= 10:
            break
        print("Tente novamente.", end=" ")
        

    print(f"Você digitou o número {NUMBERS[num]}.\n")

    #Verificador se a pessoa quer continuar
    while choice not in "SN":
        while True:
            choice = str(input("Queres continuar? [s/n]").upper().strip()[0])
            if choice != "N" and choice != "S":
                print("Opção inválida, tente novamente.", end=" ")
            else:
                break

    if choice == "N":
        break
    
print("FIM")
