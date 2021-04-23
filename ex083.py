#Check if the user typed the correct numbers of parenthesis of an expression. Example (a+b) -> valid expression. (a+b*(c) -> invalid

expression = str(input("Type your expression with parenthesis:"))

#sum of "(" ")"
parenthesis = expression.count("(") + expression.count(")")

#Expression validator
if parenthesis%2 == 0:
    print("It's a valid expression")
else:
    print("It's a invalid expression")

print("-"*30)
