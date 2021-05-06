#Read various persons names and weights. Show in the end how many people were registered, how many persons are the lightest and how many ones are the heaviest.

group = []
heavy_p = [] #names of people that has the maximum weight 
light_p = [] #names of people that has the minimum weight

#Data receiver.
while(True):
    person = [] # index 0 is name, index 1 is weight.
    person.append(str(input("Type the persons name: ")))
    person.append(int(input("Type his/her weight(kg): ")))
    group.append(person[:]) # adds the typed person information to the group list.

    while(True): #Want to continue question answer verifier.
        choice = str(input("Do you want to continue? (Y/N)")).upper()[0]
        if choice == "Y" or choice == "N":
            break
        else:
            print("Invalid answer, please try again")
    
    if choice == "N":
        break

for p in range(len(group)): # p = person
    if p == 0:
        # w = weight 
        max_w = group[p][1] 
        min_w = group[p][1]
    
    #max weight and min weight verifier.
    if group[p][1] > max_w:
        max_w = group[p][1] 
    elif group[p][1] < min_w:
        min_w = group[p][1]

#Adds the person name to a list if the person has the max weight or the minimum weight registered. And adds on the respective lists.   
for p in range(len(group)):
    if group[p][1] == max_w:
        heavy_p.append(group[p][0][:])
    elif group[p][1] == min_w:
        light_p.append(group[p][0][:])

#Prints for debug.
# print(f"Group: {group}")   
# print(f"HEAVY_P: {heavy_p}") 
# print(f"LIGHT_P: {light_p}")   
# print(f"MIN: {min_w}")
# print(f"MAX: {max_w}")

print("="*65)
print(f"It was registered {len(group)} people.")
print(f"The heaviest weight was {max_w}KG, and it was from {heavy_p}")
print(f"The lightest weight was {min_w}KG, and it was from {light_p}")
print("="*65)
