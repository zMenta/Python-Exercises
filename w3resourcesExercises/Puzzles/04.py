# We are making n stone piles! The first pile has n stones. If n is even, then all piles have an even number of stones. If n is odd, all piles have an odd number of stones. Each pile must more stones than the previous pile but as few as possible. Write a Python program to find the number of stones n each pile.#

pile_size = int(input("Type stone pile amount: "))

stone_pile = []

for i in range(pile_size):
    stone_pile.append(pile_size)
    pile_size += 2

print(stone_pile)
