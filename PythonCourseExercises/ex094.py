#Name,gender,age reader. Appends the person into a list.
#Person is a dictionary.
# 1) Show the average of age and who's age is greater or lower than the average.
# 2) Show all the female names.
# 3) The amount of people registered.

people = {
    "name": "",
    "gender": "",
    "age": 0
}

group = []

while True:
    people["name"] = input(str("Please type the name of the person: "))
    #-While Validate if the gender answer is either m or f.
    while True: 
        people["gender"] = input(str("Please type it's gender [m/f]: ")).upper()[0]
        if people["gender"] in "FM":
            break
        else:
            print("Invalid answer. Please try again")
    people["age"] = int(input(f"Please type {people['name']} age: "))

    #Appends the registered person to group
    group.append(people.copy())
    
    #-While Asks and verifies if the user wants to register another person
    while True: 
        answer = input(str("Do you want to register another person? [y/n]")).upper()
        if answer != "N" and answer != "Y":
            print("Invalid answer. Please try again.")
        else:
            break
        
    if answer == "N":
        break
    
    print("="*40)

print("-"*50)
for i in group:
    print(i)
