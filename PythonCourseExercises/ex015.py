#Aluguel de carros

dia = int(input("Quantos dias o carro foi alugado?"))
km = float(input("Quantos KM foi percorrido com o carro?"))

print("O valor a ser pago é de: {:.2f}".format((dia*60)+(km*0.15)))