#Tangent, cos and sin calculator.

from math import cos,sin,tan,radians

num = float(input("Type an angle and be happy:"))


print("The Cos, Sin and Tangent of {} is:\nCos:{:.2f}\nSin{:.2f}\nTan{:.2f}".format(num, cos(radians(num)), sin(radians(num)), tan(radians(num))))