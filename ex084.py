#Read various persons names and weights. Show in the end how many people were registered, how many persons are the lightest and how many ones are the heaviest.

group = []
heavy = []
light = []

#Data receiver.
while(True):
    person = [] # index 0 is name, index 1 is weight.
    person.append(str(input("Type the persons name: ")))
    person.append(str(input("Type his/her weight: ")))
    group.append(person[:]) # adds the typed person information to the group list.

    while(True): #Want to continue question answer verifier.
        choice = str(input("Do you want to continue? (Y/N)")).upper()[0]
        print(choice)
        if choice == "Y" or choice == "N":
            break
        else:
            print("Invalid answer, please try again")
    
    if choice == "N":
        break

print("-"*40)

for p in range(len(group)): # p = person
    if p == 0:
        # w = weight 
        max_w = group[p][1] 
        min_w = group[p][1]
    
    if group[p][1] > max_w:
        max_w = group[p][1] 
    elif group[p][1] < min_w:
        min_w


print(group)       
print(f"MIN: {min_w}")
print(f"MAX: {max_w}")
print("END OF PROGRAM")