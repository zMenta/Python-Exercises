#Read 5 values and show the max and min values of the list

numbers = []

for i in range(5):
    numbers.append(int(input(f"Type the number of {i}th postion: ")))

print("-="*40)

print(f"You typed the following numbers: {numbers}")

print(f"The highest number that you typed is {max(numbers)} in the {numbers.index(max(numbers))}th position",end="")

if numbers.count(max(numbers)) > 1:
    for i in range(numbers.count(max(numbers))):

        position = numbers.index(max(numbers))
        
        print(f"IS IN THE {position}th POSITION")

