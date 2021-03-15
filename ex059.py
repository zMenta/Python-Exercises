#Primitive "WHILE" Calculator
print("="*20)
print("Calculator!".center(20))
print("="*20)

option = 4
lst = []

while option != 5:
    if option == 4:
        num1 = int(input("Type the first number:"))
        num2 = int(input("Type the second number:"))
    print("="*25)
    option = int(input('''
Escolha uma das opções:

    1 - Somar;
    2 - Multiplicar;
    3 - Maior;
    4 - Novos Números;
    5 - Sair.

Sua escolha:'''))
    print("="*25)

    if option < 1 or option > 5:
        print("Opção Inválida. Por favor digite novamente sua escolha.")
    elif option == 1:
        print("{} + {} == {}".format(num1, num2, num1 + num2))
    elif option == 2:
        print("{} X {} == {}".format(num1, num2, num1 * num2))
    elif option == 3:
        lst = [num1, num2]
        print("{} é maior que {}".format(max(lst), min(lst)))

print("Fim da Calculadora\n")
    

