#Triangle chekcer with triangle type output.

a = float(input("Please type the A side of the triangle:"))
b = float(input("Please type the B side of the triangle:"))
c = float(input("Please type the C side of the triangle:"))

if (a < b+c and b < a+c and c < a+b) == False:
    print("You can't make a triangle with these values!")
elif a == b == c:
    print("Seu triângulo é Equilátero.")
elif a != b != c:
    print("Seu triângulo é Escaleno.")
else:
    print("Seu triângulo é Isósceles.")
