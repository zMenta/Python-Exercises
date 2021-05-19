# somador de múltiplo de 3 , 1-500
s = 0
quantity = 0
for c in range(0,500,3):
    if c > 0:
        print(c)
        s += c
        quantity += 1
print("A soma de todos os múltiplos de 3 entre 1-500 é --> {}".format(s))
print(quantity)