#Create a function that counts 1 to 10, 10 to 0 with pace of 2 and a custom counting.

from time import sleep

#start, end, c 

def line(*x): #x = 1(or any number) is 'with line break' | Default is 'no line break'
    if len(x) > 0:
        print()
    print("-="*19)

def count():
    line()
    for i in range(11): #print numbers 1 to 10
        print(f"{i}",end="")
        if i < 10: #if verifies if there's need to print a comma
            print(", ",end="")

    line(1)
    while i >= 0:
        print(f"{i}", end="")
        if i != 0:
            print(f", ",end="")
        i -= 2

    #Get data from the user.
    line(1)
    start = int(input("Type the starting number to count: "))
    end = int(input("Type the ending number: "))
    pace = int(input("Type the pace of the counting: "))
    num = start
    line()

    # Verifies if pace is 0. If pace 0, pace = 1
    if pace == 0: 
        pace = 1

    #Print the couting.
    if start < end:
        while num <= end:
            print(f"{num} ,",end="")
            num += pace
    else:
        if pace > 0: #Verifies if the pace is negative or positive. Determines wich counting method is the best fit.
            while num >= end:
                print(f"{num} ,",end="")
                num -= pace
        else:
            while num >= end:
                print(f"{num} ,",end="")
                num += pace

    line(1)

#Main body

count()
