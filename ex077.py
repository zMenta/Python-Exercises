#listador de vogais em tuplas
print()
words = ("Batata", "Milho", "Pineapple", "Apfel", "Orange")



for c in range(0,len(words)):

    print(f"Na palavra {words[c]} existe as seguintes vogais: ", end="")

    
    #Verificar de letras em cada palavra
    if words[c].upper().count("A") >= 1:
        print("A", end=" ")
    if words[c].upper().count("E") >= 1:
        print("E", end=" ")
    if words[c].upper().count("I") >= 1:
        print("I", end =" ")
    if words[c].upper().count("O") >= 1:
        print("O", end=" ")
    if words[c].upper().count("U") >= 1:
        print("U", end="")
    
    print("\n")

