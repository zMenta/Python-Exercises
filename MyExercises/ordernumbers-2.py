#order numbers from any amount of numbers.

number = []
from time import sleep
from random import randint


qt = int(input("How many numbers you want to type?")) #qt = quantity 

for i in range(1,qt+1):
    # number.append(int(input(f"Type the {i}th number: ")))
    number.append(randint(0,100))
while True:

    for i in range(1,qt):
            if number[i-1] > number[i]:
                number[i-1],number[i] = number[i], number[i-1]

    print(number)
    sleep(0.6)
  
print(number)
