#Validating inputs

c = 0
sex = ""

#Take closer look on the AND 
while c != 1:
    sex = str(input("Please type your sex:")).strip().upper()
    if sex != "M" and sex != "F":
        print("Invalid. please try again.")
    else:
        c += 1
print("Nice sex")


'''c = 0
sex = ""

while c != 1:
    sex = str(input("Please type your sex:")).upper()
    if sex == "M" or sex == "F":
        print("Nice sex")
        c += 1
    else:
        print("Please try again.")'''