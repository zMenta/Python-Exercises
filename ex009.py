#Mostrar tabuado de X num 

n = int(input("Digite um número para sua tabuada:"))

print("{:-<15}".format(""))
print(" x1 == {:4}\n x2 == {:4}\n x3 == {:4}\n x4 == {:4}\n x5 == {:4}".format(n, n*2, n*3, n*4, n*5))
print(" x6 == {:4}\n x7 == {:4}\n x8 == {:4}\n x9 == {:4}\nx10 == {:4}".format(n*6, n*7, n*8, n*9, n*10))
print("-" * 15 )