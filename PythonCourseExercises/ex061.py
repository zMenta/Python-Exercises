# Progressão Aritimética
answer = "Y"

while answer == "Y":
    c = 0
    start_num = int(input("Type the starting number of the Arithimetic Progression:"))
    rate = int(input("Type the rate:"))

    while c != 10:
        c += 1
        start_num += rate
        print("Term:{} ----- Value:{}".format(c, start_num).center(30))

    answer = str(input("Do you want to try again? (Y to continue):")).upper()

print("END OF THE PROGRAM")
