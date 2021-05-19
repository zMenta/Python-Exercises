#Number inserter in list, don't insert if the number typed is repeated. 
#V2

numbers = []

for i in range(5):
    num = int(input("Type an number: "))

    #Append num if it's the first list item or is the higher number from the numbers list.
    if i == 0 or num >= numbers[-1]:
        numbers.append(num)
    else:
        for index in range(0,len(numbers)):
            if num <= numbers[index]:
                numbers.insert(index, num)
                break

print(numbers)
