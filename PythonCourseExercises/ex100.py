#Create a function that randomize 5 numbers in a list and other function that do a sum of all the numbers.

from random import randint
from time import sleep

#Variables

numbers = []

#Functions
def rand(var):
    for i in range(5):
        var.append(randint(0,10))

def tot(var):
    total = 0
    for i in var:
        total += i
    return total

#Main body
rand(numbers)

print("The random numbers: ",end="")
for i in numbers:
    print(f"{i}, ",end="")

print(f"\nThe sum of the numbers: {tot(numbers)}")

