#order numbers from any amount of numbers.

from time import sleep
from random import randint

number = []
sort = True


qt = int(input("How many numbers you want to type?")) #qt = quantity 

for i in range(1,qt+1):
    # number.append(int(input(f"Type the {i}th number: ")))
    number.append(randint(0,100))

print(f"INITIAL NUMBER {number}")

while sort:
    num_change = number[:]
    
    for i in range(1,qt):
            if number[i-1] > number[i]:
                number[i-1],number[i] = number[i], number[i-1] 

    if num_change == number:
        sort = False
           
print(f"SORTED LIST: {number}")
