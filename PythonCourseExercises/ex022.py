frase = input("Digite um nome:").strip()
short_frase = frase.split()
name_num = len("".join(short_frase))

print("O nome com letras maiúsculas é: {}".format(frase.upper()))

print("O nome com letras minúsculas é: {}".format(frase.lower()))

#print("O número de letras em seu nome é: {}".format(str(name_num)))
print("O número de letras em seu nome é: {}".format(len(frase) - frase.count(" ")))

print("Seu primeiro nome tem {} letras.".format(str(len(short_frase[0]))))