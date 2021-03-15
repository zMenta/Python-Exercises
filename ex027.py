# Separador de primeiro e último nome

name = input("Digite seu nome:").split()


print("Seu primeiro nome é: {}".format(name[0].title()))
print("Seu último nome é: {}".format(name[-1].title()))
