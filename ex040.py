#Calculador de nota

n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a segunda nota:"))

average = (n1 + n2) / 2

if average > 7:
    print("APROVADO, nota final: {}".format(average))
elif 5 < average < 6.9:
    print("RECUPERAÇÃO, nota final: {}".format(average))
else:
    print("REPROVADO, nota final: {}".format(average))