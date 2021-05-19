#Check if the user typed the correct numbers of parenthesis of an expression. Example (a+b) -> valid expression. (a+b*(c) -> invalid

expression = str(input("Type a math expression: "))
pile = []

for index in expression:  
    if index == "(":
        pile.append(index)
    elif index == ")":
        if len(pile) > 0:
            pile.pop()
        else:
            pile.append(index)
            break

if len(pile) == 0:
    print("The expression is VALID!")
else:
    print("The expression is INVALID")
    