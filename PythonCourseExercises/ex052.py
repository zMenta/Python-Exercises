#Verificador de número primo

num = int(input("Digite um número inteiro:"))

division = 1

verify = num % num
verify2 = num % 1

"""
if verify == 0 and verify2 == 0 and num != 1:
    print("O número {} é um número primo.".format(num))
else:
    print("O número {} não é primo.".format(num))
"""
#Tests 
'''  
for c in range (1,num+1):
     division = num % c
     print("{} | {}".format(num,c)) 
     if division == 0:
         print("\033[1;32m{} | {}\033[0;0;0m".format(num, c))
'''
divisions_num = 0

for c in range (1,num+1):
    division = num % c
    if division == 0:
         divisions_num += 1
         print("\033[1;32m{} | {}\033[0;0;0m".format(num, c))
    else: 
        print("{} | {}".format(num, c))

if divisions_num == 2:
    print("Isso é um número primo")
else:
    print("Não é um número primo")         