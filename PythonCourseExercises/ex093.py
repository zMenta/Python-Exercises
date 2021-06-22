#Create an algorithm that asks for a name of football player and how many matches he/she played.
#Ask for how many goals the player made in each match.
#Print the player stats afterwards.

stats = { #Player stats
    "name": "",
    "goals": [],
    "total": 0
} 

stats["name"] = (input("Please type the player name: "))
matches = int(input(f"Please type how many matches {stats['name']} played:"))

#Asks for each match results and adds to the total of goals.
for i in range(matches):
    stats["goals"].append(int(input(f"Goals made in {i}th match: "))) 
    stats["total"] += stats["goals"][i]

print("-="*30)
print(stats)
print("-="*30)

#print the keys and respective values
for key,value in stats.items():
    print(f"The field '{key}' has the value of {value}")
print("-="*30)

#Print each match result

print(f"The player {stats['name']} played a total of {len(stats['goals'])} matches.")
for i in range(len(stats["goals"])):
    print(f"{'':5} -> In the {i}th match, scored {stats['goals'][i]} goals.")
print(f"A total of {stats['total']} goals")
print("-="*30)

