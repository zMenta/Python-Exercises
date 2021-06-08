#Create an algorithm that has 4 players that throws a dice(random number from 1 to 6). Place the results in a dictionary, later on sort this dictionary, knowing that the winner is who got the highest number of the die.

from random import randint
from time import sleep

game = {}
sort = {}

for i in range(1,5): #Randomize a value for each player.
    game[f"Player{i}"] = randint(1,6)

print("="*50)
print("Dice Resuts:")
for k,v in game.items():
    print(f"{'':5}The {k} played {v} from the dice.")
    sleep(0.2)

Sorted = False
g = 0
high = game["Player1"]

while Sorted is not True:
    for i in game.values(): #Check for the highest Dice played from the players. And assign the respective value to the high variable.
        if i > high:
            high = i
            
    for i in game.keys(): #Check which player(s) has the highest score and add to the sort dictionary and pop it on the game dictionary.
        if game[f"{i}"] == high:
            sort[f"{i}"] = game[f"{i}"]

    if g == 4:
        Sorted = True

    g += 1

print(sort)
print(game)


print("Game Result:")


# NEEDS WORK | NOT FINISHED