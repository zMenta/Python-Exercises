#Tabuada que interrompe com número negativo

c = 1

while True:
    num = int(input("Por favor digite o número da tabuada:"))

    if num < 0:
        break

    print("-"*45)

    while c <= 10:
        print(f"{num:2} x {c:2} = {num*c:3}")
        c += 1

    print("-"*45)
    c = 1

print("\033[1;32mFim do Progama\033[0;0;0m\n")
       