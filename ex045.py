#Rock, paper and scissors

from random import randint

colors = { 
    "red": "\033[1;31m",
    "green": "\033[1;32m",
    "blue": "\033[1;34m",
    "normal": "\033[0;0;0m",
    "won": "\033[1;33mWon!\033[0;0;0m",
    "lose": "\033[1;35mLose!\033[0;0;0m"
}

plays = {
    1: "\033[1;31mRock\033[0;0;0m",
    2: "\033[1;32mPaper\033[0;0;0m",
    3: "\033[1;34mScissors\033[0;0;0m"
}

pc_play = randint(1,3)

hu_play = (input("""
Please choose one to play:

{}1 - Rock{}

{}2 - Paper{}

{}3 - Scissors{}

""".format(colors["red"], colors["normal"], colors["green"], colors["normal"], colors["blue"], colors["normal"])))
if hu_play.isnumeric() == True and int(hu_play) >=1 and int(hu_play) <=3 :
    hu_play = int(hu_play)
    print("\nYou chose {} and the computer chose {}.".format(plays[hu_play], plays[pc_play]))

    #Win Conditions
    if hu_play == pc_play:
        print("Nobody wins!")
    elif hu_play == 1 and pc_play == 3:
        print("Congratulations! You {}".format(colors["won"]))
    elif hu_play == 2 and pc_play == 1:
        print("Congratulations! You {}".format(colors["won"]))
    elif hu_play == 3 and pc_play == 2:
        print("Congratulations! You {}".format(colors["won"]))
    else:
        print("You {}".format(colors["lose"]))
else:
    print("Invalid Input.")