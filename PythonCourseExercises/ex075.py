#Leitor de 4 números e retorna informações sobre números digitados. (usando Tupples)

num =  (int(input("1Digite um número:")),
        int(input("2Digite um número:")),
        int(input("3Digite um número:")),
        int(input("4Digite um número:")),)

print(f"O número 9 apareceu {num.count(9)}")
if 3 in num:
    print(f"O número apareceu na posição {num.index(3)+1}")
else:
    print(f"O número 3 não foi encontrado.")
print(f"Os números pares dessa Tupla são: ", end="")
for c in num:
    if c % 2 == 0:
        print(c , end=", ")
