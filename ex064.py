#Somador de Números:

num = 0
s = 0
c = 0
lis = []
c2 = 0

while num != 999:
    num = int(input("Please type an integer number to the sum (999 to stop):"))
    if num  != 999:
        lis += [num]
        s += num
        c += 1

print("")

for coun in range(0,c):
    print("Term {:2} == {:4}".format(c2+1, lis[c2]))
    c2 += 1
    
print("\nThe total sum of the {} typed terms is: {}\n".format(c,s))
