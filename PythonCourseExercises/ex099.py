#Create a function that returns the biggest number.

def line(*x): #x = 1(or any number) is with line break | Default is no line break
    if len(x) > 0:
        print()
    print("-="*30)

def big(*num):
    line()
    print(f"From the number(s) {num} the biggest is: {max(num)}")

def big2(*num): #Max number without the max() function
    line()
    if len(num) == 0:
        print(f"No numbers were typed.")
    else:
        for i,n in enumerate(num): #i = index | n = number
            if i == 0:
                #m = max
                m = n
            elif n > m:
                m = n
        print(f"From the number(s) {num} the biggest is: {m}")

#Main Body

big2(2,4,5,8)

big2(0,8,2,152,6)

big2(6,2,9)

big2(0)

big2(6)

big2()

line()