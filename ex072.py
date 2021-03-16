#Leitor de número inteiro que diz o número digitado em cursivo.

NUMBERS = ("zero", "um" , "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove" , "dez")

num = int(input("Digite um número entre 0-10:"))

print(f"Você digitou o número {NUMBERS[num]}.\n")
