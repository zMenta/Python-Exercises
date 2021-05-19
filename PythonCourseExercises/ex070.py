#Leitro de compras 
print("="*40)
print("CAIXA DAHORA".center(40))
print("="*40)

minimo = big = total = 0

while True:
    choice = " "
    product = str(input("Digite o nome do produto:"))
    while True:
        preco = float(input("Digite o valor de sua compra:"))
        if preco <= 0:
            print("Valor inválido, digite novamente o preço.")
        else: 
            break
    while choice not in "SN":
        choice = str(input("Você quer continuar [s/n]?")).upper().strip()[0]
     
    if minimo == 0:
        minimo = preco
        low_product = product
    elif minimo > preco and preco > 0:
        minimo = preco
        low_product = product

    if preco > 1000:
        big += 1

    total += preco

    if choice == "N":
        break

print(f"\n O total de sua compra foi R${total:.2f}.")
print(f"\n Teve {big} produtos acima de R$1000.00")
print(f"\n O produto com o menor preço foi {low_product}, que custou R${minimo:.2f}.\n")



