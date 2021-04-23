# List of numbers and make another list with even and odd numbers of the first list.

choice = 'Y'
numbers = []
odd_list = []
even_list = []

while choice == "Y":
    numbers.append(int(input("Type an number: ")))
    choice = input("Want to continue? (y for yes)")[0].upper()

#Even or odd number verifier, then append the number to the corresponding list.
for i in range(0,len(numbers)):
    if numbers[i]%2 == 0:
        even_list.append(numbers[i])
    else:
        odd_list.append(numbers[i])

#print results
print("-"*30)
print(f"Typed list: {numbers}")
print(f"Even list: {even_list}")
print(f"Odd list: {odd_list}")
print("-"*30)
