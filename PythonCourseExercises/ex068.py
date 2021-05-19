#Jogo de par ou ímpar 

from random import randint

#Colors: 1 = red ,  2 = green
color = {
    1: "\033[1;31m{}\033[0;0;0m",
    2: "\033[1;32m{}\033[0;0;0m"
}

w = 0

while True:
    pc_num = randint(1,10)
    s = 0

    choice = str(input("Você escolhe par ou ímpar? (P/I)")).upper()

    #Validação de Dados
    if choice != "P" and choice != "I":
        print("Dados inválidos, por favor tente novamente")
    else:
        hu_num = int(input("Qual número você escolhe para jogar?"))
        

        s = pc_num + hu_num

        #Impar ou Par
        if s % 2 == 0:
            result = "Par"
        else:
            result = "Ímpar"


        #Condição de vitória
        if result == "Par" and choice == "P":
            vitoria = True
        elif result == "Ímpar" and choice == "I":
            vitoria = True
        else:
            vitoria = False

        #Seleção de palavra e contador de vitórias
        if vitoria == True:
            word = f"{color[2]}".format("Ganhou")
            w += 1
        else:
            word = f"{color[1]}".format("Perdeu")

        print(f"Você {word}. {hu_num} + {pc_num} = {s}, é um número {result}")

        if vitoria == False:
            print(f"\nFIM DO JOGO. você conseguiu ter {w} vitórias consecutivas!\n")
            break
        
        