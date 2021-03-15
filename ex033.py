#Comparador de números

n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
n3 = int(input("Digite o terceiro número:"))

#Definidor de menor número
if n1 < n2 and n1 < n3: 
    l_num = n1
elif n2 < n1 and n2 < n3:
    l_num = n2
elif n3 < n2 and n3 < n1:
    l_num = n3


#Definidor de maior número
if n1 > n2 and n1 > n3:
    h_num = n1
elif n2 > n1 and n2 > n3:
    h_num = n2
elif n3 > n2 and n3 > n1:
    h_num = n3

print("-="*10)
print("O Menor número é {}. \nE o Maior número é {}".format(l_num, h_num))
print("-="*10)
