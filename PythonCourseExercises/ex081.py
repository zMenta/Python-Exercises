# Type list and check how many numbers were typed, put in inversed ordened order and check if the number 5 was typed.

choice = "Y"
numbers = []

while choice == "Y":
    numbers.append(int(input("Type a number: ")))
    choice = input("Want to type one more number? (Y for yes)")[0].upper()


print("-"*30)
print(f"You typed {len(numbers)} numbers!")

numbers = sorted(numbers, reverse = True)
print(f"The descending order of the list is:  {numbers}")

if 5 in numbers:
    print("You typed the number 5.")
else:
    print("You didn't typed the number 5.")
print("-"*30)
