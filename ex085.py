#Read 7 numbers, separate odd and even number inside other list. Afterwards show the even and odd numbers sorted.

numbers = [[],[]] #Index 0 -> Even numbers. Index 1 -> Odd Numbers

for i in range(7):
    num = int(input("Type an number: "))

    if num%2 == 0:
        numbers[0].append(num)
    else:
        numbers[1].append(num)
    
numbers[0].sort()
numbers[1].sort()

print("-"*40)
print(f"Even numbers typed: {numbers[0]}")
print(f"Odd numbers typed: {numbers[1]}")
