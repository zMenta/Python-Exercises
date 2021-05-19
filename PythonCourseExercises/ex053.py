#Verificador de Políndromo

#string with no spaces
name = str(input("Por favor digite algo, e veremos se ela é um Políndromo:"))
name_no_spaces = name.replace(" ", "").upper()
lenght = len(name_no_spaces)
counter = -1
inver_name = ""


#Tests
'''
for c in range(0,lenght):
    print("{} | {}".format(c, name[c]))

print("-"*15)    

for c in range(0,lenght):
    inver_name += name[-counter]
    print("{} ~ {}".format(name[c], name[-(counter)]))
    counter += 1

print(inver_name)
'''

for c in range(0, lenght):
    inver_name += name_no_spaces[counter]
    counter -= 1


if name_no_spaces == inver_name:
    print("A palvara '{}' é um Políndromo.".format(name))
else:
    print("Esta palavra '{}' Não é um Políndromo.".format(name))


