#order numbers from any amount of numbers.

number = []


qt = int(input("How many numbers you want to type?")) #qt = quantity 

for i in range(1,qt+1):
    number.append(int(input(f"Type the {i}th number: ")))
print(number)

while number[0] > number[1]:
    for i in range(1,qt):
        while number[i-1] > number[i]:
            if number[i-1] > number[i]:
                number[i-1],number[i] = number[i], number[i-1]
            
    
print(number)
