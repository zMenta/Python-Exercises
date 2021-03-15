# SILVA name finder

name = input("Digite um nome de uma pessoa:").strip()

print("Seu nome tem Silva nele? {} ".format(name.upper().find("SILVA") != -1))