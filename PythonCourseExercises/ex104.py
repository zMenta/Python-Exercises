#Create a function similar to input(), but it can only accept int values on it.

# help(input)

def inputInt(prompt=None):
    """
    prompt -> string text

    Only return the input answer if is an integer number.
    """
    passed = False
    while not passed:     
        try:
            num = int(input(prompt))
            passed = True
        except:
            print("\033[1;31;40mERROR! Not a integer number!\033[0;0;0m")
            passed = False
    return num

#Main body

n = inputInt("Type an integer number: ")
print(f"You typed the number {n}")

# print("\033[1;31;40mTEXT EXAMPLE TEXT\033[0;0;0m")
