#Factorial without math library 

'''num = int(input("Factorial of :"))
fac = num
result = num-1

while fac != 1:
    result = fac*result
    fac -= 1

print("The factorial of {} is {}".format(num, result))'''

num = int(input("Factorial of:"))
num_backup = num
resultado = num

while num != 1:
    resultado = resultado*(num-1)
    num -= 1
    #print("{} |  {}".format(num, resultado))

print("The factorial of {} is {}".format(num_backup, resultado))

