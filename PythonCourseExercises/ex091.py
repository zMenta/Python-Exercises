#Create an algorithm that has 4 players that throws a dice(random number from 1 to 6). Place the results in a dictionary, later on sort this dictionary, knowing that the winner is who got the highest number of the die.

from random import randint
from time import sleep
from operator import itemgetter

game = {}
ranking = {}

for i in range(1,5): #Randomize a value for each player.
    game[f"Player{i}"] = randint(1,6)

print("="*50)
print("Dice Resuts:")
for k,v in game.items():
    print(f"{'':5}The {k} played {v} from the dice.")
    sleep(0.2)

ranking = sorted(game.items(), key=itemgetter(1), reverse=True)
print(ranking)
