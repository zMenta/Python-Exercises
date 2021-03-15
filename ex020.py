#Sorteador de ordem de apresentação do professor

from random import sample

nom1 = input("Digite o nome do primeiro aluno:")
nom2 = input("Digite o nome do segundo aluno:")
nom3 = input("Digite o nome do terceiro aluno:")
nom4 = input("Digite o nome do quarto aluno:")

list = [nom1, nom2, nom3, nom4]

print("A ordem dos trabalhos são {}".format(sample(list,4)))

