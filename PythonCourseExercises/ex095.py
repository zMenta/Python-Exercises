#Create an algorithm that asks for a name of football player and how many matches he/she played.
#Ask for how many goals the player made in each match.
#Print the player stats afterwards.
#
#Upgraded version of ex93.
#Register multiple players and being able to check their stats afterwards

stats = { #Player stats
    "name": "",
    "goals": [],
    "total": 0
} 

player = []

while True:
    stats["goals"].clear()
    stats["total"] = 0

    stats["name"] = (input("Please type the player name: "))
    matches = int(input(f"Please type how many matches {stats['name']} played:"))

    #Asks for each match results and adds to the total of goals.
    for i in range(matches):
        stats["goals"].append(int(input(f"Goals made in {i}th match: ")))
        stats["total"] += stats["goals"][i]

    player.append(stats.copy())
    #Make a proper copy of the "goals" list inside stats{}
    list_copy = stats["goals"]
    player[-1]["goals"] = list_copy[:]
    

    #Checks if the user wants to register another player 
    while True:
        choice = str(input("Want to register another player? [y/n]")).upper()
        if choice == "Y" or choice == "N":
            break
        else:
            print("Invalid answer. Please try again")

    if choice == "N":
        break

# Functions

#P == specific player
def p_keyvalues(p):
    #print the keys and respective values
    for key,value in player[p].items():
        print(f"The field '{key}' has the value of {value}")

#P == specific player
def match_result(p):
    # #Print each match result
    print(f"The player {player[p]['name']} played a total of {len(player[p]['goals'])} matches.")
    for i in range(len(player[p]["goals"])):
        print(f"{'':5} -> In the {i}th match, scored {player[p]['goals'][i]} goals.")
    print(f"A total of {player[p]['total']} goals")

# for i in range(len(player)):
#     print(p_keyvalues(i))
#     print("-"*35)
#     print(match_result(i))
#     print("=-"*20)

print("-"*45)
print(f"|{'Code':^6}|{'Name':^8}|{'Total':^7}|{'Goals':^20}")
print(f"|{'':-^6}|{'':-^8}|{'':-^7}|{'':-^20}")
for p in range(len(player)):
    print(f"|{p:^6}|{player[p]['name']:8}|{player[p]['total']:^7}|{'':5}{player[p]['goals']}")
    print(f"|{'':-^6}|{'':-^8}|{'':-^7}|{'':-^20}")

#-While, asks if the user wants to check for a specific player data.
while True:
    #Ask the user if he wants to check a player stats.
    while True:
        choice = str(input("Want to check for a specific player? [y/n]")).upper()
        if choice != "N" and choice != "Y":
            print("Invalid answer. Please try again")
        else:
            break
    if choice == "N":
        break

    #Ask for the player code and verifies it
    while True:
        code = int(input("Please type the code of the player: "))
        if code not in range(len(player)):
            print("Invalid Code. Please Try again:")
        else:
            break

    #Options for the info.
    while True:
        option = int(input("1 - Match Results | 2 - Stats | 3 - Exit"))
        if option == 1:
            print(match_result(code))
        elif option == 2:
            print(p_keyvalues(code))
        elif option == 3:
            break
