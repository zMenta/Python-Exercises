#Adivinha numero v2

from random import randint

pc_num = randint(1,10)
guess = 0
tries = 0

while guess != pc_num:
    guess = int(input("Try to guess a number(1-10):"))
    if guess != pc_num:
        tries += 1
    
print("Congratulation, you guessed it right!. Total tries: {}".format(tries))