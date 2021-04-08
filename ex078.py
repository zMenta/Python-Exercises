#Read 5 values and show the max and min values of the list

numbers = []

for i in range(5):
    numbers.append(int(input(f"Type the number of {i}th postion: ")))

print("-="*40)

print(f"You typed the following numbers: {numbers}")

print(f"The highest number that you typed is {max(numbers)}, and it is on the",end="")

#Highest number position verifier 
for posi,index in enumerate(numbers):
    if index == max(numbers):
        print(f" {posi}th,",end="")
print(" position.")

print(f"And the lowest number that you typed is {min(numbers)}, and it is on the",end="")

#Lowest number position verifier
for posi,index in enumerate(numbers):
    if index == min(numbers):
        print(f" {posi}th,",end="")
print(" position.")

print("-"*80)