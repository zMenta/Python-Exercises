#Sorteando Alunos

from random import choice

nom1 = str(input("Escreva o nome do primeiro aluno:"))
nom2 = str(input("Escreva o nome do segundo aluno:"))
nom3 = str(input("Escreva o nome do terceiro aluno:"))
nom4 = str(input("Escreva o nome do quarto aluno:"))

list = [nom1, nom2, nom3 ,nom4]

print("Parabéns {}, você foi escolhido para limpar o quadro.".format(choice(list)))
