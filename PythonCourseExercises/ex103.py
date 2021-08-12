#Create a player form, informing his name and goals that he made. 2 optional parameters.

def form(p="<unkown>",g=0):
    """
    param: p -> player name;
    param: g -> goals that this player made;

    Both optional 
    """
    if p == "":
        p = "<unkown>"
    if g == "":
        g = 0
    print(f"Players name: {p} | Goals: {g}")


#main body
a = input("Type the players name: ")
b = input("The amount of goals he/she made: ")

form(a,b)
