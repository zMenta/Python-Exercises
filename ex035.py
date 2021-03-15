#Triangle checker

a = float(input("Digite o lado A do triângulo:"))
b = float(input("Digite o lado B do triângulo:"))
c = float(input("Digite o lado C do triângulo:"))

if a < b+c and b < c+a and c < a+b:
    print("You can make a Triangle.")
else:
    print("You CAN't make a Triangle.")