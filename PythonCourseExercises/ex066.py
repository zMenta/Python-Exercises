#Somador de números

s = n = 0


while True:
    num = int(input("Digite um número a ser somado:"))
    if num == 999:
        break
    s += num
    n += 1

print(f"Você digitou {n} número e a soma deles é {s}.")