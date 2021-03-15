#Média de vários valores

choice = "Y"

while choice == "Y":
    c = 1
    lis = []
    s = 0 
    i = 0
    num = 0

    while c != 0:
        num = float(input("Digite um dos valores da média (0 to stop):"))
        c = num
        if num != 0:
            i += 1
            s += num
            lis += [num]
    print("Higher:{} || Lower: {}".format(max(lis), min(lis)))
    print("The average of all numbers typed is: {}".format(s / i))
    choice = str(input("Want to continue: (Y for yes)")).upper()

print("\033[1;31mEND OF THE PROGRAM\033[0;0;0m")
    