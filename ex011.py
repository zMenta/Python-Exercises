# Calculador de metros quadrados e quanta tinta é necessária para pintá-la , cada litro de tinta equivale a 2 metros quadrados.

n1 = float(input("Qual a medida vertical da sua parede?"))
n2 = float(input("Qual é a medida horizontal da sua parede?"))

m2  = n1*n2

print("Você vai precisar usar {} litros de tinta para pintar sua parede de {} metros quadrados".format(m2/2, m2))