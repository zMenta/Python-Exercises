# Progressão Aritimética

answer = "Y"

while answer == "Y":
    choice = 10
    c = 0
    start_num = int(input("Type the starting number of the Arithimetic Progression:"))
    rate = int(input("Type the rate:"))

    while c != choice:
        c += 1
        start_num += rate
        print("Term:{} ----- Value:{}".format(c, start_num).center(30))
        if c == choice:
            choice = int(input("Want to show more terms? How many? (type 0 to stop)"))
            c = 0

    answer = str(input("Do you want to try again? (Y to continue):")).upper()

print("END OF THE PROGRAM")