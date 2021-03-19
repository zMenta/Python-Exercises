#Leitor de 4 números e retorna informações sobre números digitados. (usando Tupples)


tupla = ()

for c in range(0,4):
    num = tuple(input("Type an number:"))
    tupla += num
    
print(tupla)

print(f"O número 9 apareceu {tupla.count(9)} vezes")
print(f"O 3 foi primeiramente digitado na posição {tupla.index(3)}")
#print(f"Apareceu {} números pares.")


