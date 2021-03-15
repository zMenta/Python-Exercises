#Pagamentos à vista e parcelado

#tela inicial
print("~"*70)
print("{:|<1}{}{}{:|>1}".format(""," "*10, "Por favor digite o valor de sua compra:".center(58), ""))

price = float(input("{:|<1} -Preço R$ ".format("")))

print("-"*70)
print("{:|<1}{}{:|>1}".format("", "Por favor escolha uma das formas de pagamento:".center(68), ""))
print("{:|<1}{}{:|>1}".format("", "Digite 1 para pagar em Dinheiro:".center(68), ""))
print("{:|<1}{}{:|>1}".format("", "Digite 2 para pagar com cartão de débito:".center(68), ""))
print("{:|<1}{}{:|>1}".format("", "Digite 3 para pagar com cartão e parcelar o valor:".center(68), ""))
print("-"*70)

pay_method = int(input("{:|<1} -Digite o método de pagamento:".format("")))

if pay_method == 1:
    print("O valor total a ser pago é R${:.2f}. 10% de desconto do valor{:.2f}".format(price*0.9, price))
elif pay_method == 2:
    print("O valor total a ser pago é R${:.2f}. 5% de desconto do valor{:.2f}".format(price*0.95, price))
elif pay_method == 3:
    parcela = int(input("Digite em quantos mesês você deseja parcelar a compra."))
    if parcela <=2 and parcela >= 1:
        preco_parcela = price / parcela
        print("O valor de cada parcela é R${} , O valor final da compra foi{}".format(preco_parcela, price))
    elif parcela >= 3:
        preco_parcela = (price*1.2) / parcela
        print("O valor de cada parcela é R${:.2f} , O valor final da compra foi {}, com 20% de juros do valor original de {}".format(preco_parcela, price*1.2, price))
    else:
        print("Valor inválido.")
else:
    print("Númeor inválido")
