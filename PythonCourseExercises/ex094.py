#Name,gender,age reader. Appends the person into a list.
#Person is a dictionary.
# 1) Show the average of age and who's age is greater than the average age. 
# 2) Show all the female names.
# 3) The amount of people registered.

people = {
    "name": "",
    "gender": "",
    "age": 0
}

group = []
sum_age = 0

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
    sum_age += people["age"]

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
print(f"The amount of people registered: {len(group)}")
print("All the female names: ",end="")
for person in group:
    if person["gender"] == "F":
        print(f"{person['name']},",end=" ")
print(f"The average of the ages is: {sum_age/len(group)}")
print("List of people that have the age greater than the average: ")
for person in group:
    if person["age"] > sum_age/len(group):
        print(f"{'':5}Name: {person['name']:10} | Gender: {person['gender']:4} | Age: {person['age']:4}")
