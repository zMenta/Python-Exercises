# highest number and lowest 

a = int(input(("Type the number A: ")))
b = int(input(("Type the number B: ")))
c = int(input(("Type the number C: ")))

'''# First method
# print("The biggest number in crescent order is ", end = "")

# if a > b:
#     if a > c:
#         high = a
#     else: 
#         high = c 
# elif b > c:
#     high = b
# else:
#     high = c

# print(f"The highest number is: {high}")

# if a < b:
#     if a < c:
#         mini = a
#     else: 
#         mini = c 
# elif b < c:
#     mini = b
# else:
#     mini = c

# print(f"The minimal number is: {mini}")'''

# second method 

if a >= b and a >= c:
    high = a
    if b >= c:
        high2 = b
        mini = c
    else:
        high2 = c
        mini = b
elif b >= a and b >= c:
    high = b
    if a >= c:
        high2 = a
        mini = c
    else:
        high2 = c
        mini = a
elif c >= b and c >= a:
    high = c
    if b >= a:
        high2 = b
        mini = a
    else:  
        high2 = a
        mini = b

print(f"The crescent order is {mini} , {high2} , {high}.")

print(f"\nThe decrescent order is {high}, {high2}, {mini}.")

print(f"\nThe biggest numbe is in between {high2}, {high}, {mini}.")
