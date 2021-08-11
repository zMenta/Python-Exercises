#Create a factorial function that has an optional parameter to show the calculus.

def fac(num=1,show=False):
    """
    Factorial function.

    Show -> If true, shows the process of calculation.
    """
    f = 1 #f = factorial
    for i in range(num,0,-1):
        f *= i

    if not show:
        print(f"The factorial of {num} is {f}")
    else:
        for i in range(num,0,-1):
            print(f"{i}",end="")
            if i != 1:
                print(" x ",end="")
        print(f" = {f}")

#Main Body

fac(5,True)
fac(4)
fac(7,True)
fac()

