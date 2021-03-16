#Random numbers in Tupple, return the higher and the lower.

from random import randint

numbers = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
order = ""

for c in numbers:
    order += str(c) + ", "

print(f"The random order that was chosen is {order}") 
print(f"The highest number was {max(numbers)}, and it was found {numbers.count(max(numbers))} of the highest number in the tupple.")
print(f"The lowest number was {min(numbers)}")
