#Leitor de 4 números e retorna informações sobre números digitados. (usando Tupples) V2

num = tuple(int(input("digite um valor:"))for c in range(0,4))

print(f"O número 9 aparece {num.count(9)} vezes")
try:
    print(f"O número 3 aparece primeiro na posição {num.index(3)+1}")
except:
    print("O número 3 não aparece")

print("Apareceu os seguintes números pares: ", end="")
for c in num:
    if c % 2 == 0:
        print(c, end=", ")
        


