#Comparador de dois números inteiros

num1 = int(input("Por favor digite o primeiro número a ser comparado:"))
num2 = int(input("Por favor digite o segundo número a ser comparado:"))

if num1 == num2:
    print("Os valores {} e {} são iguais.".format(num1, num2))
elif num1 > num2:
    print("O valor {} é maior que {}.".format(num1, num2))
else:
    print("O valor {} é maior que {}.".format(num2, num1))