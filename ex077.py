#listador de vogais em tuplas

words = ("Batata", "Milho", "Pineapple")

print(f"Na palavra {words[0]} existe as seguintes vogais: ", end="")


for c in words:
    if c.upper().count("A") >= 1:
        print("A", end=" ")
    if c.upper().count("E") >= 1:
        print("E", end=" ")
    if c.upper().count("I") >= 1:
        print("I", end =" ")

