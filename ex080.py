#Inserting numbers in list and sorting it, without sort() method

numbers = []

for i in range(5):
    
    num = int(input("Type an number: "))

    #Insert any number typed if the list has no numbers inside it.
    if len(numbers) == 0:
        numbers.insert(0, num)
    else:

        #Number Placement Verifier 
        if num >= max(numbers):
            numbers.insert(i+1, num)
        else:
            for c in range(len(numbers)):
                if num < numbers[c] and num not in numbers:
                    numbers.insert(c, num)
    
print("="*30)
print(numbers)
