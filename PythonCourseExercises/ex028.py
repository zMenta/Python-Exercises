#Guess the number game

from random import randint

rng_num = randint(0,5)

player_num = int(input("Try to guess the number between 0-5, good luck!"))

if player_num < 0 or player_num > 5:
    print("Invalid Number")
elif player_num == rng_num:
    print("Congratulation! You guessed the number {}. You won! ".format(rng_num))
else:
    print("Sorry, you didn't guessed the number. The computer chose {}, you guessed the number {}".format(rng_num, player_num))