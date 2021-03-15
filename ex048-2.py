#Contador de 1-500 de todos os múltiplos de 3 (numéros ímpares)

s = 0
contador = 0

for c in range(1,500,2):
    if (c%3) == 0:
        contador += 1
        s += c
        print(c)
        
print(s)
print(contador)