#Pythagoras Theorem 

from math import sqrt

a = float(input("What is the size of the adjacent side of the 90 degrees triangle:"))
b = float(input("What is the size of the opposite side of the 90 degrees triangle:"))

print("The adjacent side is {:.2f} in length, the Opposite side is {:.2f} . And the hypotenuse is {:.2f}.".format(a, b, sqrt((a**2) + (b**2))))