#gambler helper. Helps a gambler to come up with lucky numbers.

from random import randint

gambles = []

for i in range(int(input("How many guesses you want to make?"))):
    guess = []
    for c in range(6): #generating guesses for the gamble
        number = randint(1,60)
        guess.append(number)
    
    gambles.append(guess[:])

print("="*50)
for i in range(len(gambles)):
    print(f"Guess {i} : {gambles[i]}")
print("="*50)
