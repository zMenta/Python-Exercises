#Number inserter in list, don't insert if the number typed is repeated.

numbers = []
choice = "Y"

#Want to continue verifier.
while choice == "Y":

    num = int(input("Type a number: "))

    #Typed number verifier
    if num not in numbers:
        numbers.append(num)
        print("Number added successful.")
    else:
        print("Number is already in the list.")

    choice = input("Want to continue? [Y/N]").upper()

numbers.sort()

print(f"\nThe numbers that you typed are: {numbers}")

print("="*30)
print("END".center(30))
print("="*30)