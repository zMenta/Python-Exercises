#Leitor de ano Bissexto

ano = int(input("Digite um ano."))

if (ano % 4 )== 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} foi bissexto.".format(ano))
else:
    print("O ano {} não foi bissexto.".format(ano))