#Int converter to binary, octal, hexa

print("-"*50)
print("{:|<1}{}{:|>1}".format("","Integer Converter".center(48),""))
print("-"*50) 



num = int(input("Please type an whole number:"))
choice = int(input("""Please select the form you want to convert.
1 - Binary

2 - Octal

3 - Hexa
"""))

if choice == 1:
    print("The number {} is {} in Binary.".format(num, bin(num)[2:]))
elif choice == 2:
    print("The number {} is {} in  Octal.".format(num, oct(num)[2:]))
elif choice == 3:
    print("The number {} is {} in hexa.".format(num, hex(num)[2:]))
else:
    print("Invalid Input")