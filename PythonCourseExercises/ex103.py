#Create a player form, informing his name and goals that he made. 2 optional parameters.

def form(p="<unkown>",g=0):
    """
    param: p -> player name;
    param: g -> goals that this player made;

    Both optional 
    """
    print(f"Players name: {p} | Goals: {g}")


#main body
form()
form("Pablo",2)
form(g=5)